import sympy as sp
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def varying_sl(
    f_str,
    eq_strs=None,
    ineq_strs=None,
    R0=1.0,
    scale=10.0,
    max_round=6,
    tol=1e-6,
    initial_guess=None,
    method='BFGS',
    plot=False
):
    eq_strs = eq_strs or []
    ineq_strs  = ineq_strs  or []

    # 1) symbolic parse
    f_expr  = sp.sympify(f_str)
    eq_expr = [sp.sympify(s) for s in eq_strs]
    ineq_expr  = [sp.sympify(s) for s in ineq_strs]

    # 2) detect variables
    vars_syms = sorted(
        f_expr.free_symbols
         .union(*(e.free_symbols for e in eq_expr))
         .union(*(h.free_symbols for h in ineq_expr)),
        key=lambda s: s.name
    )
    n = len(vars_syms)
    if n < 1:
        raise ValueError("No decision variables detected.")

    # 3) lambdify
    f_num    = sp.lambdify(vars_syms,             f_expr,    'numpy')
    eq_num   = [sp.lambdify(vars_syms, e,         'numpy') for e in eq_expr]
    ineq_expr    = [sp.lambdify(vars_syms, h,         'numpy') for h in ineq_expr]

    # 4) initial guess
    if initial_guess is None:
        x0 = np.ones(n)
    else:
        x0 = np.array(initial_guess, dtype=float)

    # 5) outer loop
    R = R0
    for round_idx in range(max_round):
        R = R0 * (scale**round_idx)

        def F(x):
            val = f_num(*x)
            # equality penalties: R·(h_i(x))²
            for eq in eq_num:
                v = eq(*x)
                val += R * (v**2)
            # inequality penalties: R·max(0, -g_j(x))²
            for hfun in ineq_expr:
                v = hfun(*x)
                if v < 0:
                    val += R * ((-v)**2)
            return val

        res = minimize(F, x0, method=method)
        x0 = res.x  # warm start

        # check constraints
        eq_viol = np.array([abs(eq(*x0)) for eq in eq_num])
        h_vals  = np.array([h(*x0)       for h in ineq_expr])
        if np.all(eq_viol < tol) and np.all(h_vals >= -tol):
            break

    # 6) package results
    sol_dict = {str(v): x0[i] for i, v in enumerate(vars_syms)}
    sol_dict['f*']     = float(f_num(*x0))
    sol_dict['R_final'] = R
    residuals = {'eq_viol': eq_viol, 'h_vals': h_vals}

    # 7) optional 2D plot
    if plot and n == 2:
        x_sym, y_sym = vars_syms
        xs = np.linspace(x0[0]-1, x0[0]+1, 200)
        ys = np.linspace(x0[1]-1, x0[1]+1, 200)
        X, Y = np.meshgrid(xs, ys)
        Z = f_num(X, Y)
        plt.contour(X, Y, Z, levels=50, cmap='viridis')
        plt.plot(x0[0], x0[1], 'ro', label='Solution')
        plt.title("Penalty Schedule Solution")
        plt.xlabel(str(x_sym)); plt.ylabel(str(y_sym))
        plt.legend(); plt.grid(True); plt.show()

    return sol_dict, residuals
