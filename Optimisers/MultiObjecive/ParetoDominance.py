import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
x = sp.symbols('x', real=True)

# INPUT
func_strs = [
    "1.9*(x**3) - 2.2*x + 7.2",     # f1(x)
    "3.1*(x**2) - 2.4*x + 1.6",   # f2(x)
    # Add more here
]



f_list = [sp.sympify(s, locals={'x': x}) for s in func_strs]

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
    return float(min(mins, key=lambda c: expr.subs(x, c)))

endpoints = []
for fi in f_list:
    xi = find_minimizer(fi)
    vals = [float(fj.subs(x, xi)) for fj in f_list]
    endpoints.append((xi, *vals))

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

print("Pareto endpoints (pure objectives):")
for i, tup in enumerate(endpoints, start=1):
    print(f" f{i}-only → {tup}")

print("\nEqual-weight compromise:")
print(f" {compromise}")


# ── Plot Pareto front ────────────────────────────────────────────
# Weighted-sum sampling
f_list = [sp.sympify(s, locals={'x': x}) for s in func_strs]
f1, f2 = f_list

alphas = np.linspace(0, 1, 100)
pareto_points = []

for alpha in alphas:
    Phi = alpha * f1 + (1 - alpha) * f2
    dPhi = sp.diff(Phi, x)
    d2Phi = sp.diff(Phi, x, 2)

    crits = sp.solve(dPhi, x)
    mins = [c for c in crits if c.is_real and d2Phi.subs(x, c) > 0]

    if mins:
        # Pick the global min among local minima
        x_star = min(mins, key=lambda c: Phi.subs(x, c))
        f1_val = float(f1.subs(x, x_star))
        f2_val = float(f2.subs(x, x_star))
        pareto_points.append((f1_val, f2_val))

# Plot
f1_vals, f2_vals = zip(*pareto_points)
plt.scatter(f1_vals, f2_vals, s=15)
plt.title("Pareto Front (f1 vs f2)")
plt.xlabel("f1")
plt.ylabel("f2")
plt.grid(True)
plt.show()