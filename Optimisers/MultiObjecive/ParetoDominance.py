import sympy as sp

# === User inputs ===
x = sp.symbols('x', real=True)

f_list = [
    x**3 - 3*x + 6,      # f1(x)
    3*x**2 + 3*x - 5,    # f2(x)
    #EXTRA FUNCTIONS HERE
]
# ====================

def find_minimizer(expr):
    """Solve expr'(x)=0, pick the real root where expr''>0 giving the smallest expr value."""
    d1 = sp.diff(expr, x)
    crits = sp.solve(d1, x)
    d2 = sp.diff(expr, x, 2)
    mins = [
        c for c in crits
        if c.is_real and d2.subs(x, c) > 0
    ]
    if not mins:
        raise RuntimeError(f"No real minimizer for {expr}")
    # pick the one with smallest f-value
    return float(min(mins, key=lambda c: expr.subs(x, c)))

# 1) Pure‐fi endpoints
endpoints = []
for fi in f_list:
    xi = find_minimizer(fi)
    vals = [float(fj.subs(x, xi)) for fj in f_list]
    endpoints.append((xi, *vals))

# 2) Equal‐weight compromise: minimize sum(fi)
Phi = sum(f_list)
dPhi = sp.diff(Phi, x)
critP = sp.solve(dPhi, x)
d2P = sp.diff(Phi, x, 2)
cands = [c for c in critP if c.is_real and d2P.subs(x, c) > 0]
if not cands:
    raise RuntimeError("No real compromise point found")
x_eq = float(cands[0])
vals_eq = [float(fj.subs(x, x_eq)) for fj in f_list]
compromise = (x_eq, *vals_eq)

# 3) Print results
print("Pareto endpoints (pure objectives):")
for i, tup in enumerate(endpoints, start=1):
    print(f" f{i}-only → {tup}")

print("\nEqual-weight compromise:")
print(f" {compromise}")
