import numpy as np
import sympy as sp
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def bfgs(f_str, initial_guess, num_iterations=1, plot=False):
    # Symbolic setup
    x0 = np.array(initial_guess, dtype=float)
    n = len(x0)
    x_syms = sp.symbols(f'x0:{n}')
    f_expr = sp.sympify(f_str)
    grad_syms = [sp.diff(f_expr, xi) for xi in x_syms]

    # Lambdify numeric functions
    f_num    = sp.lambdify(x_syms,              f_expr,    'numpy')
    grad_num = sp.lambdify(x_syms, grad_syms,   'numpy')

    # BFGS parameters
    Hk = np.eye(n)
    alpha_init = 1.0
    rho = 0.8
    c1  = 1e-4

    # Wolfe-backtracking line search
    def line_search(xk, pk, gk):
        alpha = alpha_init
        fk = f_num(*xk)
        while True:
            x_new = xk + alpha * pk
            if f_num(*x_new) <= fk + c1 * alpha * np.dot(gk, pk):
                return alpha
            alpha *= rho

    # Initialization
    xk = x0.copy()
    trajectory = [xk.copy()]
    history = []

    for k in range(1, num_iterations + 1):
        gk = np.array(grad_num(*xk), dtype=float).flatten()
        pk = -Hk.dot(gk)

        # line search
        alpha = line_search(xk, pk, gk)
        sk = alpha * pk
        x_new = xk + sk
        fk_old = float(f_num(*xk))
        fk_new = float(f_num(*x_new))

        # record
        history.append({
            'iteration':  k,
            'x_old':      xk.copy(),
            'f_old':      fk_old,
            'grad_old':   gk.copy(),
            'direction':  pk.copy(),
            'step':       alpha,
            'x_new':      x_new.copy(),
            'f_new':      fk_new
        })
        trajectory.append(x_new.copy())

        # update Hk
        g_new = np.array(grad_num(*x_new), dtype=float).flatten()
        yk = g_new - gk
        syk = np.dot(yk, sk)
        if syk > 1e-12:
            rho_k = 1.0 / syk
            I = np.eye(n)
            Vk = I - rho_k * np.outer(sk, yk)
            Hk = Vk @ Hk @ Vk.T + rho_k * np.outer(sk, sk)

        # advance
        xk = x_new

        # print
        print(f"\nIteration {k}")
        print("--------------")
        print(f"x[{k-1}]      = {history[-1]['x_old'].tolist()}")
        print(f"f(x[{k-1}])   = {fk_old:.6f}")
        print(f"∇f(x[{k-1}])  = {gk.tolist()}")
        print(f"Direction p   = {pk.tolist()}")
        print(f"Step α        = {alpha:.6f}")
        print(f"x[{k}]        = {x_new.tolist()}")
        print(f"f(x[{k}])     = {fk_new:.6f}")
        print("--------------")

    trajectory = np.vstack(trajectory)

    # Optional contour + path plot for 2D
    if plot and n == 2:
        # grid
        mins = trajectory.min(axis=0) - 1
        maxs = trajectory.max(axis=0) + 1
        xs = np.linspace(mins[0], maxs[0], 200)
        ys = np.linspace(mins[1], maxs[1], 200)
        X, Y = np.meshgrid(xs, ys)
        Z = f_num(X, Y)

        plt.contour(X, Y, Z, levels=50, cmap='viridis')
        traj = trajectory
        plt.plot(traj[:,0], traj[:,1], 'o-', color='red', label='BFGS path')
        plt.title("BFGS Optimization Path on " + f_str)
        plt.xlabel(str(x_syms[0]))
        plt.ylabel(str(x_syms[1]))
        plt.grid(True)
        plt.axis('equal')
        plt.legend()
        plt.show()

    return trajectory, history

"""
# Example usage:
if __name__ == "__main__":
    traj, hist = bfgs(
        f_str="x0**2 + 3*x1**2 - x0*x1 + 2*x0 - 4*x1 + 1",
        initial_guess=[0.5, -1.0],
        num_iterations=5,
        plot=True
    )
    print("\nFinal trajectory:\n", traj)
    print("History:")
    for entry in hist:
        print(entry)
"""