import sympy as sp
import numpy as np

def fuzzy(func_strs, thresholds):
    x = sp.symbols('x', positive=True, real=True)
    funcs = [sp.sympify(s) for s in func_strs]
    
    acc, unacc = thresholds[0]

    mu_syms = [(unacc - f)/(unacc - acc) for f in funcs]
    mu_total = sum(mu_syms)

    dmu = sp.diff(sp.simplify(mu_total), x)
    sols = sp.solve(dmu, x)
    crit_points = [
        float(sol) for sol in sols
        if sol.is_real and acc < sol < float(sp.sqrt(unacc))
    ]
    if not crit_points:
        raise RuntimeError("No critical point found in (acc, sqrt(unacc)).")
    x_crit = crit_points[0]

    mu_num = sp.lambdify(x, mu_total, 'numpy')
    f_nums = [sp.lambdify(x, f, 'numpy') for f in funcs]

    x_lb = acc
    x_ub = float(sp.sqrt(unacc))
    candidates = [x_crit, x_lb, x_ub]

    mu_vals = [(xi, mu_num(xi)) for xi in candidates]
    x_best, mu_best   = max(mu_vals, key=lambda t: t[1])
    x_worst, mu_worst = min(mu_vals, key=lambda t: t[1])

    f_best  = [fn(x_best)  for fn in f_nums]
    f_worst = [fn(x_worst) for fn in f_nums]

    best = {
        'x':      x_best,
        'mu':     mu_best,
        'f_vals': f_best
    }
    worst = {
        'x':      x_worst,
        'mu':     mu_worst,
        'f_vals': f_worst
    }

    return best, worst