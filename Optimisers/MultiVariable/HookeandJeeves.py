import numpy as np
import sympy as sp
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def hooke_jeeves(func_str, initial_base, h=0.1, num_iterations=1, plot=False):
    # Symbolic setup
    base = np.array(initial_base, dtype=float)
    n = len(base)
    x_syms = sorted(sp.sympify(func_str).free_symbols, key=lambda s: s.name)
    expr = sp.sympify(func_str)
    f_num = sp.lambdify(x_syms, expr, 'numpy')

    def f(x):
        return float(f_num(*x))

    def fmt_pt(pt):
        return np.array(pt, dtype=float)

    trajectory = [base.copy()]
    history = []
    prev_base = base.copy()

    for k in range(1, num_iterations + 1):
        f_base = f(base)
        explored = base.copy()

        # Exploratory moves
        for i, xi in enumerate(x_syms):
            improved = False
            for direction in (+1, -1):
                trial = explored.copy()
                trial[i] += direction * h
                f_trial = f(trial)
                if f_trial < f_base:
                    f_base = f_trial
                    explored = trial
                    improved = True
                    break
            # if improved, move to next coordinate immediately
            if improved:
                continue

        # Pattern move
        pattern = explored + (explored - prev_base)
        f_pattern = f(pattern)

        # Decide whether to accept pattern or stay at explored
        if f_pattern < f_base:
            next_base = pattern
            f_next = f_pattern
        else:
            next_base = explored
            f_next = f_base

        history.append({
            'iteration':              k,
            'base_before':            prev_base.copy(),
            'base_after_explore':     explored.copy(),
            'pattern_point':          pattern.copy(),
            'f_base':                 f(prev_base),
            'f_explored':             f_base,
            'f_pattern':             f_pattern
        })
        prev_base = next_base.copy()
        base = next_base.copy()
        trajectory.append(base.copy())

        print(f"\nIteration {k}")
        print("--------------")
        print(f"Base start         = {trajectory[-2].tolist()}, f = {history[-1]['f_base']:.6f}")
        print(f"After explore      = {explored.tolist()}, f = {history[-1]['f_explored']:.6f}")
        print(f"Pattern point      = {pattern.tolist()}, f = {history[-1]['f_pattern']:.6f}")
        print(f"Next base          = {base.tolist()}")
        print("--------------")

    trajectory = np.vstack(trajectory)

    # Optional plot for 2D functions
    if plot and n == 2:
        mins = trajectory.min(axis=0) - h
        maxs = trajectory.max(axis=0) + h
        xs = np.linspace(mins[0], maxs[0], 200)
        ys = np.linspace(mins[1], maxs[1], 200)
        X, Y = np.meshgrid(xs, ys)
        Z = f_num(X, Y)

        plt.contour(X, Y, Z, levels=40, cmap='viridis')
        plt.plot(trajectory[:,0], trajectory[:,1], 'o-', color='red', label='HJ path')
        plt.title("Hooke–Jeeves on " + func_str)
        plt.xlabel(str(x_syms[0]))
        plt.ylabel(str(x_syms[1]))
        plt.grid(True)
        plt.legend()
        plt.show()

    return trajectory, history

"""
# Example usage:
if __name__ == "__main__":
    traj, hist = hooke_jeeves(
        func_str="x1 - x2 + 2*x1*x2 + 2*(x1**2) + x2**2",
        initial_base=[0.0, 0.0],
        num_iterations=8,
        h=0.25,
        plot=True
    )
    print("\nFinal trajectory:\n", traj)
    print("History records:")
    for record in hist:
        print(record)
"""