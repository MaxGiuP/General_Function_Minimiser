import numpy as np
import sympy as sp
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from fractions import Fraction

def newton_multivariate(f_str, initial_guess, num_iterations=1, plot=False):
    # Symbolic setup
    x0 = np.array(initial_guess, dtype=float)
    n = len(x0)
    x_syms = sp.symbols(f'x0:{n}')
    f_expr = sp.sympify(f_str)
    grad_syms = [sp.diff(f_expr, xi) for xi in x_syms]
    hess_syms = [[sp.diff(g, xj) for xj in x_syms] for g in grad_syms]

    # Lambdify
    f_num    = sp.lambdify(x_syms, f_expr,    'numpy')
    grad_num = sp.lambdify(x_syms, grad_syms, 'numpy')
    hess_num = sp.lambdify(x_syms, hess_syms, 'numpy')

    # Formatter
    def fmt_frac(v):
        fr = Fraction(v).limit_denominator()
        return f"{fr.numerator}/{fr.denominator}" if fr.denominator != 1 else str(fr.numerator)

    # Initialize
    x = x0.copy()
    trajectory = [x.copy()]
    history = []

    for i in range(1, num_iterations + 1):
        x_old = x.copy()
        f_old = float(f_num(*x_old))
        g_old = np.array(grad_num(*x_old), dtype=float).flatten()
        H_old = np.array(hess_num(*x_old), dtype=float)

        # Newton step: solve H_old * delta = g_old
        delta = np.linalg.solve(H_old, g_old)
        x = x_old - delta

        f_new = float(f_num(*x))
        g_new = np.array(grad_num(*x), dtype=float).flatten()
        H_new = np.array(hess_num(*x), dtype=float)

        # Record
        history.append({
            'iteration':  i,
            'x_old':      x_old.copy(),
            'f_old':      f_old,
            'grad_old':   g_old.copy(),
            'hess_old':   H_old.copy(),
            'delta':      delta.copy(),
            'x_new':      x.copy(),
            'f_new':      f_new,
            'grad_new':   g_new.copy(),
            'hess_new':   H_new.copy()
        })
        trajectory.append(x.copy())

        # Print
        print(f"\nIteration {i}")
        print("--------------")
        print(f"x[{i-1}]       = ({', '.join(fmt_frac(v) for v in x_old)})")
        print(f"f(x[{i-1}])    = {f_old:.6f}")
        print(f"∇f(x[{i-1}])   = {g_old.tolist()}")
        print("Hessian old:")
        print(H_old)
        print(f"Newton step δ = {delta.tolist()}")
        print(f"x[{i}]        = ({', '.join(fmt_frac(v) for v in x)})")
        print(f"f(x[{i}])     = {f_new:.6f}")
        print(f"∇f(x[{i}])    = {g_new.tolist()}")
        print("Hessian new:")
        print(H_new)
        print("--------------")

    trajectory = np.vstack(trajectory)

    # Optional plot for 2D
    if plot and n == 2:
        xs = np.linspace(trajectory[:,0].min()-1, trajectory[:,0].max()+1, 200)
        ys = np.linspace(trajectory[:,1].min()-1, trajectory[:,1].max()+1, 200)
        X, Y = np.meshgrid(xs, ys)
        Z = f_num(X, Y)
        plt.contour(X, Y, Z, levels=40, cmap='viridis')
        traj = trajectory
        plt.plot(traj[:,0], traj[:,1], 'o-', color='red', label='Newton path')
        plt.title("Newton's Method on " + f_str)
        plt.xlabel(str(x_syms[0]))
        plt.ylabel(str(x_syms[1]))
        plt.legend()
        plt.grid(True)
        plt.show()

    return trajectory, history

"""
# Example usage
if __name__ == "__main__":
    traj, hist = newton_multivariate(
        f_str="2*x0 - 2*x1 + 1.8*x0*x1 + x0**2 + x1**2",
        initial_guess=[0.0, 0.0],
        num_iterations=3,
        plot=True
    )
    print("\nFinal trajectory:\n", traj)
    print("History entries:")
    for entry in hist:
        print(entry)
"""