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

    results = []
    next_label = 4

    for i in range(1, num_iterations + 1):
        print(f"\n--------- Iteration {i} ---------")
        # current evaluations
        f1, f2, f3 = f(x1), f(x2), f(x3)
        print(f"Bracket points:")
        print(f"  Lower = {x1:.6f}, f = {f1:.6f}")
        print(f"  Middle = {x2:.6f}, f = {f2:.6f}")
        print(f"  Upper = {x3:.6f}, f = {f3:.6f}")

        # compute new estimate
        num = (x2 - x1)**2 * (f2 - f3) - (x2 - x3)**2 * (f2 - f1)
        den = (x2 - x1) * (f2 - f3)   - (x2 - x3) * (f2 - f1)
        if den == 0:
            print("Interpolation failed: denominator = 0.")
            break

        x_min = x2 - 0.5 * num / den
        f_min = f(x_min)
        print(f"\nComputed new point:")
        print(f"  x{next_label} = {x_min:.6f}, f = {f_min:.6f}")

        # store results
        results.append((i, next_label, x_min, f_min, (x1, x2, x3)))

        # pick the best three of {x1,x2,x3,x_min} by f-value
        pts = sorted(
            [(x1, f1), (x2, f2), (x3, f3), (x_min, f_min)],
            key=lambda p: p[1]
        )[:3]
        # sort by x to keep bracket order
        pts.sort(key=lambda p: p[0])
        x1, x2, x3 = pts[0][0], pts[1][0], pts[2][0]

        print(f"\nUpdated bracket:")
        print(f"  Lower = {x1:.6f}, Middle = {x2:.6f}, Upper = {x3:.6f}")
        print(f"------------------------------")

        next_label += 1

    return results