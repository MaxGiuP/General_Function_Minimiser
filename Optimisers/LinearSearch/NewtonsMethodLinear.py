import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

formula_str = "-x**5 + 2*x**4 - x**2 - 5"

x = sp.symbols('x')

f_expr = sp.sympify(formula_str, {"x": x})

df_expr  = sp.diff(f_expr, x)
ddf_expr = sp.diff(df_expr, x)

f   = sp.lambdify(x, f_expr,  modules="numpy")
df  = sp.lambdify(x, df_expr, modules="numpy")
ddf = sp.lambdify(x, ddf_expr,modules="numpy")

#Plot f(x)
x_vals = np.linspace(-1, 2, 400)
plt.plot(x_vals, f_num(x_vals), label="f(x)")
plt.title("Newton's Method")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.legend()
plt.show()



for i in range(1, num_iterations+2):
    fx   = f_num(current_x)
    dfx  = df_num(current_x)
    ddfx = ddf_num(current_x)

    if ddfx == 0:
        print(f"Iteration {i - 1}: second derivative zero at x = {current_x:.6f}. Stopping.")
        break

    if i > 1:
        print(f"Iteration {i - 1}: x = {current_x:.6f},  f(x) = {fx:.6f}")

    current_x = current_x - dfx / ddfx

fx = f_num(current_x)
print(f"After {i - 1} iterations: x = {current_x:.6f},  f(x) = {fx:.6f}")
