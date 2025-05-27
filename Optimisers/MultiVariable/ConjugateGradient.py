import numpy as np
import sympy as sp
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def conjugate_gradient(f_str, start, num_iterations=1, plot=False):
    f_expr = sp.sympify(f_str)
    syms = sorted(f_expr.free_symbols, key=lambda s: s.name)
    n = len(syms)
    if n != len(start):
        raise ValueError(f"Got {n} symbols {syms} but start vector has length {len(start)}")
    l = sp.Symbol('l')

    f_num    = sp.lambdify(tuple(syms),        f_expr,    'numpy')
    grad_exprs = [sp.diff(f_expr, s) for s in syms]
    grad_num = sp.lambdify(tuple(syms), grad_exprs, 'numpy')

    logs = []
    x_k = np.array(start, dtype=float)

    g_prev = np.array(grad_num(*x_k), dtype=float).flatten()
    p = -g_prev

    for k in range(1, num_iterations+1):
        subs = {syms[i]: x_k[i] + l*p[i] for i in range(n)}
        phi = f_expr.subs(subs)
        dphi = sp.diff(phi, l)
        sols = sp.solve(dphi, l)
        real_ls = [float(sol) for sol in sols if sol.is_real]
        if not real_ls:
            logs.append(f"Iteration {k}: no real step length found—stopping.\n")
            break
        alpha = real_ls[0]

        x_k = x_k + alpha * p
        f_val = float(f_expr.subs({syms[i]: x_k[i] for i in range(n)}).evalf())

        logs.append(f"\nConjugate‐Gradient Iter {k}\n")
        logs.append("-"*30 + "\n")
        logs.append(f"  alpha_{k}  = {alpha:.8f}\n")
        logs.append(f"  x          = {x_k.tolist()}\n")
        logs.append(f"  f(x)       = {f_val:.8f}\n")

        g = np.array(grad_num(*x_k), dtype=float).flatten()
        beta = (g.dot(g)) / (g_prev.dot(g_prev))
        p = -g + beta * p
        g_prev = g.copy()

    if plot and n == 2:
        mins = x_k.min() - 1
        maxs = x_k.max() + 1
        xs = np.linspace(mins, maxs, 200)
        X, Y = np.meshgrid(xs, xs)
        Z = f_num(X, Y)
        plt.contour(X, Y, Z, levels=40, cmap='viridis')

        plt.plot(x_k[0], x_k[1], 'ro', label='Final')
        plt.title("Conjugate Gradient on " + f_str)
        plt.xlabel(str(syms[0])); plt.ylabel(str(syms[1]))
        plt.legend(); plt.grid(True); plt.show()

    result = "".join(logs)
    return result

"""
# Example usage:
if __name__ == "__main__":
    # uses variables x2 and x3 instead of x0,x1
    log_output = conjugate_gradient(
        f_str="x2**2 + x3**2 + 2*x2*x3",
        start=[1.0, -1.0],
        num_iterations=4,
        plot=False
    )
    print(log_output)
"""