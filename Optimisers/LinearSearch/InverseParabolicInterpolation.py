import numpy as np
import matplotlib.pyplot
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sympy import sympify, lambdify, symbols

# Initial input points
x1, x2, x3 = 0, 1.0, 2.0
num_iterations = 2

x = symbols('x')
expr_str = "x**5 - 2*x**3 - 10*x + 5"
expr = sympify(expr_str)
f = lambdify(x, expr, modules=["numpy"])


#Plot
x_vals = np.linspace(0, 2.5, 400)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label="f(x)")
plt.title("Inverse Parabolic Interpolation")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.legend()
plt.show()




next_label = 4 #Defines the label for the output

for i in range(num_iterations):
    print(f"\n--- Iteration {i+1} ---")

    f1, f2, f3 = f(x1), f(x2), f(x3)

    print(f"Bracket points:")
    print(f"  x1 = {x1:.6f}, f1 = {f1:.6f}")
    print(f"  x2 = {x2:.6f}, f2 = {f2:.6f}")
    print(f"  x3 = {x3:.6f}, f3 = {f3:.6f}")

    numerator = (x2 - x1)**2 * (f2 - f3) - (x2 - x3)**2 * (f2 - f1)
    denominator = (x2 - x1) * (f2 - f3) - (x2 - x3) * (f2 - f1)

    if denominator == 0:
        print("Interpolation failed: denominator = 0.")
        break

    x_min = x2 - 0.5 * numerator / denominator
    f_min = f(x_min)

    print(f"\nComputed new point:")
    print(f"  x{next_label} = {x_min:.6f}, f{next_label} = {f_min:.6f}")

    points = sorted([(x1, f1), (x2, f2), (x3, f3), (x_min, f_min)], key=lambda p: p[1])[:3]
    points.sort()
    x1, x2, x3 = points[0][0], points[1][0], points[2][0]

    print(f"\nUpdated bracket for next iteration:")
    print(f"  x1 = {x1:.6f}, x2 = {x2:.6f}, x3 = {x3:.6f}")
    print(f"------------------------------")

    next_label += 1
