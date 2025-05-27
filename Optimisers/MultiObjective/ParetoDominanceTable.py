import pandas as pd
import numpy as np
import sympy as sp
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

def pareto_analysis(func_strs, x_inputs, samples, plot=False):
    x_vals = np.array(x_inputs)

    df = pd.DataFrame({"sample": samples, "x": x_vals})

    x = sp.symbols("x", real=True)
    f_lambdas = [
        sp.lambdify(x, sp.sympify(s), "numpy")
        for s in func_strs
    ]

    for i, f in enumerate(f_lambdas, start=1):
        df[f"f{i}"] = f(x_vals)

    def pareto_ranks(objs):
        n = len(objs)
        ranks = np.zeros(n, int)
        rem   = set(range(n))
        current = 1
        while rem:
            front = set()
            for i in rem:
                dominated = False
                for j in rem:
                    if j==i: continue
                    if (all(objs[j][k] <= objs[i][k] for k in range(len(objs[i])))
                        and any(objs[j][k]  < objs[i][k] for k in range(len(objs[i])))):
                        dominated = True
                        break
                if not dominated:
                    front.add(i)
            for i in front:
                ranks[i] = current
            rem -= front
            current += 1
        return ranks

    obj_cols = [f"f{i}" for i in range(1, len(f_lambdas)+1)]
    objs     = list(zip(*(df[col] for col in obj_cols)))
    df["rank"] = pareto_ranks(objs)

    groups = df.groupby("rank")["sample"].apply(list).to_dict()
    lines = []
    for r in sorted(groups):
        lines.append(f"Rank {r}: samples {groups[r]}\n")
    worst = df["rank"].max()
    lines.append(f"\nLowest rank = {worst}, sample(s) {groups[worst]}\n")
    log = "".join(lines)

    if plot and len(f_lambdas)==2:
        pareto_df = df[df["rank"]==1]
        plt.scatter(df["f1"], df["f2"], color="lightgray", label="All samples")
        plt.scatter(pareto_df["f1"], pareto_df["f2"], color="red", label="Pareto front")
        for _, row in pareto_df.iterrows():
            plt.annotate(int(row["sample"]), (row["f1"], row["f2"]),
                         xytext=(5,-5), textcoords="offset points")
        plt.title("Pareto Front (f1 vs f2)")
        plt.xlabel("f1"); plt.ylabel("f2")
        plt.legend(); plt.grid(True)
        plt.show()

    return log



"""
# ── Example usage ─────────────────────────────────────────────
if __name__=="__main__":
    samples    = np.arange(1,9)
    x_vals     = np.array([-0.75, -0.50, -0.25, 0.00, 0.50, 1.00, 1.25, 1.50])
    func_strs  = ["x**2", "x**2 - 2*x"]
    logstr = pareto_analysis(func_strs, samples, x_vals, plot=True)
    print(logstr)
"""