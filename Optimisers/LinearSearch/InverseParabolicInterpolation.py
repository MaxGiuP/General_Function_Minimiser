import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import sympy as sp

def inverse_parabolic_interpolation(f_str, x1, x2, x3, num_iterations=1, plot=False):
    # Parse and detect variable
    f_expr = sp.sympify(f_str)
    syms = list(f_expr.free_symbols)
    if len(syms) != 1:
        raise ValueError(f"Expected exactly one variable in '{f_str}', found {syms}")
    var = syms[0]

    # Numeric function
    f = sp.lambdify(var, f_expr, modules=['numpy'])

    # Optional plot
    if plot:
        a, c = min(x1, x3), max(x1, x3)
        xs = np.linspace(a, c, 400)
        ys = f(xs)
        plt.plot(xs, ys, label=f_str)
        plt.title("Inverse Parabolic Interpolation")
        plt.xlabel(str(var))
        plt.ylabel(f_str)
        plt.grid(True)
        plt.axhline(0, color='black', linewidth=0.5)
        plt.legend()
        plt.show()

    logs = []
    next_label = 4

    for i in range(1, num_iterations + 1):
        logs.append(f"\n--------- Iteration {i} ---------\n")

        # current evaluations
        f1, f2, f3 = f(x1), f(x2), f(x3)
        logs.append("Bracket points:\n")
        logs.append(f"  Lower  = {x1:.6f}, f = {f1:.6f}\n")
        logs.append(f"  Middle = {x2:.6f}, f = {f2:.6f}\n")
        logs.append(f"  Upper  = {x3:.6f}, f = {f3:.6f}\n")

        # compute new estimate
        num = (x2 - x1)**2 * (f2 - f3) - (x2 - x3)**2 * (f2 - f1)
        den = (x2 - x1) * (f2 - f3)   - (x2 - x3) * (f2 - f1)
        if den == 0:
            logs.append("Interpolation failed: denominator = 0.\n")
            break

        x_min = x2 - 0.5 * num / den
        f_min = f(x_min)
        logs.append("\nComputed new point:\n")
        logs.append(f"  x{next_label} = {x_min:.6f}, f = {f_min:.6f}\n")

        # pick the best three of {x1,x2,x3,x_min} by f-value
        pts = sorted(
            [(x1, f1), (x2, f2), (x3, f3), (x_min, f_min)],
            key=lambda p: p[1]
        )[:3]
        # sort by x to keep bracket order
        pts.sort(key=lambda p: p[0])
        x1, x2, x3 = pts[0][0], pts[1][0], pts[2][0]

        logs.append(f"\nUpdated bracket:\n")
        logs.append(f"  Lower  = {x1:.6f}, Middle = {x2:.6f}, Upper = {x3:.6f}\n")
        logs.append("------------------------------\n")

        next_label += 1

    result = "".join(logs)
    return result