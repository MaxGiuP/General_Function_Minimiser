import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import sympy as sp

def golden_section_search(f_str, x1, x2, x3, num_iterations=1, plot=False):
    # Create symbol and function
    f_expr = sp.sympify(f_str)
    syms = list(f_expr.free_symbols)
    if len(syms) != 1:
        raise ValueError(f"Expected exactly one variable in {f_str}, got {syms}")
    var = syms[0]

    # Numeric function
    f = sp.lambdify(var, f_expr, modules=['numpy'])

    # Optional plot
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

    # Golden ratio
    phi = (1 + np.sqrt(5)) / 2
    resphi = 2 - phi

    results = []
    a, b, c = x1, x2, x3
    for i in range(1, num_iterations + 1):
        x_new = b + resphi * (c - b)
        f_new = f(x_new)
        results.append((i, x_new, f_new, b, c))

        print(f"Iteration {i}:")
        print(f"  {var} = {x_new:.6f}, f({var}) = {f_new:.6f}")
        a, b, c = b, x_new, c
        print(f"  New interval: [{b:.6f}, {c:.6f}]\n")

    return results