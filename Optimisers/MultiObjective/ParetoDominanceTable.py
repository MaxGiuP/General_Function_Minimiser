import pandas as pd
import numpy as np
import sympy as sp
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def pareto_analysis(samples, x_vals, func_strs, plot=False):
    x = sp.symbols('x', real=True)
    exprs = [sp.sympify(s, locals={'x': x}) for s in func_strs]
    f_nums = [sp.lambdify(x, e, 'numpy') for e in exprs]

    df = pd.DataFrame({'sample': samples, 'x': x_vals})
    for i, fn in enumerate(f_nums, start=1):
        df[f'f{i}'] = fn(x_vals)

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
                    if j!=i and all(objs[j][k] <= objs[i][k] for k in range(len(objs[i]))) \
                            and any(objs[j][k] < objs[i][k] for k in range(len(objs[i]))):
                        dominated = True
                        break
                if not dominated:
                    front.add(i)
            for i in front:
                ranks[i] = current_rank
            rem -= front
            current_rank += 1
        return ranks

    obj_cols = [f'f{i}' for i in range(1, len(func_strs)+1)]
    objs = list(zip(*(df[col] for col in obj_cols)))
    df['rank'] = pareto_ranks(objs)

    groups = df.groupby('rank')['sample'].apply(list).to_dict()

    if plot and len(func_strs)==2:
        pareto_df = df[df['rank']==1]
        plt.scatter(df['f1'], df['f2'], color='lightgray', label='All samples')
        plt.scatter(pareto_df['f1'], pareto_df['f2'], color='red', label='Pareto front')
        for _, row in pareto_df.iterrows():
            plt.annotate(int(row['sample']), (row['f1'], row['f2']),
                         xytext=(5,-5), textcoords='offset points')
        plt.title("Pareto Front (f1 vs f2)")
        plt.xlabel("f1")
        plt.ylabel("f2")
        plt.legend()
        plt.grid(True)
        plt.show()

    return df, groups