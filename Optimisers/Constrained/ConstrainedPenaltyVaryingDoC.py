import numpy as np
import sympy as sp
from scipy.optimize import minimize
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def varying_doc(f_str, eq_strs=None, ineq_strs=None,
                R=1e3, initial_guess=None, method='BFGS', plot=False):
    # 0) Clean empty inputs
    eq_strs   = [s for s in (eq_strs or [])   if s.strip()]
    ineq_strs = [s for s in (ineq_strs or []) if s.strip()]
    logs = []

    # 1) Parse objective & constraints
    f_expr     = sp.sympify(f_str)
    eq_exprs   = [sp.sympify(s) for s in eq_strs]
    ineq_exprs = [sp.sympify(s) for s in ineq_strs]

    # 2) Auto‐detect variables
    vars_syms = sorted(
        f_expr.free_symbols
         .union(*(e.free_symbols for e in eq_exprs))
         .union(*(h.free_symbols for h in ineq_exprs)),
        key=lambda s: s.name
    )
    n = len(vars_syms)
    if n == 0:
        raise ValueError("No decision variables found.")

    # 3) Lambdify
    f_num    = sp.lambdify(tuple(vars_syms),             f_expr,    'numpy')
    eq_funcs = [sp.lambdify(tuple(vars_syms), e,        'numpy') for e in eq_exprs]
    ineq_funcs= [sp.lambdify(tuple(vars_syms), h,       'numpy') for h in ineq_exprs]

    # 4) Penalty objective: R*(violation)^2
    def F(x):
        val = f_num(*x)
        # equality: penalty = R*(h(x))^2
        for ef in eq_funcs:
            v = ef(*x)
            val += R * (v**2)
        # inequality: penalty = R*max(0,-g(x))^2
        for hf in ineq_funcs:
            v = hf(*x)
            if v < 0:
                val += R * ((-v)**2)
        return val

    # 5) Initial guess: avoid zero divide
    x0 = np.ones(n) if initial_guess is None else np.array(initial_guess, dtype=float)

    # 6) Unconstrained solve
    res = minimize(F, x0, method=method)
    sol = res.x
    f_star = f_num(*sol)

    # 7) Constraint evaluations
    eq_viol = [ef(*sol) for ef in eq_funcs]
    ineq_viol = [hf(*sol) for hf in ineq_funcs]

    # 8) Build logs
    logs.append("Optimal solution:\n")
    for v, xi in zip(vars_syms, sol):
        logs.append(f"  {v} = {xi:.6f}\n")
    logs.append(f"  f*  = {f_star:.6f}\n\n")

    if eq_viol:
        logs.append("Equality residuals (should be ≈0):\n")
        for s, rv in zip(eq_strs, eq_viol):
            logs.append(f"  {s} = {rv:.6e}\n")
    if ineq_viol:
        logs.append("Inequality residuals (must be ≥0):\n")
        for s, rv in zip(ineq_strs, ineq_viol):
            logs.append(f"  {s} = {rv:.6e}\n")

    # 9) Optional plot if 2D
    if plot and n == 2:
        x_sym, y_sym = vars_syms
        xs = np.linspace(sol[0]-1, sol[0]+1, 200)
        ys = np.linspace(sol[1]-1, sol[1]+1, 200)
        X, Y = np.meshgrid(xs, ys)
        Z = f_num(X, Y)
        plt.contour(X, Y, Z, levels=50, cmap='viridis')
        plt.plot(sol[0], sol[1], 'ro', label='Solution')
        plt.title("Quadratic Penalty Solution")
        plt.xlabel(str(x_sym)); plt.ylabel(str(y_sym))
        plt.legend(); plt.grid(True); plt.show()

    return "".join(logs)


"""
# Example usage:
if __name__ == "__main__":
    # minimize  x0^2 + x1^2  subject to x0 + x1 = 1  and  x0 >= 0.2
    out = varying_doc(
        f_str="x0**2 + x1**2",
        eq_strs=["x0 + x1 - 1"],
        ineq_strs=["x0 - 0.2"],
        R=1e3,
        initial_guess=[0.5, 0.5],
        method='BFGS',
        plot=False
    )
    print(out)
"""