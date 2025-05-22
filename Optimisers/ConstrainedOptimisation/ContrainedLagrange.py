"""
2. The function 2
5 ( , )
xy
f x y = is to be minimized inside a circle of
radius 2 centred at the origin. Use the method of Lagrange
multipliers to find the location of all minima clearly showing how
you have dealt with the constraint.
"""

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# ────────────────────────────────────────────────────────────────
#  USER INPUT
# ────────────────────────────────────────────────────────────────
var_names = ["x", "y"]
f_str     = "5 / (x*y**2)"
g_strs    = ["x**2 + y**2 - 4 = 0"]
params    = {}

# ────────────────────────────────────────────────────────────────
#  REST OF YOUR ORIGINAL SOLVER (unchanged)
# ────────────────────────────────────────────────────────────────
vars_syms = sp.symbols(var_names, real=True)
loc       = dict(zip(var_names, vars_syms)) | params

f = sp.sympify(f_str, locals=loc)

clean = []
for s in g_strs:
    t = s.replace(" ", "")
    clean.append(t if "=" not in t else "(" + t.replace("=", ")-(") + ")")
g_list = [sp.sympify(expr, locals=loc) for expr in clean]

lam_syms = sp.symbols(f"lam0:{len(g_list)}", real=True)
L = f + sum(lam * g for lam, g in zip(lam_syms, g_list))

eqs = [sp.diff(L, v) for v in vars_syms] + g_list
sols = sp.solve(eqs, (*vars_syms, *lam_syms), dict=True)

good = [s for s in sols
        if all(s[v].is_real for v in vars_syms)
        and all(abs(sp.N(g.subs(s))) < 1e-10 for g in g_list)]

if not good:
    print("No real stationary point satisfies all constraints.")
else:
    print(f"Found {len(good)} feasible stationary point(s):\n")
    for k, s in enumerate(good, 1):
        print(f"Point {k}:")
        for v in vars_syms:
            print(f"  {v} = {float(sp.N(s[v], 6)):.6g}")
        print(f"  f = {float(sp.N(f.subs(s), 6)):.6g}\n")
