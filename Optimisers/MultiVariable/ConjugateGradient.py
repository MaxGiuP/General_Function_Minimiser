import numpy as np
import sympy as sp
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def conjugate_gradient(f_str, start, num_iterations=1, plot=False):
    # --- Symbolic setup ---
    n = len(start)
    x_syms = sp.symbols(f'x0:{n}')         # (x0, x1, ..., x{n-1})
    l = sp.Symbol('l')
    f_expr = sp.sympify(f_str)

    # gradient expressions
    grad_exprs = [sp.diff(f_expr, xi) for xi in x_syms]

    # numeric lambdas
    f_num    = sp.lambdify(x_syms, f_expr,    'numpy')
    grad_num = sp.lambdify(x_syms, grad_exprs, 'numpy')

    # --- Initialization ---
    x_k    = np.array(start, dtype=float)
    g_prev = np.array(grad_num(*x_k), dtype=float).flatten()
    p      = -g_prev
    trajectory = [x_k.copy()]
    history    = []

    # --- CG iterations ---
    for k in range(1, num_iterations + 1):
        # 1) exact line‐search along p:
        subs = {x_syms[i]: x_k[i] + l*p[i] for i in range(n)}
        phi  = f_expr.subs(subs)
        dphi = sp.diff(phi, l)
        sols = sp.solve(dphi, l)
        # pick the first real solution
        real_ls = [sol for sol in sols if sol.is_real]
        if not real_ls:
            print(f"Iteration {k}: no real step length found—stopping.")
            break
        alpha = float(real_ls[0])

        # 2) update x
        x_k = x_k + alpha * p
        f_val = float(f_expr.subs({x_syms[i]: x_k[i] for i in range(n)}).evalf())

        # 3) record & print
        history.append({
            'iteration': k,
            'alpha':    alpha,
            'x':        x_k.copy(),
            'f':        f_val
        })
        trajectory.append(x_k.copy())

        print(f"\nConjugate-Gradient Iter {k}")
        print("------------------------------")
        print(f"  alpha_{k}  = {alpha:.8f}")
        print(f"  x_{k}      = {x_k.tolist()}")
        print(f"  f(x_{k})   = {f_val:.8f}")

        # 4) new gradient & direction
        g = np.array(grad_num(*x_k), dtype=float).flatten()
        beta = (g.dot(g)) / (g_prev.dot(g_prev))
        p    = -g + beta * p
        g_prev = g.copy()

    trajectory = np.vstack(trajectory)

    # --- Optional 2D plot ---
    if plot and n == 2:
        # build a grid around your trajectory
        mins = trajectory.min(axis=0) - 1
        maxs = trajectory.max(axis=0) + 1
        xs = np.linspace(mins[0], maxs[0], 200)
        ys = np.linspace(mins[1], maxs[1], 200)
        X, Y = np.meshgrid(xs, ys)
        Z = f_num(X, Y)
        plt.contour(X, Y, Z, levels=40, cmap='viridis')
        traj = trajectory
        plt.plot(traj[:,0], traj[:,1], 'o-', color='red', label='CG path')
        plt.title("Conjugate Gradient on " + f_str)
        plt.xlabel(str(x_syms[0]))
        plt.ylabel(str(x_syms[1]))
        plt.legend()
        plt.grid(True)
        plt.show()

    return trajectory, history

"""
# === Example usage ===
if __name__ == "__main__":
    traj, hist = conjugate_gradient(
        f_str="x0 - x1 + 0.86*x0*x1 + 2*(x0**2) + x1**2",
        x0=[0.0, 0.0],
        num_iterations=3,
        plot=True
    )

    print("\nFinal trajectory:\n", traj)
    print("History:")
    for entry in hist:
        print(entry)
"""