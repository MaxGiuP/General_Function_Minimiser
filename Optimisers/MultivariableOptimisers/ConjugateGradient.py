import numpy as np
import sympy as sp
from fractions import Fraction

# === User inputs ===
def f(x):
    # objective (x: NumPy array or tuple of sympy symbols)
    return x[0] - x[1] + 2*x[0]**2 + 2*x[0]*x[1] + x[1]**2

x0             = np.array([0.0, 0.0])   # starting point
p0             = np.array([-1.0,  1.0]) # initial search direction (should be -grad at x0)
lam1           = 1.0                    # initial step-length
num_iterations = 2                      # number of CG steps
# ====================

# build symbols and symbolic f + gradient
def build_symbolic():
    n = len(x0)
    x_syms = sp.symbols(f'x0:{n}')
    l = sp.symbols('l')
    f_expr = f(x_syms)
    grad_syms = [sp.diff(f_expr, xi) for xi in x_syms]
    return x_syms, l, f_expr, grad_syms

x_syms, l, f_expr, grad_syms = build_symbolic()
# lambdify for numeric
grad_num = sp.lambdify(x_syms, grad_syms, 'numpy')
f_num    = sp.lambdify(x_syms, f_expr,    'numpy')

# helper to format fractions
def fmt_frac(v):
    fr = Fraction(v).limit_denominator()
    return f"{fr.numerator}/{fr.denominator}" if fr.denominator!=1 else str(fr.numerator)

grad_prev = np.array(grad_num(*x0), dtype=float)
p = p0.astype(float).copy()
lam = lam1
x = x0.astype(float).copy()

for k in range(1, num_iterations+1):
    x = x + lam * p
    fx = f_num(*x)

    # print iteration
    print(f"Iteration {k}")
    print("--------------------")
    print(f"lambda_{k} = {fmt_frac(lam)}")
    print(f"x_{k}      = ({', '.join(fmt_frac(v) for v in x)})")
    print(f"f(x_{k})   = {fx:.2f}\n")

    g = np.array(grad_num(*x), dtype=float)
    beta = (g.dot(g)) / (grad_prev.dot(grad_prev))
    p = -g + beta * p
    grad_prev = g.copy()

    if k < num_iterations:
        subs = { x_syms[i]: x[i] + l*p[i] for i in range(len(x0)) }
        phi  = f_expr.subs(subs)
        dphi = sp.diff(phi, l)
        sols = sp.solve(dphi, l)
        real_ls = [float(sol.evalf()) for sol in sols if sol.is_real]
        if not real_ls:
            raise RuntimeError(f"No real line-search at iter {k+1}")
        lam = real_ls[0]