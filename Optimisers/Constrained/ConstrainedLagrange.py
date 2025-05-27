import numpy as np
import sympy as sp
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import itertools

def lagrange(f_str, eq_strs=None, ineq_strs=None, plot=False):
    eq_strs   = [s.strip() for s in (eq_strs or [])   if s.strip()]
    ineq_strs = [s.strip() for s in (ineq_strs or []) if s.strip()]

    logs = []

    f      = sp.sympify(f_str)
    eqs    = [sp.sympify(s) for s in eq_strs]
    ineqs  = [sp.sympify(s) for s in ineq_strs]

    vars_syms = sorted(
        f.free_symbols
         .union(*(g.free_symbols for g in eqs))
         .union(*(h.free_symbols for h in ineqs)),
        key=lambda s: s.name
    )
    if not vars_syms:
        raise ValueError("No decision variables detected.")

    best      = None
    best_fval = np.inf

    for r in range(len(ineqs)+1):
        for active in itertools.combinations(range(len(ineqs)), r):
            lam_eq   = sp.symbols(f"lam_eq0:{len(eqs)}", real=True)
            lam_ineq = sp.symbols(f"lam_i0:{r}",   real=True) if r>0 else ()

            L = f
            for j, g in enumerate(eqs):
                L += lam_eq[j] * g
            for k, idx in enumerate(active):
                L += lam_ineq[k] * ineqs[idx]

            stat_eqs     = [sp.diff(L, v) for v in vars_syms]
            constraint_eqs = eqs + [ineqs[i] for i in active]
            eqns = stat_eqs + constraint_eqs

            unknowns = tuple(vars_syms) + lam_eq + lam_ineq
            sols = sp.solve(eqns, unknowns, dict=True)

            for sol in sols:
                if not all(sol[v].is_real for v in vars_syms):
                    continue
                feas = True
                for j in set(range(len(ineqs))) - set(active):
                    if float(ineqs[j].subs(sol)) <= 0:
                        feas = False
                        break
                if not feas:
                    continue

                fval = float(f.subs(sol))
                if fval < best_fval:
                    best_fval = fval
                    best      = sol

    if best is None:
        raise RuntimeError("No feasible KKT solution found.")

    best_vals = {str(v): float(best[v]) for v in vars_syms}

    logs.append("Optimal solution:\n")
    for v in vars_syms:
        logs.append(f"  {v} = {best_vals[str(v)]:.4f}\n")
    logs.append(f"  f = {best_fval:.4f}\n")

    result = "".join(logs)
    return result

"""
# Example usage:
if __name__ == "__main__":
    # Solve min 5/(x0 * x1**2)  s.t.  x0**2 + x1**2 = 4
    f_str      = "5/(x0 * x1**2)"
    eq_lines   = ["x0**2 + x1**2 - 4"]
    ineq_lines = []

    result_str = lagrange(f_str, eq_lines, ineq_lines)
    print(result_str)
"""