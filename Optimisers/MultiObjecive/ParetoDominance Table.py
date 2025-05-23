import pandas as pd
import numpy as np
import sympy as sp

# === User inputs ===
samples = np.arange(1, 9)
x_vals  = np.array([-0.75, -0.50, -0.25, 0.00, 0.50, 1.00, 1.25, 1.50])

# Objective function strings (as strings)
func_strs = [
    "x**2",          # f1(x)
    "x**2 - 2*x",    # f2(x)
    # Add more as needed
]

# === Symbolic setup ===
x = sp.symbols('x', real=True)
obj_funcs = [sp.lambdify(x, sp.sympify(s, locals={'x': x}), 'numpy') for s in func_strs]

# === DataFrame construction ===
df = pd.DataFrame({'sample': samples, 'x': x_vals})
for idx, fn in enumerate(obj_funcs, start=1):
    df[f'f{idx}'] = fn(x_vals)

# === Pareto ranking ===
def pareto_ranks(objs):
    n = len(objs)
    ranks = np.zeros(n, int)
    rem = set(range(n))
    current_rank = 1

    while rem:
        front = set()
        for i in rem:
            dominated = False
            for j in rem:
                if j == i:
                    continue
                if (all(objs[j][k] <= objs[i][k] for k in range(len(objs[i])))
                    and any(objs[j][k] < objs[i][k] for k in range(len(objs[i])))):
                    dominated = True
                    break
            if not dominated:
                front.add(i)

        for i in front:
            ranks[i] = current_rank
        rem -= front
        current_rank += 1

    return ranks

obj_cols = [f'f{idx}' for idx in range(1, len(obj_funcs)+1)]
objs = list(zip(*(df[col] for col in obj_cols)))
df['rank'] = pareto_ranks(objs)

groups = df.groupby('rank')['sample'].apply(list).to_dict()

for rank in sorted(groups):
    print(f"Rank {rank}: samples {groups[rank]}")

worst_rank = df['rank'].max()
print(f"\nLowest rank = {worst_rank}, sample(s) {groups[worst_rank]}")




import matplotlib.pyplot as plt

# Plot Pareto front (rank 1)
pareto_df = df[df['rank'] == 1]
plt.scatter(df['f1'], df['f2'], color='lightgray', label='All Samples')
plt.scatter(pareto_df['f1'], pareto_df['f2'], color='red', label='Pareto Front')

# Optional: label points
for _, row in pareto_df.iterrows():
    plt.annotate(f"{int(row['sample'])}", (row['f1'], row['f2']), fontsize=8, xytext=(5, -5), textcoords='offset points')

plt.title("Pareto Front (f1 vs f2)")
plt.xlabel("f1")
plt.ylabel("f2")
plt.legend()
plt.grid(True)
plt.show()