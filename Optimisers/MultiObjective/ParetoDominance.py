import sympy as sp
import math

def pareto_front(func_strs, plot=False):
    exprs = [sp.sympify(s) for s in func_strs]
    syms  = set().union(*(e.free_symbols for e in exprs))
    if len(syms) != 1:
        raise ValueError("Expected exactly one decision variable")
    var = syms.pop()

    def find_min(e):
        d1 = sp.diff(e, var)
        crits = sp.solve(d1, var)
        d2 = sp.diff(e, var, 2)
        mins = [c for c in crits if c.is_real and d2.subs(var, c) > 0]
        if not mins:
            raise RuntimeError(f"No real minimizer for {e}")
        return float(min(mins, key=lambda c: float(e.subs(var, c))))

    endpoints = []
    for f in exprs:
        x_i = find_min(f)
        f1 = float(exprs[0].subs(var, x_i))
        f2 = float(exprs[1].subs(var, x_i))
        endpoints.append((x_i, f1, f2))

    Phi = exprs[0] + exprs[1]
    x_eq = find_min(Phi)
    f1_eq = float(exprs[0].subs(var, x_eq))
    f2_eq = float(exprs[1].subs(var, x_eq))
    compromise = (x_eq, f1_eq, f2_eq)

    def fmt(triple):
        return "{" + ",".join(
            f"{v:.6g}" for v in triple
        ) + "}"

    s = f"{fmt(endpoints[0])}, {fmt(endpoints[1])}, {fmt(compromise)}"
    return s


"""
# ── Test ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    funcs = ["x**3 - 3*x + 6", "3*x**2 + 3*x - 5"]
    print(pareto_front(funcs))
    # prints: {1,4,1}, {-0.5,7.375,-5.75}, {0,6,-5}
"""