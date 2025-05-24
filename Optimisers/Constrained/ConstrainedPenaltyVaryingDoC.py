import sympy as sp
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def varying_doc(
    f_str,
    eq_strs=None,
    ineq_strs=None,
    R=1e3,
    initial_guess=None,
    method='BFGS',
    plot=False
):
    """
    Fixed‐penalty method for constrained optimization.

    Parameters:
        f_str (str): Objective as a string, e.g. "x**2+y**2+z**2".
        eq_strs (list of str): Equalities h(x)=0.
        ineq_strs (list of str): Inequalities g(x)>=0.
        R (float): Penalty multiplier.
        initial_guess (array‐like): Starting point; defaults to ones.
        method (str): SciPy minimize method.
        plot (bool): If True and n==2, show contour + solution.

    Returns:
        sol_dict (dict): Variable names → solution values, plus 'f*'.
        violations (dict): {'eq': [h_i(x)], 'ineq': [g_j(x)]}.
    """
    eq_strs = eq_strs or []
    ineq_strs  = ineq_strs  or []

    # 1) Parse
    f_expr  = sp.sympify(f_str)
    eq_expr = [sp.sympify(s) for s in eq_strs]
    ineq_expr  = [sp.sympify(s) for s in ineq_strs]

    # 2) Auto‐detect variables
    vars_syms = sorted(
        f_expr.free_symbols
         .union(*(e.free_symbols for e in eq_expr))
         .union(*(h.free_symbols for h in ineq_expr)),
        key=lambda s: s.name
    )
    n = len(vars_syms)
    if n == 0:
        raise ValueError("No decision variables found.")

    # 3) Lambdify
    f_num  = sp.lambdify(vars_syms,             f_expr,  'numpy')
    eq_num = [sp.lambdify(vars_syms, e,         'numpy') for e in eq_expr]
    h_num  = [sp.lambdify(vars_syms, h,         'numpy') for h in ineq_expr]

    # 4) Penalty objective
    def F(x):
        val = f_num(*x)
        for eqf in eq_num:
            v = eqf(*x)
            val += R * (v**2)
        for hf in h_num:
            v = hf(*x)
            if v < 0:
                val += R * ((-v)**2)
        return val

    # 5) Initial guess
    if initial_guess is None:
        x0 = np.ones(n)
    else:
        x0 = np.array(initial_guess, dtype=float)

    # 6) Unconstrained minimize
    res = minimize(F, x0, method=method)
    sol = res.x
    fstar = f_num(*sol)

    # 7) Gather violations
    eq_viol = [eqf(*sol) for eqf in eq_num]
    h_viol  = [hf(*sol) for hf in h_num]

    sol_dict = {str(v): sol[i] for i, v in enumerate(vars_syms)}
    sol_dict['f*'] = fstar
    violations = {'eq': eq_viol, 'ineq': h_viol}

    # 8) Optional 2D plot
    if plot and n == 2:
        x_sym, y_sym = vars_syms
        # build grid
        xs = np.linspace(sol[0]-1, sol[0]+1, 200)
        ys = np.linspace(sol[1]-1, sol[1]+1, 200)
        X, Y = np.meshgrid(xs, ys)
        Z = f_num(X, Y)
        plt.contour(X, Y, Z, levels=50, cmap='viridis')
        plt.plot(sol[0], sol[1], 'ro', label='Solution')
        plt.title("Fixed Penalty Solution")
        plt.xlabel(str(x_sym))
        plt.ylabel(str(y_sym))
        plt.legend()
        plt.grid(True)
        plt.show()

    return sol_dict, violations