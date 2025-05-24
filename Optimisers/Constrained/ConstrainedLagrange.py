import sympy as sp
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import itertools

def lagrange(f_str, eq_strs=None, ineq_strs=None, plot=False):
    eq_strs   = eq_strs   or []
    ineq_strs = ineq_strs or []

    # 1) Parse expressions
    f      = sp.sympify(f_str)
    eqs    = [sp.sympify(s) for s in eq_strs]
    hs     = [sp.sympify(s) for s in ineq_strs]

    # 2) Auto-detect variables
    vars_syms = sorted(
        f.free_symbols
         .union(*(g.free_symbols for g in eqs))
         .union(*(h.free_symbols for h in hs)),
        key=lambda s: s.name
    )
    n = len(vars_syms)
    if n < 1:
        raise ValueError("No decision variables detected.")
    # limit plotting to 2D
    x_sym, y_sym = (vars_syms + [None])[:2]

    # 3) Enumerate active‐set combinations
    best        = None
    best_fval   = np.inf
    best_active = None
    all_solutions = []

    for r in range(len(hs)+1):
        for active in itertools.combinations(range(len(hs)), r):
            # multipliers
            lam_eq   = sp.symbols(f"lam_eq0:{len(eqs)}", real=True)
            lam_ineq = sp.symbols(f"lam_i0:{r}",   real=True) if r>0 else ()

            # Lagrangian
            L = f
            for j, g in enumerate(eqs):
                L += lam_eq[j] * g
            for k, idx in enumerate(active):
                L += lam_ineq[k] * hs[idx]

            # KKT equations: stationarity + active constraints
            stationarity = [sp.diff(L, v) for v in vars_syms]
            constraint_eqs = eqs + [hs[i] for i in active]
            eqns = stationarity + constraint_eqs

            # unknowns = decision vars + multipliers
            unknowns = tuple(vars_syms) + lam_eq + lam_ineq
            sols = sp.solve(eqns, unknowns, dict=True)

            for sol in sols:
                # check real
                if not all(sol[v].is_real for v in vars_syms):
                    continue
                # inactive inequalities must satisfy h>0
                feasible = True
                for j in set(range(len(hs))) - set(active):
                    if float(hs[j].subs(sol)) <= 0:
                        feasible = False
                        break
                if not feasible:
                    continue

                all_solutions.append(sol)
                fval = float(f.subs(sol))
                if fval < best_fval:
                    best_fval   = fval
                    best        = sol
                    best_active = active

    if best is None:
        raise RuntimeError("No feasible KKT solution found.")

    # Prepare output dict of numeric values
    best_vals = {str(v): float(best[v]) for v in vars_syms}

    # Optional 2D plot
    if plot and n == 2:
        # build grid around solutions
        pts = np.array([[float(sol[v]) for v in vars_syms] for sol in all_solutions])
        mins = pts.min(axis=0) - 1
        maxs = pts.max(axis=0) + 1
        xs = np.linspace(mins[0], maxs[0], 200)
        ys = np.linspace(mins[1], maxs[1], 200)
        X, Y = np.meshgrid(xs, ys)
        f_num = sp.lambdify((x_sym, y_sym), f, 'numpy')
        Z = f_num(X, Y)

        plt.contour(X, Y, Z, levels=40, cmap='viridis')
        # mark all KKT candidates
        for sol in all_solutions:
            px, py = float(sol[x_sym]), float(sol[y_sym])
            plt.plot(px, py, 'kx', alpha=0.5)
        # highlight the best
        bx, by = best_vals[str(x_sym)], best_vals[str(y_sym)]
        plt.plot(bx, by, 'ro', label='Optimal')
        plt.title("KKT Solutions for " + f_str)
        plt.xlabel(str(x_sym))
        plt.ylabel(str(y_sym))
        plt.legend()
        plt.grid(True)
        plt.show()

    return best_vals, best_fval, best_active, all_solutions