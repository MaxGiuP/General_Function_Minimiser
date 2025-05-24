import sympy as sp
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def steepest_descent(f_str, start, num_iterations=1, plot=False):
    # --- Parse and lambdify ---
    f_expr = sp.sympify(f_str)
    syms = sorted(f_expr.free_symbols, key=lambda s: s.name)
    n = len(syms)
    if n < 1:
        raise ValueError("No variables found in the function string.")
    # gradient expressions
    grad_expr = [sp.diff(f_expr, v) for v in syms]
    # lambdified functions
    f_num = sp.lambdify(tuple(syms), f_expr, 'numpy')
    grad_num = sp.lambdify(tuple(syms), grad_expr, 'numpy')
    # symbol for line‐search
    l = sp.Symbol('l')

    # initial setup
    x_k = np.array(start, dtype=float)
    trajectory = [x_k.copy()]
    history = []

    for k in range(1, num_iterations + 1):
        # compute gradient at x_k
        grad_k = np.array(grad_num(*x_k), dtype=float).flatten()
        # descent direction
        d_k = -grad_k

        # build φ(l) = f(x_k + l d_k)
        x_l_subs = {syms[i]: x_k[i] + l * d_k[i] for i in range(n)}
        f_l = f_expr.subs(x_l_subs)
        df_dl = sp.diff(f_l, l)
        sols = sp.solve(df_dl, l)
        # filter real solutions
        real_steps = [float(sol.evalf()) for sol in sols if sol.is_real]
        if not real_steps:
            print(f"Iteration {k}: no real step length found—stopping.")
            break
        l_star = real_steps[0]

        # update point
        x_new = x_k + l_star * d_k
        f_new = float(f_expr.subs({syms[i]: x_new[i] for i in range(n)}).evalf())

        # record
        history.append({
            'iteration': k,
            'x': x_new.copy(),
            'gradient': grad_k.copy(),
            'direction': d_k.copy(),
            'step': l_star,
            'f_value': f_new
        })
        trajectory.append(x_new.copy())

        # print details
        print(f"\nSteepest Descent Iter {k}")
        print("================================")
        print(f"  x{k}            = {x_k.tolist()}")
        print(f"  ∇f(x{k})        = {grad_k.tolist()}")
        print(f"  d{k}            = {d_k.tolist()}")
        print(f"  step size ℓ*    = {l_star:.7f}")
        print(f"  x{k+1}          = {x_new.tolist()}")
        print(f"  f(x{k+1})       = {f_new:.7f}")
        print("================================")

        x_k = x_new

    trajectory = np.vstack(trajectory)

    # optional plot (only for 2D)
    if plot and n == 2:
        # grid for contour
        vals = np.linspace(np.min(trajectory)-1, np.max(trajectory)+1, 200)
        X, Y = np.meshgrid(vals, vals)
        Z = f_num(X, Y)
        plt.contour(X, Y, Z, levels=80, cmap='viridis')
        plt.plot(trajectory[:,0], trajectory[:,1], 'o-', label='Descent path', color='red')
        plt.title("Steepest Descent on " + f_str)
        plt.xlabel(str(syms[0]))
        plt.ylabel(str(syms[1]))
        plt.legend()
        plt.grid(True)
        plt.show()

    return trajectory, history


"""
# Example usage:
if __name__ == "__main__":
    traj, hist = steepest_descent(
        f_str="x0 - x1 + 2*x0**2 + 2*x0*x1 + x1**3",
        x0=[0.0, 1.0],
        num_iterations=3,
        plot=True
    )
    print("\nFinal trajectory:\n", traj)
    print("History:")
    for entry in hist:
        print(entry)"""
