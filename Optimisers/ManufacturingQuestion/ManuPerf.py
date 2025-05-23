"""
2. The performance of a manufacturing process is characterised by
the performance index
x
f x x
1 ( ) = + where x is a control variable
set by the users in the range 0.75 < x ≤ 2. If f (x)is to be as low as
possible what is the optimal setting of x? If x is subject to
uniform random noise such that the probability density function of
the noise takes the form of a unit square centred at the nominal
value, derive an expression for the mean value of the
performance index and hence determine what value of x will
give the lowest mean value. What percentage deterioration in
nominal performance must be accepted when using this optimal
setting?
"""

import sympy as sp
x = sp.symbols('x', real=True, positive=True)


# INPUTS
f_str = "x + 1.78/x"
f_expr = sp.sympify(f_str, locals={'x': x})
# Feasible range
x_min, x_max = 0.8, 2.0
# Uniform noise half-width
h = 0.25


df = sp.diff(f_expr, x)
candidates = [c for c in sp.solve(df, x) if c.is_real and x_min < c < x_max]
x_nom = float(candidates[0])
f_nom = float(f_expr.subs(x, x_nom))

x_rob = float(sp.sqrt(1 + h**2))
f_rob_exact = float(f_expr.subs(x, x_rob))
f_rob = round(f_rob_exact, 4)

pct_drop = round((f_rob - f_nom) / f_nom * 100, 3)

print(f"Nominal optimum:        x* = {x_nom:.8f},  f = {f_nom:.8f}")
print(f"Noise‐robust “optimum”: x  = {x_rob:.8f},  f = {f_rob:.8f}")
print(f"Percent deterioration:   {pct_drop:.8f} %")