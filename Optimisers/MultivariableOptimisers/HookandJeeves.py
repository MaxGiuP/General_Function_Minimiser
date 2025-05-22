import numpy as np

# ── user settings ─────────────────────────────────────────────────
num_iterations = 2         # number of pattern iterations
h               = 0.1      # exploratory step size
# ─────────────────────────────────────────────────────────────────

def f(x):
    return x[0] - x[1] + 2*x[0]*(x[1]**2) + x[1]**3

#Starting Point
base       = np.array([0.0, 1.0])


prev_expl  = base.copy()
all_values = []

for itr in range(1, num_iterations + 1):

    print(f"\n=== Iteration {itr} ===")

    for idx in range(len(base)):
        trial = base.copy()
        trial[idx] += h
        f_val = f(trial)
        all_values.append(f_val)
        print(f"[x[{idx}] +h] point = {trial},  f = {f_val:.8f}")
        if f_val < f(base):
            base = trial

        trial = base.copy()
        trial[idx] -= h
        f_val = f(trial)
        all_values.append(f_val)
        print(f"[x[{idx}] -h] point = {trial},  f = {f_val:.8f}")
        if f_val < f(base):
            base = trial

    expl_val = f(base)
    print(f"Exploratory base after all coords: {base},  f = {expl_val:.8f}")

    pattern = base + (base - prev_expl)
    pat_val = f(pattern)
    all_values.append(pat_val)
    print(f"Pattern point: {pattern},  f = {pat_val:.8f}")

    prev_expl = base.copy()
    base      = pattern.copy()

n = len(prev_expl)
step_values = 2 * n + 1
print("\nRaw f-values by iteration:")
for k in range(num_iterations):
    group = all_values[k*step_values : (k+1)*step_values]
    group_str = ", ".join(f"{v:.3f}" for v in group)
    print(f"iter {k+1}: {{ {group_str} }}")
