import sympy as sp
import numpy as np

def manufacturing(f_str, x_min, x_max, h, plot=False):
    # 1) Symbolic set-up
    x = sp.symbols('x', real=True)
    f_expr = sp.sympify(f_str, locals={'x': x})
    
    # 2) Nominal minimizer: solve f'(x)=0 in (x_min, x_max)
    df = sp.diff(f_expr, x)
    crits = sp.solve(df, x)
    # pick the real root in the open interval
    x_nom = float(next(c for c in crits if c.is_real and x_min < c < x_max))
    f_nom = float(f_expr.subs(x, x_nom))
    
    # 3) Mean performance under uniform noise:
    u = sp.symbols('u', real=True)
    f_noisy = f_expr.subs(x, x + u)
    mean_f_expr = (1/(2*h)) * sp.integrate(f_noisy, (u, -h, h))
    # simplify a bit
    mean_f_expr = sp.simplify(mean_f_expr)
    
    # 4) Robust minimizer: solve d(mean_f)/dx = 0, subject to x∈[x_min+h, x_max-h]
    dmean = sp.diff(mean_f_expr, x)
    crits2 = sp.solve(dmean, x)
    valid = [
        float(c) for c in crits2
        if c.is_real and (x_min + h) <= c <= (x_max - h)
    ]
    if not valid:
        raise RuntimeError("No robust minimizer in the valid domain.")
    x_rob = valid[0]
    f_rob = float(mean_f_expr.subs(x, x_rob))
    
    # 5) Percentage deterioration
    pct_drop = 100*(f_rob - f_nom)/f_nom
    
    # 6) Optional plotting
    if plot:
        import numpy as np, matplotlib.pyplot as plt
        xs = np.linspace(x_min+h, x_max-h, 400)
        f_num    = sp.lambdify(x, f_expr,    'numpy')
        mean_num = sp.lambdify(x, mean_f_expr,'numpy')
        plt.plot(xs, f_num(xs),    label='f(x)')
        plt.plot(xs, mean_num(xs), label='E[f(x+u)]')
        plt.axvline(x_nom, color='C0', linestyle='--', label='x_nom')
        plt.axvline(x_rob, color='C1', linestyle='--', label='x_rob')
        plt.xlabel('x')
        plt.ylabel('performance')
        plt.legend()
        plt.grid(True)
        plt.show()
    
    return {
        'nominal': {
            'x': x_nom,
            'f': f_nom
        },
        'robust': {
            'x': x_rob,
            'mean_f': f_rob
        },
        'deterioration_pct': pct_drop
    }

"""
# Example usage:
if __name__ == "__main__":
    res = robust_performance_setting(
        f_str="x + 1.78/x",
        x_min=0.75,
        x_max=2.0,
        h=0.25,
        plot=True
    )
    print("Nominal optimum:")
    print(f" x* = {res['nominal']['x']:.6f}, f = {res['nominal']['f']:.6f}")
    print("\nNoise‐robust optimum:")
    print(f" x   = {res['robust']['x']:.6f}, E[f] = {res['robust']['mean_f']:.6f}")
    print(f"\nPerformance deterioration: {res['deterioration_pct']:.2f}%")
"""
