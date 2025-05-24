import numpy as np
import sympy as sp
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def bfgs(f_str, initial_guess, num_iterations=1, plot=False):
    """
    Perform BFGS quasi‐Newton optimization, capturing all console output
    into a returned string instead of printing. Automatically detects
    whichever variables (e.g. x0,x1 or x2,x3) appear in f_str.
    """
    # 1) Parse and detect symbols
    f_expr = sp.sympify(f_str)
    syms = sorted(f_expr.free_symbols, key=lambda s: s.name)
    n = len(syms)
    if n != len(initial_guess):
        raise ValueError(f"Detected symbols {syms} but initial_guess has length {len(initial_guess)}")
    
    # 2) Lambdify objective and gradient
    f_num    = sp.lambdify(tuple(syms),             f_expr,    'numpy')
    grad_syms= [sp.diff(f_expr, v) for v in syms]
    grad_num = sp.lambdify(tuple(syms), grad_syms,   'numpy')

    # 3) BFGS setup
    Hk = np.eye(n)
    alpha_init, rho, c1 = 1.0, 0.8, 1e-4

    def line_search(xk, pk, gk):
        alpha = alpha_init
        fk = f_num(*xk)
        while True:
            x_new = xk + alpha*pk
            if f_num(*x_new) <= fk + c1*alpha*np.dot(gk, pk):
                return alpha
            alpha *= rho

    # 4) Iteration
    xk = np.array(initial_guess, dtype=float)
    trajectory = [xk.copy()]
    logs = []

    for k in range(1, num_iterations+1):
        gk = np.array(grad_num(*xk), dtype=float).flatten()
        pk = -Hk.dot(gk)

        alpha = line_search(xk, pk, gk)
        sk = alpha * pk
        x_new = xk + sk
        fk_old = float(f_num(*xk))
        fk_new = float(f_num(*x_new))

        # 5) Log details
        logs.append(f"\nIteration {k}\n")
        logs.append("--------------\n")
        logs.append(f"Variables       = {syms}\n")
        logs.append(f"x[{k-1}]         = {xk.tolist()}\n")
        logs.append(f"f(x[{k-1}])      = {fk_old:.6f}\n")
        logs.append(f"∇f(x[{k-1}])     = {gk.tolist()}\n")
        logs.append(f"Direction p     = {pk.tolist()}\n")
        logs.append(f"Step α          = {alpha:.6f}\n")
        logs.append(f"x[{k}]           = {x_new.tolist()}\n")
        logs.append(f"f(x[{k}])        = {fk_new:.6f}\n")
        logs.append("--------------\n")

        # 6) Update Hessian approx
        g_new = np.array(grad_num(*x_new), dtype=float).flatten()
        yk = g_new - gk
        syk = float(np.dot(yk, sk))
        if syk > 1e-12:
            rho_k = 1.0 / syk
            I = np.eye(n)
            Vk = I - rho_k * np.outer(sk, yk)
            Hk = Vk @ Hk @ Vk.T + rho_k * np.outer(sk, sk)

        xk = x_new
        trajectory.append(xk.copy())

    # 7) Optional plot if exactly 2 variables
    if plot and n == 2:
        xs = np.linspace(trajectory[0][0]-1, trajectory[-1][0]+1, 200)
        ys = np.linspace(trajectory[0][1]-1, trajectory[-1][1]+1, 200)
        X, Y = np.meshgrid(xs, ys)
        Z = f_num(X, Y)
        plt.contour(X, Y, Z, levels=50, cmap='viridis')
        traj = np.vstack(trajectory)
        plt.plot(traj[:,0], traj[:,1], 'o-', color='red', label='BFGS path')
        plt.title("BFGS Optimization Path on " + f_str)
        plt.xlabel(str(syms[0]))
        plt.ylabel(str(syms[1]))
        plt.grid(True)
        plt.axis('equal')
        plt.legend()
        plt.show()

    # 8) Return all logs as a single string
    return "".join(logs)

"""
# Example usage:
if __name__ == "__main__":
    log_output = bfgs(
        f_str="x2**2 + 3*x2*x3 + x3**2",
        initial_guess=[1.0, -1.0],
        num_iterations=3,
        plot=False
    )
    print(log_output)
"""