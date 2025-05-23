import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import itertools

# ── USER INPUT ───────────────────────────────────────────────────────
f_str      = "3.2 + 2.8*(x0**2) + 2.5*(x1**2)"
eq_strs    = [""]      # == 0
ineq_strs  = ['x*y - 2.1', 'y', 'x']               # >= 0
# If you wanted to force ≥0 region, put e.g. ["x**2+y**2-4"] here.
# ─────────────────────────────────────────────────────────────────────

# 1) Parse everything
f    = sp.sympify(f_str)
eqs  = [sp.sympify(s) for s in eq_strs]
hs   = [sp.sympify(s) for s in ineq_strs]

# 2) Auto‐discover variables
vars_syms = sorted(
    f.free_symbols
     .union(*(c.free_symbols for c in eqs))
     .union(*(h.free_symbols for h in hs)),
    key=lambda s: s.name
)
if len(vars_syms) != 2:
    raise ValueError("Plotting version requires exactly 2 decision variables!")
x_sym, y_sym = vars_syms

# 3) Prepare lambdified functions
f_num   = sp.lambdify((x_sym, y_sym), f, 'numpy')
eq_nums = [sp.lambdify((x_sym, y_sym), e, 'numpy') for e in eqs]
h_nums  = [sp.lambdify((x_sym, y_sym), h, 'numpy') for h in hs]

# 4) Active‐set enumeration
best      = None
best_fval = np.inf
best_act  = None
real_sols = []

for r in range(len(hs)+1):
    for active_idxs in itertools.combinations(range(len(hs)), r):
        # multipliers
        lam_eq   = sp.symbols(f"lam_eq0:{len(eqs)}", real=True)
        lam_ineq = sp.symbols(f"lam_i0:{r}", real=True) if r>0 else ()

        # Lagrangian
        L = f
        for j, g in enumerate(eqs):
            L += lam_eq[j]*g
        for k, idx in enumerate(active_idxs):
            L += lam_ineq[k]*hs[idx]

        # KKT equations
        stat = [sp.diff(L, v) for v in vars_syms]
        eqs_on = eqs + [hs[i] for i in active_idxs]
        eqns  = stat + eqs_on

        sols = sp.solve(eqns, tuple(vars_syms)+tuple(lam_eq)+tuple(lam_ineq),
                        dict=True)
        for sol in sols:
            # real check
            if not all(sol[v].is_real for v in vars_syms):
                continue
            # inactive inequalities >0
            ok = True
            for j in set(range(len(hs))) - set(active_idxs):
                if float(hs[j].subs(sol)) <= 0:
                    ok = False; break
            if not ok:
                continue
            real_sols.append(sol)
            fval = float(f.subs(sol))
            if fval < best_fval:
                best_fval = fval
                best = sol
                best_act = active_idxs

# 5) Report
if best is None:
    raise RuntimeError("No feasible KKT solution found.")
print("Optimal solution:")
print(f"  {x_sym} = {float(best[x_sym]):.6f}, {y_sym} = {float(best[y_sym]):.6f}")
print(f"  f = {best_fval:.6f}")
print("Active constraints:")
if not best_act:
    print("  (none)")
else:
    for i in best_act:
        print(" ", ineq_strs[i], "= 0")
