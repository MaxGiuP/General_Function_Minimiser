import sympy as sp
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def fixed_penalty(f_str, eq_strs=None, ineq_strs=None, R=1e3, initial_guess=None, method='BFGS', plot=False):
    eq_strs   = eq_strs or []
    ineq_strs    = ineq_strs  or []
    # 1) parse
    f_expr = sp.sympify(f_str)
    eq_exprs = [sp.sympify(s) for s in eq_strs]
    ineq_exprs  = [sp.sympify(s) for s in ineq_strs]
    # 2) detect vars
    vars_syms = sorted(
        f_expr.free_symbols
         .union(*(e.free_symbols for e in eq_exprs))
         .union(*(h.free_symbols for h in ineq_exprs)),
        key=lambda s: s.name
    )
    n = len(vars_syms)
    # 3) lambdify
    f_num  = sp.lambdify(vars_syms, f_expr,  'numpy')
    eq_num = [sp.lambdify(vars_syms, e,      'numpy') for e in eq_exprs]
    ineq_num  = [sp.lambdify(vars_syms, h,      'numpy') for h in ineq_exprs]
    # 4) penalty objective
    def F(x):
        val = f_num(*x)
        for e in eq_num:
            if abs(e(*x)) > 1e-8:
                val += R
        for h in ineq_num:
            if h(*x) < 0:
                val += R
        return val
    # 5) initial guess
    if initial_guess is None:
        x0 = np.zeros(n)
    else:
        x0 = np.array(initial_guess, dtype=float)
    # 6) minimize
    res = minimize(F, x0, method=method)
    sol = res.x
    f_star = f_num(*sol)
    sol_dict = {str(v): sol[i] for i,v in enumerate(vars_syms)}
    sol_dict['f*'] = f_star
    # 7) broken constraints
    broken_eq  = [s for s,e in zip(eq_strs, eq_num) if abs(e(*sol))>1e-8]
    broken_ineq = [s for s,h in zip(ineq_strs, ineq_num) if h(*sol)<0]
    # 8) optional plot
    if plot and n==2:
        x_sym, y_sym = vars_syms
        # contour
        xs = np.linspace(sol[0]-1, sol[0]+1, 200)
        ys = np.linspace(sol[1]-1, sol[1]+1, 200)
        X,Y = np.meshgrid(xs, ys)
        Z = f_num(X,Y)
        plt.contour(X,Y,Z,levels=50,cmap='viridis')
        plt.plot(sol[0], sol[1], 'ro', label='Solution')
        plt.title("Penalty Method Solution")
        plt.xlabel(str(x_sym)); plt.ylabel(str(y_sym))
        plt.legend(); plt.grid(True); plt.show()
    return sol_dict, {'equalities': broken_eq, 'inequalities': broken_ineq}
