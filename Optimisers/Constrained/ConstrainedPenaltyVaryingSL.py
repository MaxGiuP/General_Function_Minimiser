import numpy as np
import sympy as sp
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

    eq_strs   = [s for s in (eq_strs or [])   if s.strip()]
    ineq_strs = [s for s in (ineq_strs or []) if s.strip()]
    logs = []

    f_expr    = sp.sympify(f_str)
    eq_exprs  = [sp.sympify(s) for s in eq_strs]
    ineq_exprs= [sp.sympify(s) for s in ineq_strs]

    vars_syms = sorted(
        f_expr.free_symbols
         .union(*(e.free_symbols for e in eq_exprs))
         .union(*(h.free_symbols for h in ineq_exprs)),
        key=lambda s: s.name
    )
    n = len(vars_syms)
    if n < 1:
        raise ValueError("No decision variables detected.")

    f_num    = sp.lambdify(tuple(vars_syms),            f_expr,    'numpy')
    eq_funcs = [sp.lambdify(tuple(vars_syms), e,       'numpy') for e in eq_exprs]
    ineq_funcs= [sp.lambdify(tuple(vars_syms), h,      'numpy') for h in ineq_exprs]

    x0 = np.ones(n) if initial_guess is None else np.array(initial_guess, dtype=float)
    logs.append(f"Initial guess: {dict(zip([str(v) for v in vars_syms], x0.tolist()))}\n\n")

    R = R0
    for k in range(1, max_round+1):
        R = R0 * (scale**(k-1))
        logs.append(f"Round {k}, R = {R:.4g}\n")

        def F(x):
            val = f_num(*x)
            for ef in eq_funcs:
                v = ef(*x)
                val += R * (v**2)
            for hf in ineq_funcs:
                v = hf(*x)
                if v < 0:
                    val += R * ((-v)**2)
            return val

        res = minimize(F, x0, method=method)
        x0 = res.x
        eq_viol = np.array([abs(ef(*x0)) for ef in eq_funcs])
        ineq_vals= np.array([hf(*x0)        for hf in ineq_funcs])

        sol_repr = dict(zip([str(v) for v in vars_syms], x0.tolist()))
        logs.append(f"  Solution: {sol_repr}\n")
        logs.append(f"  f     = {f_num(*x0):.6f}\n")
        logs.append(f"  |eq|  = {eq_viol.tolist()}\n")
        logs.append(f"  ineq. = {ineq_vals.tolist()}\n\n")

        if np.all(eq_viol < tol) and np.all(ineq_vals >= -tol):
            logs.append("Constraints satisfied—stopping early.\n")
            break

    logs.append("Final result:\n")
    logs.append(f"  R_final = {R:.6g}\n")
    sol_repr = dict(zip([str(v) for v in vars_syms], x0.tolist()))
    logs.append(f"  x       = {sol_repr}\n")
    logs.append(f"  f*      = {f_num(*x0):.6f}\n")

    return "".join(logs)


"""
# Example usage
if __name__ == "__main__":
    f_str    = "x0**2 + x1**2"
    eq_strs  = ["x0 + x1 - 1"]
    ineq_strs= ["x0 - 0.2"]
    print(varying_sl(
        f_str,
        eq_strs=eq_strs,
        ineq_strs=ineq_strs,
        R0=1e2,
        scale=10,
        max_round=4,
        initial_guess=[0.5,0.5],
        method='BFGS'
    ))
"""