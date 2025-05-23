import sympy as sp
import numpy as np

# ── user settings ─────────────────────────────────────────────────
func_str       = "x1 - x2 + 2*x1*x2 + 2*(x1**2) + x2**2"  # function string
num_iterations = 8    # number of Hooke–Jeeves iterations
h              = 0.25 # exploratory step size
base           = np.array([0.0, 0.0])  # starting point
# ─────────────────────────────────────────────────────────────────

# Parse and lambdify
expr    = sp.sympify(func_str)
symbols = sorted(expr.free_symbols, key=lambda s: s.name)  # [x1, x2]
f_num   = sp.lambdify(symbols, expr, 'numpy')

def f(x):
    return float(f_num(*x))

def format_point(pt):
    return ", ".join(f"{symbols[i].name}={pt[i]:.3f}" for i in range(len(pt)))

prev_expl = base.copy()

for itr in range(1, num_iterations+1):
    print(f"\n=== Iteration {itr} ===")
    current_val = f(base)
    
    # Exploratory moves
    for idx, var in enumerate(symbols):
        move_accepted = False
        for direction, sign in [(+1, '+'), (-1, '-')]:
            trial = base.copy()
            trial[idx] += direction * h
            val = f(trial)
            print(f"[{var.name} {sign}h] trial=({format_point(trial)}), f={val:.6f}", end='')
            if val < current_val:
                print("  → Accept")
                base = trial
                current_val = val
                move_accepted = True
                print(f"    Accepted move at {var.name} {sign}h to point ({format_point(trial)})")
                break
            else:
                print("  → Reject")
        if move_accepted:
            # skip remaining direction on this coordinate
            continue

    # Pattern move
    pattern = base + (base - prev_expl)
    pat_val = f(pattern)
    print(f"[Pattern] trial=({format_point(pattern)}), f={pat_val:.6f}", end='')
    if pat_val < f(base):
        print("  → Accept")
        print(f"    Accepted pattern move to point ({format_point(pattern)})")
        prev_expl = base.copy()
        base = pattern
    else:
        print("  → Reject")
        prev_expl = base.copy()
