import numpy as np
import sympy as sp
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from fractions import Fraction

def newton_multivariate(f_str, initial_guess, num_iterations=1, plot=False):
    """
    Multivariate Newton’s method that auto-detects the variable symbols
    (e.g. x0,x1 or x2,x3) from f_str, captures all console output into
    a returned string instead of printing.
    """
    # 1) parse and detect symbols
    f_expr = sp.sympify(f_str)
    syms = sorted(f_expr.free_symbols, key=lambda s: s.name)
    n = len(syms)
    if n != len(initial_guess):
        raise ValueError(f"Detected symbols {syms} but initial_guess has length {len(initial_guess)}")
    
    # 2) build lambdas
    grad_syms = [sp.diff(f_expr, v) for v in syms]
    hess_syms = [[sp.diff(g, v) for v in syms] for g in grad_syms]
    f_num    = sp.lambdify(tuple(syms), f_expr,    'numpy')
    grad_num = sp.lambdify(tuple(syms), grad_syms, 'numpy')
    hess_num = sp.lambdify(tuple(syms), hess_syms, 'numpy')

    # 3) formatter
    def fmt_frac(v):
        fr = Fraction(v).limit_denominator()
        return f"{fr.numerator}/{fr.denominator}" if fr.denominator != 1 else str(fr.numerator)

    # 4) iterate
    x = np.array(initial_guess, dtype=float)
    logs = []
    trajectory = [x.copy()]

    for i in range(1, num_iterations+1):
        x_old = x.copy()
        f_old = float(f_num(*x_old))
        g_old = np.array(grad_num(*x_old), dtype=float).flatten()
        H_old = np.array(hess_num(*x_old), dtype=float)

        # Newton step
        delta = np.linalg.solve(H_old, g_old)
        x = x_old - delta

        f_new = float(f_num(*x))
        g_new = np.array(grad_num(*x), dtype=float).flatten()
        H_new = np.array(hess_num(*x), dtype=float)

        # log
        logs.append(f"\nIteration {i}\n")
        logs.append("--------------\n")
        logs.append(f"vars = {syms}\n")
        logs.append(f"x_old = [{', '.join(fmt_frac(v) for v in x_old)}]\n")
        logs.append(f"f_old = {f_old:.6f}\n")
        logs.append(f"grad  = {g_old.tolist()}\n")
        logs.append("Hess old:\n"); logs.append(f"{H_old}\n")
        logs.append(f"delta = {delta.tolist()}\n")
        logs.append(f"x_new = [{', '.join(fmt_frac(v) for v in x)}]\n")
        logs.append(f"f_new = {f_new:.6f}\n")
        logs.append(f"grad' = {g_new.tolist()}\n")
        logs.append("Hess new:\n"); logs.append(f"{H_new}\n")
        logs.append("--------------\n")

        trajectory.append(x.copy())

    # 5) optional plot if exactly 2 vars
    if plot and n==2:
        xs = np.linspace(trajectory[:,0].min()-1, trajectory[:,0].max()+1, 200)
        ys = np.linspace(trajectory[:,1].min()-1, trajectory[:,1].max()+1, 200)
        X,Y = np.meshgrid(xs, ys)
        Z = f_num(X, Y)
        plt.contour(X, Y, Z, levels=40, cmap='viridis')
        traj = np.vstack(trajectory)
        plt.plot(traj[:,0], traj[:,1], 'o-', color='red', label='Newton path')
        plt.title("Newton's Method on " + f_str)
        plt.xlabel(str(syms[0])); plt.ylabel(str(syms[1]))
        plt.legend(); plt.grid(True); plt.show()

    return "".join(logs)

"""
# Example usage:
if __name__ == "__main__":
    log = newton_multivariate(
        f_str="2*x2 - 2*x3 + x2**2 + x3**2",
        initial_guess=[1.0, 2.0],
        num_iterations=3,
        plot=False
    )
    print(log)
"""