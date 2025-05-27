import sympy as sp
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def manufacturing(f_str, x_min, x_max, h, plot=False):
    x_min = float(x_min)
    x_max = float(x_max)
    h     = float(h)

    x = sp.symbols('x', real=True)
    f_expr = sp.sympify(f_str, locals={'x': x})

    df = sp.diff(f_expr, x)
    crits = sp.solve(df, x)
    x_nom = float(next(c for c in crits if c.is_real and x_min < c < x_max))
    f_nom = float(f_expr.subs(x, x_nom))

    u = sp.symbols('u', real=True)
    f_noisy     = f_expr.subs(x, x + u)
    mean_f_expr = (1/(2*h)) * sp.integrate(f_noisy, (u, -h, h))
    mean_f_expr = sp.simplify(mean_f_expr)

    dmean  = sp.diff(mean_f_expr, x)
    crits2 = sp.solve(dmean, x)
    valid  = [float(c) for c in crits2
              if c.is_real and (x_min + h) <= c <= (x_max - h)]
    if not valid:
        raise RuntimeError("No robust minimizer in the valid domain.")
    x_rob = valid[0]
    f_rob = float(mean_f_expr.subs(x, x_rob))

    pct_drop = 100*(f_rob - f_nom)/f_nom

    lines = []
    lines.append("Nominal optimum:\n")
    lines.append(f"  x*        = {x_nom:.6f}\n")
    lines.append(f"  f(x*)     = {f_nom:.6f}\n\n")
    lines.append("Noise-robust optimum:\n")
    lines.append(f"  x_rob     = {x_rob:.6f}\n")
    lines.append(f"  E[f(x+u)] = {f_rob:.6f}\n\n")
    lines.append(f"Performance deterioration: {pct_drop:.2f}%\n")
    result = "".join(lines)

    if plot:
        xs      = np.linspace(x_min+h, x_max-h, 400)
        f_num   = sp.lambdify(x, f_expr,     'numpy')
        mean_num= sp.lambdify(x, mean_f_expr,'numpy')
        plt.plot(xs, f_num(xs),     label='f(x)')
        plt.plot(xs, mean_num(xs),  label='E[f(x+u)]')
        plt.axvline(x_nom, color='C0', ls='--', label='x*')
        plt.axvline(x_rob, color='C1', ls='--', label='x_rob')
        plt.xlabel('x')
        plt.ylabel('performance')
        plt.legend()
        plt.grid(True)
        plt.show()

    return result


"""
# Example usage:
if __name__ == "__main__":
    out = manufacturing(
        f_str="x + 1.78/x",
        x_min=0.75,
        x_max=2.0,
        h=0.25,
        plot=False
    )
    print(out)
"""
