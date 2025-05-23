import numpy as np
import sympy as sp
from fractions import Fraction

# === User inputs ===
f_str = "2*x0 - 2*x1 + 1.8*x0*x1 + x0**2 + x1**2"
initial_guess  = [0.0, 0.0]
num_iterations = 3

# === Setup symbolic expressions ===
num_vars = len(initial_guess)
x_syms = sp.symbols(f'x0:{num_vars}')
f_expr = sp.sympify(f_str)
grad_syms = [sp.diff(f_expr, xi) for xi in x_syms]
hess_syms = [[sp.diff(g, xj) for xj in x_syms] for g in grad_syms]

# Lambdify numeric functions
f_num    = sp.lambdify(x_syms, f_expr, 'numpy')
grad_num = sp.lambdify(x_syms, grad_syms, 'numpy')
hess_num = sp.lambdify(x_syms, hess_syms, 'numpy')

# Formatter for display
def fmt_frac(v):
    fr = Fraction(v).limit_denominator()
    return f"{fr.numerator}/{fr.denominator}" if fr.denominator != 1 else str(fr.numerator)

# === Newton's method iterations ===
x = np.array(initial_guess, dtype=float)

for i in range(1, num_iterations + 1):
    # Save old x
    x_old = x.copy()
    
    # Evaluate at x_old
    f_old = f_num(*x_old)
    g_old = np.array(grad_num(*x_old), dtype=float)
    H_old = np.array(hess_num(*x_old), dtype=float)
    
    # Compute Newton step
    delta = np.linalg.solve(H_old, g_old)
    x = x_old - delta
    
    # Evaluate at new x
    f_new = f_num(*x)
    g_new = np.array(grad_num(*x), dtype=float)
    H_new = np.array(hess_num(*x), dtype=float)
    
    # Print iteration results
    print(f"\nIteration {i}")
    print("--------------")
    print(f"x[{i-1}]       = ({', '.join(fmt_frac(v) for v in x_old)})")
    print(f"f(x[{i-1}])    = {f_old:.6f}")
    print(f"∇f(x[{i-1}])   = {list(g_old)}")
    print("Hessian old:")
    print(H_old)
    print(f"Newton step δ = {list(delta)}")
    print(f"x[{i}]        = ({', '.join(fmt_frac(v) for v in x)})")
    print(f"f(x[{i}])     = {f_new:.6f}")
    print(f"∇f(x[{i}])    = {list(g_new)}")
    print("Hessian new:")
    print(H_new)
    print("--------------")
