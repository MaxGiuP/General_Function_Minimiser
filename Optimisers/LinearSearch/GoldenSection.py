import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import sympy as sp

def golden_section_search(f_str, x1, x2, x3, num_iterations=1, plot=False):
    f_expr = sp.sympify(f_str)
    syms = list(f_expr.free_symbols)
    if len(syms) != 1:
        raise ValueError(f"Expected exactly one variable in {f_str}, got {syms}")
    var = syms[0]

    f = sp.lambdify(var, f_expr, modules=['numpy'])

    if plot:
        xs = np.linspace(x1, x3, 400)
        ys = f(xs)
        plt.plot(xs, ys, label=f_str)
        plt.title("Golden Section Search")
        plt.xlabel(str(var))
        plt.ylabel(f_str)
        plt.grid(True)
        plt.axhline(0, color='black', linewidth=0.5)
        plt.legend()
        plt.show()

    phi = (1 + np.sqrt(5)) / 2
    resphi = 2 - phi

    logs = []
    result = ""

    a, b, c = x1, x2, x3
    for i in range(1, num_iterations + 1):
        x_new = b + resphi * (c - b)
        f_new = f(x_new)
        a, b, c = b, x_new, c

        logs.append(f"Iteration {i}:\n")
        logs.append(f"  {var} = {x_new:.6f}, f({var}) = {f_new:.6f}\n")
        logs.append(f"  New interval: [{b:.6f}, {c:.6f}]\n\n")

        print(f"Iteration {i}:")
        print(f"  {var} = {x_new:.6f}, f({var}) = {f_new:.6f}")
        print(f"  New interval: [{b:.6f}, {c:.6f}]\n")

    results = "".join(logs)

    return results