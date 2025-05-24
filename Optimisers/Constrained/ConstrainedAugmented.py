import sympy as sp
import itertools
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def augmented(f_str, eq_strs=None, ineq_strs=None, plot=False):
    eq_strs = eq_strs or []
    ineq_strs  = ineq_strs  or []

    # 1) parse everything
    f_expr   = sp.sympify(f_str)
    eq_exprs = [sp.sympify(s) for s in eq_strs]
    ineq_exprs  = [sp.sympify(s) for s in ineq_strs]

    # 2) detect variables from all expressions
    vars_syms = sorted(
        f_expr.free_symbols
         .union(*(e.free_symbols for e in eq_exprs))
         .union(*(h.free_symbols for h in ineq_exprs)),
        key=lambda s: s.name
    )
    n = len(vars_syms)
    if n == 0:
        raise ValueError("No decision variables found in your strings.")

    # 3) do active‐set enumeration
    best       = None
    best_fval  = np.inf
    best_active= None
    all_sols   = []

    # for each subset of inequalities assumed active
    for r in range(len(ineq_exprs)+1):
        for active_idxs in itertools.combinations(range(len(ineq_exprs)), r):
            # multipliers
            lam_eq   = sp.symbols(f"lam_eq0:{len(eq_exprs)}", real=True)
            lam_ineq = sp.symbols(f"lam_i0:{r}", real=True) if r>0 else ()
            # build L = f - Σ λ_eq·eq_expr - Σ λ_ineq·h_expr(active)
            L = f_expr
            for j, g in enumerate(eq_exprs):
                L -= lam_eq[j] * g
            for k, idx in enumerate(active_idxs):
                L -= lam_ineq[k] * ineq_exprs[idx]
            # stationarity + enforce eqs + active hs = 0
            stat_eqs   = [sp.diff(L, v) for v in vars_syms]
            constraint_eqs = eq_exprs + [ineq_exprs[i] for i in active_idxs]
            eqns = stat_eqs + constraint_eqs
            unknowns = tuple(vars_syms) + lam_eq + lam_ineq

            sols = sp.solve(eqns, unknowns, dict=True)
            for sol in sols:
                # only real decision‐var solutions
                if not all(sol[v].is_real for v in vars_syms):
                    continue
                # inactive inequalities must be ≥ 0
                feasible = True
                for j in set(range(len(ineq_exprs))) - set(active_idxs):
                    if float(ineq_exprs[j].subs(sol)) <= 0:
                        feasible = False
                        break
                if not feasible:
                    continue

                all_sols.append(sol)
                fval = float(f_expr.subs(sol))
                if fval < best_fval:
                    best_fval   = fval
                    best        = sol
                    best_active = active_idxs

    if best is None:
        raise RuntimeError("No feasible KKT solution found.")

    # package best decision‐vars into a dict
    best_vals = {str(v): float(best[v]) for v in vars_syms}

    # optional 2D plot
    if plot and n == 2:
        x_sym, y_sym = vars_syms
        # grid around all solutions
        pts = np.array([[float(sol[x_sym]), float(sol[y_sym])] for sol in all_sols])
        mins = pts.min(axis=0) - 1
        maxs = pts.max(axis=0) + 1
        xs = np.linspace(mins[0], maxs[0], 200)
        ys = np.linspace(mins[1], maxs[1], 200)
        X, Y = np.meshgrid(xs, ys)
        f_num = sp.lambdify((x_sym, y_sym), f_expr, 'numpy')
        Z = f_num(X, Y)
        plt.contour(X, Y, Z, levels=40, cmap='viridis')
        # mark every KKT candidate
        for sol in all_sols:
            plt.plot(float(sol[x_sym]), float(sol[y_sym]), 'kx', alpha=0.5)
        # highlight the best
        bx, by = best_vals[str(x_sym)], best_vals[str(y_sym)]
        plt.plot(bx, by, 'ro', label='Optimal')
        plt.title("KKT Active‐Set Solutions for\n" + f_str)
        plt.xlabel(str(x_sym))
        plt.ylabel(str(y_sym))
        plt.legend()
        plt.grid(True)
        plt.show()

    return best_vals, best_fval, best_active, all_sols
