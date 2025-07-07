import sympy as sp
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def newtons_method(f_str, current_x, num_iterations=1, plot=False):
    f_expr = sp.sympify(f_str)
    syms = list(f_expr.free_symbols)
    if len(syms) != 1:
        raise ValueError(f"Expected exactly one variable in '{f_str}', found {syms}")
    var = syms[0]

    df_expr  = sp.diff(f_expr, var)
    ddf_expr = sp.diff(df_expr, var)

    f_num   = sp.lambdify(var, f_expr,  'numpy')
    df_num  = sp.lambdify(var, df_expr, 'numpy')
    ddf_num = sp.lambdify(var, ddf_expr,'numpy')

    logs = []
    x_val = current_x

    for i in range(1, num_iterations + 1):
        f_val   = f_num(x_val)
        df_val  = df_num(x_val)
        ddf_val = ddf_num(x_val)

        if ddf_val == 0:
            logs.append(f"Iteration {i}: second derivative zero at {var} = {x_val:.6f}. Stopping.\n")
            break

        x_val = x_val - df_val / ddf_val
        f_val = f_num(x_val)

        logs.append(f"Iteration {i}: {var}{i+1} = {x_val:.6f}, f({var}{i+1}) = {f_val:.6f}\n")

    if plot:

        width = (current_x * 0.5) if current_x != 0 else 1.0
        a = current_x - width
        b = current_x + width
        xs = np.linspace(a, b, 400)
        ys = f_num(xs)

        plt.figure(figsize=(6,4))
        plt.plot(xs, ys, label=f_str)
        plt.scatter([x_val], [f_num(x_val)], color='red', zorder=5,
                    label=f'Final x = {x_val:.4f}')
        plt.title("Newton's Method")
        plt.xlabel(str(var))
        plt.ylabel(f_str)
        plt.grid(True)
        plt.legend()
        plt.show()

    result = "".join(logs)
    return result
