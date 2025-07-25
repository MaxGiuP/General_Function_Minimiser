import sympy as sp
import numpy as np

"""
x = sp.symbols('x', positive=True, real=True)

# === User inputs ===
# Symbol for the decision variable
func_strs = ["1.137/x", "0.923*(x**2)"]
funcs = [sp.sympify(s) for s in func_strs]
thresholds = [(0.5, 2.0), (0.5, 2.0)]
# ===================
"""

def fuzzy(func_strs, thresholds):
    x = sp.symbols('x', positive=True, real=True)
    funcs = [sp.sympify(s) for s in func_strs]

    acc, unacc = thresholds[0]

    mu_total = 0
    for f in funcs:
        mu = (unacc - f) / (unacc - acc)
        mu_total += mu
    dmu = sp.diff(mu_total, "x")
    sols = sp.solve(sp.simplify(dmu), "x")
    
    crit = [s.evalf() for s in sols 
            if s.is_real and acc < s < sp.sqrt(unacc)]
    if not crit:
        raise RuntimeError("No critical point in domain")
    x_best = float(crit[0])

    x_low  = acc
    x_high = float(sp.sqrt(unacc))

    mu_num = sp.lambdify(x, mu_total, 'numpy')
    f_nums = [sp.lambdify(x, f, 'numpy') for f in funcs]

    candidates = [x_best, x_low, x_high]
    vals = [(xi, mu_num(xi)) for xi in candidates]
    x_best, mu_best   = max(vals, key=lambda t: t[1])
    x_worst, mu_worst = min(vals, key=lambda t: t[1])

    f_best  = [fn(x_best)  for fn in f_nums]
    f_worst = [fn(x_worst) for fn in f_nums]
    best, worst = (x_best, mu_best, *f_best), (x_worst, mu_worst, *f_worst)
    
    logs = []
    logs.append(f"best  = ({best[0]:.6f}, {best[1]:.5f}, {best[2]:.4f}, {best[3]:.5f})\n")
    logs.append(f"worst = ({worst[0]:.6f}, {worst[1]:.5f}, {worst[2]:.5f}, {worst[3]:.0f})")
    
    return "".join(logs)