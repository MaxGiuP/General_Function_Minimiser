import sympy as sp
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def steepest_descent(f_str, start, num_iterations=1, plot=False):
    f_expr = sp.sympify(f_str)
    syms = sorted(f_expr.free_symbols, key=lambda s: s.name)
    n = len(syms)
    if n < 1:
        raise ValueError("No variables found in the function string.")
    grad_expr = [sp.diff(f_expr, v) for v in syms]
    f_num = sp.lambdify(tuple(syms), f_expr, 'numpy')
    grad_num = sp.lambdify(tuple(syms), grad_expr, 'numpy')
    l = sp.Symbol('l')

    if plot and n == 2:
        a = np.array(start, float)
        mins, maxs = a.min() - 1, a.max() + 1
        xs = np.linspace(mins, maxs, 400)
        Y = f_num(xs, xs) if n == 2 else f_num(xs)
        plt.contour(*np.meshgrid(xs, xs), Y, levels=80, cmap='viridis')
        plt.title("Steepest Descent on " + f_str)
        plt.grid(True); plt.show()

    logs = []
    x_k = np.array(start, dtype=float)

    for k in range(1, num_iterations + 1):
        grad_k = np.array(grad_num(*x_k), dtype=float).flatten()
        d_k = -grad_k

        subs = {syms[i]: x_k[i] + l*d_k[i] for i in range(n)}
        phi = f_expr.subs(subs)
        dphi = sp.diff(phi, l)
        sols = sp.solve(dphi, l)
        real_ls = [float(sol.evalf()) for sol in sols if sol.is_real]
        if not real_ls:
            logs.append(f"Iteration {k}: no real step length found—stopping.\n")
            break
        l_star = real_ls[0]

        x_new = x_k + l_star * d_k
        f_new = float(f_expr.subs({syms[i]: x_new[i] for i in range(n)}).evalf())

        logs.append(f"\nSteepest Descent Iter {k}\n")
        logs.append("================================\n")
        logs.append(f"  x{k}          = {x_k.tolist()}\n")
        logs.append(f"  ∇f(x{k})      = {grad_k.tolist()}\n")
        logs.append(f"  d{k}          = {d_k.tolist()}\n")
        logs.append(f"  step size ℓ*  = {l_star:.7f}\n")
        logs.append(f"  x{k+1}        = {x_new.tolist()}\n")
        logs.append(f"  f(x{k+1})     = {f_new:.7f}\n")
        logs.append("================================\n")

        x_k = x_new

    result = "".join(logs)
    return result


"""
# Example usage:
if __name__ == "__main__":
    output = steepest_descent(
        f_str="x0 - x1 + 2*x0**2 + 2*x0*x1 + x1**3",
        start=[0.0, 1.0],
        num_iterations=3,
        plot=False
    )
    print(output)
"""