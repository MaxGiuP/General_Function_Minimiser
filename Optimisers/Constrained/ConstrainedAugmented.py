import numpy as np
import sympy as sp
from scipy.optimize import minimize

def augmented(
    f_str,
    eq_strs=None,
    ineq_strs=None,
    lambda0=None,
    r0: float = 1.0,
    tau: float = 10.0,
    max_outer: int = 6,
    tol: float = 1e-6,
    initial_guess=None,
    method: str = 'BFGS'
):
    """
    Augmented Lagrangian (method of multipliers) for h_j(x)=0 only.
    Returns all console‐style logs as one string.
    """
    eq_strs = [s for s in (eq_strs or []) if s.strip()]
    ineq_strs = [s for s in (ineq_strs or []) if s.strip()]
    logs = []

    # 1) Parse
    f_expr   = sp.sympify(f_str)
    eq_exprs = [sp.sympify(s) for s in eq_strs]

    # 2) Detect variables dynamically
    vars_syms = sorted(
        f_expr.free_symbols
         .union(*(e.free_symbols for e in eq_exprs)),
        key=lambda s: s.name
    )
    n = len(vars_syms)
    if n == 0:
        raise ValueError("No decision vars found in your strings.")

    logs.append(f"Detected variables: {[str(v) for v in vars_syms]}\n")
    logs.append(f"Equality constraints: {eq_strs}\n\n")

    # 3) Lambdify
    f_num   = sp.lambdify(tuple(vars_syms),       f_expr,    'numpy')
    eq_funcs= [sp.lambdify(tuple(vars_syms), e,  'numpy') for e in eq_exprs]

    # 4) Init multipliers & R
    m = len(eq_funcs)
    if lambda0 is None:
        lam = np.zeros(m)
    else:
        lam = np.array(lambda0, float)
        if lam.size != m:
            raise ValueError("lambda0 length must match number of eqs")
    R = r0

    # 5) Initial x
    if initial_guess is None:
        xk = np.ones(n)
    else:
        xk = np.array(initial_guess, float)
        if xk.size != n:
            raise ValueError("initial_guess length mismatch")

    # 6) Outer loop
    for k in range(1, max_outer+1):
        logs.append(f"--- Outer iter {k}, R={R:.3g} ---\n")

        # build augmented Lagrangian A(x)
        def A(x):
            val = f_num(*x)
            for j, hj in enumerate(eq_funcs):
                hval = hj(*x)
                val += lam[j]*hval + 0.5*R*(hval**2)
            return val

        # unconstrained minimize A(x)
        res = minimize(A, xk, method=method)
        xk = res.x
        fx = f_num(*xk)

        # eval constraints
        hvals = np.array([hj(*xk) for hj in eq_funcs])

        logs.append(f" x = {dict(zip([str(v) for v in vars_syms], xk.tolist()))}\n")
        logs.append(f" f = {fx:.6f}\n")
        logs.append(f" h = {hvals.tolist()}\n")

        # check convergence
        if np.all(np.abs(hvals) < tol):
            logs.append("All |h_j| < tol; stopping early.\n\n")
            break

        # 7) Update multipliers & R
        lam = lam + R*hvals
        R   = R*tau
        logs.append(f" Updated λ = {lam.tolist()}\n\n")

    # 8) Final summary
    logs.append("=== Final solution ===\n")
    logs.append(f" x = {dict(zip([str(v) for v in vars_syms], xk.tolist()))}\n")
    logs.append(f" f = {fx:.6f}\n")
    logs.append(f" h = {hvals.tolist()}\n")
    return "".join(logs)

"""
# Example usage
if __name__ == "__main__":
    f_str    = "5/(x0*x1**2)"
    eq_strs  = ["x0**2 + x1**2 - 4"]
    print(augmented_lagrangian(
        f_str,
        eq_strs=eq_strs,
        r0=1.0,
        tau=10.0,
        max_outer=6,
        tol=1e-6,
        initial_guess=[1.0,1.0],
        method='BFGS'
    ))
"""