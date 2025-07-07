import numpy as np
import sympy as sp
from scipy.optimize import minimize

def fixed_penalty(f_str, eq_strs=None, ineq_strs=None,
                  R=1e3, initial_guess=None, method='BFGS', plot=False):

    eq_strs   = [s for s in (eq_strs or [])   if s.strip()]
    ineq_strs = [s for s in (ineq_strs or []) if s.strip()]
    logs = []

    f_expr     = sp.sympify(f_str)
    eq_exprs   = [sp.sympify(s) for s in eq_strs]
    ineq_exprs = [sp.sympify(s) for s in ineq_strs]

    vars_syms = sorted(
        f_expr.free_symbols
         .union(*(e.free_symbols for e in eq_exprs))
         .union(*(h.free_symbols for h in ineq_exprs)),
        key=lambda s: s.name
    )
    n = len(vars_syms)

    f_num    = sp.lambdify(tuple(vars_syms),             f_expr,    'numpy')
    eq_funcs = [sp.lambdify(tuple(vars_syms), e,        'numpy') for e in eq_exprs]
    ineq_funcs = [sp.lambdify(tuple(vars_syms), h,       'numpy') for h in ineq_exprs]

    def F(x):
        val = f_num(*x)
        violated = (
            any(abs(ef(*x)) > 1e-8 for ef in eq_funcs)
            or any(hf(*x)   < 0   for hf in ineq_funcs)
        )
        if violated:
            val += R
        return val

    if initial_guess is None:
        x0 = np.ones(n)
    else:
        x0 = np.array(initial_guess, dtype=float)

    res = minimize(F, x0, method=method)

    res = minimize(F, x0, method=method)
    sol = res.x
    f_star = f_num(*sol)

    sol_dict = { str(v): sol[i] for i, v in enumerate(vars_syms) }
    sol_dict['f*'] = f_star

    broken_eq   = [s for s,ef in zip(eq_strs,   eq_funcs)   if abs(ef(*sol))>1e-8]
    broken_ineq = [s for s,hf in zip(ineq_strs, ineq_funcs) if hf(*sol)<0]

    logs.append("Optimal solution:\n")
    for v in vars_syms:
        logs.append(f"  {v} = {sol_dict[str(v)]:.6f}\n")
    logs.append(f"  f*  = {sol_dict['f*']:.6f}\n\n")

    if broken_eq or broken_ineq:
        logs.append("Broken constraints:\n")
        for s in broken_eq:
            logs.append(f"  equality:   {s} = 0\n")
        for s in broken_ineq:
            logs.append(f"  inequality: {s} >= 0\n")
    else:
        logs.append("No constraints broken.\n")

    return "".join(logs)


"""
# Example
if __name__ == "__main__":
    f_str     = "x**2 + y**2"
    eq_strs   = ["x + y - 1"]
    ineq_strs = ["x - 0.2", "y - 0.3"]
    initial   = [0.5, 0.5]

    print(fixed_penalty(
        f_str,
        eq_strs=eq_strs,
        ineq_strs=ineq_strs,
        R=1e3,
        initial_guess=initial,
        method='BFGS'
    ))
"""