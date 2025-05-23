import sympy as sp
import numpy as np
from scipy.optimize import minimize

# ── User inputs ──────────────────────────────────────────────────────
f_str    = "x**2 + y**2 + z**2"
eq_strs  = ["x*y - 1"]                # == 0
h_strs   = ["2*y*z - 1", "3*x*z - 1"] # >= 0
# Penalty schedule
R0        = 1.0      # initial (small) penalty
scale     = 10.0     # multiply R by this each outer iteration
max_round = 6        # maximum number of outer loops
tol       = 1e-6     # tolerance for considering a constraint “satisfied”  
# ─────────────────────────────────────────────────────────────────────

# 1) Parse to Sympy
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
if not vars:
    raise ValueError("No decision variables found.")

# 3) Lambdify all
f_num  = sp.lambdify(vars, f, 'numpy')
eq_num = [sp.lambdify(vars, e, 'numpy') for e in eqs]
h_num  = [sp.lambdify(vars, h, 'numpy') for h in hs]

# 4) Initial guess
x0 = np.ones(len(vars))

# 5) Outer loop: gradually increase penalty over “time”
for k in range(max_round):
    R = R0 * (scale ** k)

    # 6) Build penalty objective F(x) for this R
    def F(x):
        val = f_num(*x)
        # equality penalties: R * (h_j(x))^2
        for eq in eq_num:
            v = eq(*x)
            val += R * (v**2)
        # inequality penalties: R * max(0, -g_i(x))^2
        for h in h_num:
            v = h(*x)
            if v < 0:
                val += R * ((-v)**2)
        return val

    # 7) Unconstrained minimization of F
    res = minimize(F, x0, method='BFGS')
    x0  = res.x  # warm‐start next round

    # 8) Evaluate constraint residuals
    eq_viol = np.array([abs(eq(*x0)) for eq in eq_num])
    h_vals  = np.array([h(*x0)        for h in h_num])

    # 9) Check if all eqs nearly zero and all hs >= 0
    if np.all(eq_viol < tol) and np.all(h_vals >= -tol):
        break

# 10) Package & print final result
sol_dict = {vars[i].name: x0[i] for i in range(len(vars))}
sol_dict['f*'] = float(f_num(*x0))

print("Optimal solution:")
print(" ", ", ".join(f"{k}={v:.6f}" for k,v in sol_dict.items()))
print(f"\nFinal penalty weight R = {R:.1e}")
print("Constraint residuals:")
for s, v in zip(eq_strs, eq_viol):
    print(f"  {s}=0 → |{v:.3e}|")
for s, v in zip(h_strs, h_vals):
    print(f"  {s}>=0 → {v:.3e}")
