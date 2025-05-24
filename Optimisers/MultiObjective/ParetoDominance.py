import numpy as np
import sympy as sp
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def pareto_front(func_strs, num_weights=100, plot=False):
    syms = set()
    exprs = []
    for s in func_strs:
        e = sp.sympify(s)
        exprs.append(e)
        syms |= e.free_symbols
    if len(syms) != 1:
        raise ValueError("Expected exactly one decision variable")
    var = syms.pop()

    def find_minimizer(e):
        d1 = sp.diff(e, var)
        crits = sp.solve(d1, var)
        d2 = sp.diff(e, var, 2)
        mins = [c for c in crits if c.is_real and d2.subs(var, c) > 0]
        if not mins:
            raise RuntimeError(f"No real minimizer for {e}")
        # pick the one with smallest f-value
        return float(min(mins, key=lambda c: float(e.subs(var, c))))

    endpoints = []
    for e in exprs:
        xi = find_minimizer(e)
        vals = [float(f.subs(var, xi)) for f in exprs]
        endpoints.append((xi, *vals))

    Phi = sum(exprs)
    x_eq = find_minimizer(Phi)
    vals_eq = [float(f.subs(var, x_eq)) for f in exprs]
    compromise = (x_eq, *vals_eq)

    pareto_points = []
    if len(exprs) == 2:
        f1, f2 = exprs
        alphas = np.linspace(0, 1, num_weights)
        for α in alphas:
            Phiα = α*f1 + (1-α)*f2
            try:
                xi = find_minimizer(Phiα)
            except RuntimeError:
                continue
            pareto_points.append((float(f1.subs(var, xi)), float(f2.subs(var, xi))))

    if plot and len(exprs) == 2 and pareto_points:
        f1_vals, f2_vals = zip(*pareto_points)
        plt.scatter(f1_vals, f2_vals, s=20)
        plt.title("Pareto Front (f1 vs f2)")
        plt.xlabel("f1")
        plt.ylabel("f2")
        plt.grid(True)
        plt.show()

    return endpoints, compromise, pareto_points
