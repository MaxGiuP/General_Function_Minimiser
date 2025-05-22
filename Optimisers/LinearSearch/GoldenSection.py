import numpy as np
import matplotlib.pyplot
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sympy import sympify, lambdify, symbols

x = symbols('x')


expr_str = "x**5 - 2*x**3 - 10*x + 5"  # You can replace this with input() or GUI input
x1, x2, x3 = 0.5, 1.0, 2.0
num_iterations = 2


expr = sympify(expr_str)

# === Step 2: Convert symbolic expression to numeric function ===
f = lambdify(x, expr, modules=["numpy"])

x_vals = np.linspace(0, 2.5, 400)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label="f(x)")
plt.title("Golden Section Plot")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.legend()
plt.show()

phi = (1 + np.sqrt(5)) / 2
resphi = 2 - phi  # ≈ 0.381966
resphi = 0.382 #BECAUSE QUESTION SAID SO



for i in range(num_iterations):
    x_new = x2 + resphi * (x3 - x2)
    f_new = f(x_new)

    print(f"Iteration {i+1}:")
    print(f"  x{i+4} = {x_new:.6f}, f{i+4} = {f_new:.6f}")

    # Shift interval: x1 <- x2, x2 <- x_new, x3 stays the same
    x1, x2, x3 = x2, x_new, x3

    print(f"  New interval: [{x2:.6f}, {x3:.6f}]\n")