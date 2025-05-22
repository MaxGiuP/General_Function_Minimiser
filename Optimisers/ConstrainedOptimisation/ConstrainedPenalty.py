"""
penalty_solve.py  –  minimal quadratic-penalty solver (≤ 3 variables)

Usage example
-------------
sol = penalty_solve(
        f_str   = "x**2 + y**2 + z**2",
        constr  = ["x*y - 1 = 0",
                   "2*y*z - 1 = 0",
                   "3*x*z - 1 >= 0",
                   "x >= 0", "y >= 0", "z >= 0"],
        x0      = [0.5, 1.0, 0.5]       # optional; defaults to 1s
      )
print(sol)            # {'x': 0.8165, 'y': 1.2254, 'z': 0.6127, 'f': 2.218, 'success': True}
"""

import sympy as sp
import numpy as np
from scipy.optimize import minimize

# ----------------------------------------------------------------------
def penalty_solve(f_str: str,
                  constr: list[str],
                  *,
                  x0: list[float] | None = None,
                  R: float = 1e3):
    """
    Quadratic-penalty method for    min f(x)  s.t.  g_j(x)=0 ,  h_k(x)>=0
    --------------------------------------------------------------------
    Parameters
    ----------
    f_str   : str        objective, using symbols x, y, z
    constr  : list[str]  each element:
                           • "expr = 0"   (equality)
                           • "left >= right"  or  "left <= right"
                           • "expr"       (interpreted as expr >= 0)
    x0      : list[float]  initial guess (length = # free variables)
    R       : float        penalty weight (default 1e3)
    Returns
    -------
    dict  { 'x': value, 'y': value, 'z': value, 'f': f(min), 'success': bool }
    """
    # 1. define the only symbols we ever allow
    x, y, z = sp.symbols('x y z', real=True)
    name2sym = {'x': x, 'y': y, 'z': z}

    # 2. objective
    f = sp.sympify(f_str, locals=name2sym)

    # 3. parse constraints -------------------------------------------------
    eqs, ineqs = [], []

    for raw in constr:
        s = raw.replace(" ", "")
        if ">=" in s:
            left, right = s.split(">=")
            expr = sp.sympify(f"({left})-({right})", locals=name2sym)   # >=0
            ineqs.append(expr)
        elif "<=" in s:
            left, right = s.split("<=")
            expr = sp.sympify(f"({right})-({left})", locals=name2sym)   # >=0
            ineqs.append(expr)
        elif "=" in s:
            left, right = s.split("=")
            expr = sp.sympify(f"({left})-({right})", locals=name2sym)   # ==0
            eqs.append(expr)
        else:                                   # plain "expr"  ->  expr >= 0
            expr = sp.sympify(s, locals=name2sym)
            ineqs.append(expr)

    # 4. penalty function  F = f + R*(Σeq^2 + Σmax(0,-ineq)^2)
    penalty_eq   = sum(g**2 for g in eqs)
    penalty_ineq = sum(sp.Piecewise((0, h >= 0), ((-h)**2, True))
                       for h in ineqs)

    F = f + R*(penalty_eq + penalty_ineq)

    # 5. decide which variables actually appear
    vars_used = sorted(
        list(f.free_symbols.union(*(e.free_symbols for e in eqs+ineqs))),
        key=lambda s: s.name)

    if not vars_used:
        raise ValueError("No variable x, y or z appears in the problem.")

    # 6. lambdify to fast NumPy code
    F_num = sp.lambdify(vars_used, F, 'numpy')

    # 7. initial guess
    if x0 is None:
        x0 = np.ones(len(vars_used))

    # 8. numerical optimisation
    obj = lambda v: F_num(*v)
    res = minimize(obj, x0, method='BFGS')

    # 9. pack results
    sol = {v.name: float(val) for v, val in zip(vars_used, res.x)}
    sol['f']       = float(obj(res.x))
    sol['success'] = bool(res.success)
    return sol
# ----------------------------------------------------------------------

# quick self-test when run as a script -------------------------------
if __name__ == "__main__":
    sol = penalty_solve(
        "x**2 + y**2 + z**2",
        ["x*y - 1 = 0",
         "2*y*z - 1 = 0",
         "3*x*z - 1 >= 0",
         "x >= 0", "y >= 0", "z >= 0"],
        x0=[0.5, 1.0, 0.5]
    )
    print(sol)
