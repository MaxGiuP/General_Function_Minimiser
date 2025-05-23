import numpy as np
import sympy as sp
from fractions import Fraction

# === User inputs ===
f_str = "x0 - x1 + 0.86*x0*x1 + 2*(x0**2) + x1**2"  # define function as string
x0 = np.array([0.0, 0.0])   # starting point
num_iterations = 2          # number of CG steps

# === Symbolic setup ===
n = len(x0)
x_syms = sp.symbols(f'x0:{n}')
l = sp.symbols('l')
f_expr = sp.sympify(f_str)

# Precompute gradient symbolic and numeric
grad_syms = [sp.diff(f_expr, xi) for xi in x_syms]
grad_num = sp.lambdify(x_syms, grad_syms, 'numpy')
f_num    = sp.lambdify(x_syms, f_expr,    'numpy')

# Formatter
def fmt_frac(v):
    fr = Fraction(v).limit_denominator()
    return f"{fr.numerator}/{fr.denominator}" if fr.denominator != 1 else str(fr.numerator)

# === Initialization ===
x = x0.copy()
g_prev = np.array(grad_num(*x), dtype=float)
p = -g_prev  # initial search direction

# === Conjugate Gradient Iteration with line-search each step ===
for k in range(1, num_iterations + 1):
    # 1) Line-search: minimize along p
    subs = {x_syms[i]: x[i] + l * p[i] for i in range(n)}
    phi = f_expr.subs(subs)
    dphi = sp.diff(phi, l)
    sols = sp.solve(dphi, l)
    real_ls = [float(sol.evalf()) for sol in sols if sol.is_real]
    if not real_ls:
        raise RuntimeError(f"No real line-search at iter {k}")
    alpha = real_ls[0]

    # 2) Update x
    x = x + alpha * p
    fx = f_num(*x)

    # 3) Output
    print(f"Iteration {k}")
    print("--------------------")
    print(f"alpha_{k} = {alpha:.8f}")
    print(f"x_{k}      = ({', '.join(fmt_frac(v) for v in x)})")
    print(f"f(x_{k})   = {fx:.8f}\n")

    # 4) Compute new gradient and direction
    g = np.array(grad_num(*x), dtype=float)
    beta = (g.dot(g)) / (g_prev.dot(g_prev))
    p = -g + beta * p
    g_prev = g.copy()
