import pandas as pd
import numpy as np

# === User inputs ===
# Sample indices and decision variable values
samples = np.arange(1, 9)
x_vals  = np.array([-0.75, -0.50, -0.25, 0.00, 0.50, 1.00, 1.25, 1.50])

# List of objective functions
obj_funcs = [
    lambda x: x**2,           # f1(x)
    lambda x: x**2 - 2*x,     # f2(x)
    #EXTRA FUNCTIONS HERE
]

df = pd.DataFrame({'sample': samples, 'x': x_vals})
for idx, fn in enumerate(obj_funcs, start=1):
    df[f'f{idx}'] = fn(x_vals)

def pareto_ranks(objs):
    """
    objs: list of tuples, each tuple has m objective values
    returns: rank array where rank=1 is Pareto‐front, 2 is next, etc.
    """
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
                    and any(objs[j][k] < objs[i][k]  for k in range(len(objs[i])))):
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
