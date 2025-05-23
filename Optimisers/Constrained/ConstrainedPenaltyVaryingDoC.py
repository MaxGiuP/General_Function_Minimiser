import sympy as sp
import numpy as np
from scipy.optimize import minimize

# ── User inputs ──────────────────────────────────────────────────────
f_str    = "x**2 + y**2 + z**2"
eq_strs  = ["x*y - 1"]               # each treated as h(x)=0
h_strs   = ["2*y*z - 1", "3*x*z - 1"] # each treated as g(x)>=0
R        = 1e3                       # penalty scale
# ─────────────────────────────────────────────────────────────────────

# 1) Parse into Sympy
f   = sp.sympify(f_str)
eqs = [sp.sympify(s) for s in eq_strs]
hs  = [sp.sympify(s) for s in h_strs]

# 2) Auto‐detect variables
vars = sorted(
    f.free_symbols
     .union(*(e.free_symbols for e in eqs))
     .union(*(h.free_symbols for h in hs)),
    key=lambda s: s.name
)

# 3) Lambdify objective & constraints
f_num   = sp.lambdify(vars, f, 'numpy')
eq_num  = [sp.lambdify(vars, e, 'numpy') for e in eqs]
h_num   = [sp.lambdify(vars, h, 'numpy') for h in hs]

# 4) Degree‐of‐violation penalty function
def F(x):
    val = f_num(*x)
    # equality penalties: R * (h(x))^2
    for eq in eq_num:
        v = eq(*x)
        val += R * (v**2)
    # inequality penalties: R * max(0, -g(x))^2
    for h in h_num:
        v = h(*x)
        if v < 0:
            val += R * ((-v)**2)
    return val

# 5) Initial guess
x0 = np.ones(len(vars))

# 6) Unconstrained minimize of F
res = minimize(F, x0, method='BFGS')
sol = res.x

# 7) Report
sol_dict = {vars[i].name: sol[i] for i in range(len(vars))}
sol_dict['f*'] = f_num(*sol)

print("Optimal solution:")
print(" ", ", ".join(f"{k}={v:.6f}" for k,v in sol_dict.items()))

# 8) Constraint violations
print("\nConstraint violations (should be near zero):")
for s, eq in zip(eq_strs, eq_num):
    print(f"  {s}=0  →  {eq(*sol):.3e}")
for s, h in zip(h_strs, h_num):
    print(f"  {s}>=0 →  {h(*sol):.3e}")
