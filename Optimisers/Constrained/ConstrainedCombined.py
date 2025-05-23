import sympy as sp
import itertools

# ── User inputs (all as strings) ─────────────────────────────────────
f_str    = "3.82+2.23*(x**2)+2.32*(y**2)"
eq_strs  = ["x-0.76"]                  # ==0
h_strs   = []   # >= 0
# ────────────────────────────────────────────────────────────────────

# 1) Symbol setup — declare whatever symbols you’ll use
#    (you could also parse these from the strings dynamically)
x, y, z = sp.symbols('x y z', positive=True, real=True)

# 2) Parse into Sympy expressions
f   = sp.sympify(f_str,   locals=dict(x=x, y=y, z=z))
eqs = [sp.sympify(s,      locals=dict(x=x, y=y, z=z)) for s in eq_strs]
hs  = [sp.sympify(s,      locals=dict(x=x, y=y, z=z)) for s in h_strs]

best     = None
best_f   = float('inf')
best_act = None

# 3) Active‐set enumeration over all subsets of {h1, h2, …}
for r in range(len(hs)+1):
    for active_idxs in itertools.combinations(range(len(hs)), r):
        # 3a) Build Lagrangian: L = f - λ0·eq0 - Σ λi·h_i(active)
        lam0 = sp.symbols('lam0')
        lam  = sp.symbols(f'lam1:{r+1}') if r>0 else ()
        L    = f - lam0*eqs[0]
        for idx, λ in zip(active_idxs, lam):
            L = L - λ*hs[idx]

        # 3b) Stationarity ∇_x L = 0
        stat_eqs = [sp.diff(L, v) for v in (x, y, z)]
        # plus the always‐on equality and the “active” inequalities
        solve_eqs = stat_eqs + eqs + [hs[i] for i in active_idxs]

        sols = sp.solve(solve_eqs, (x, y, z, lam0, *lam), dict=True)

        # 3c) Filter real solutions that satisfy the *inactive* h_j > 0
        for sol in sols:
            if not all(sol[v].is_real for v in (x, y, z)):
                continue
            # check inactive ones are strictly ≥ 0
            ok = True
            for j in set(range(len(hs))) - set(active_idxs):
                if float(hs[j].subs(sol)) <= 0:
                    ok = False
                    break
            if not ok:
                continue

            # 3d) Evaluate objective
            val = float(f.subs(sol))
            if val < best_f:
                best_f   = val
                best     = sol
                best_act = active_idxs

# 4) Report
print("Optimal solution:")
print(f"  x = {best[x]:.6f}, y = {best[y]:.6f}, z = {best[z]:.6f}")
print(f"  f = {best_f:.6f}")
print("Active constraints:")
for i in best_act:
    print(" ", h_strs[i], "= 0")
