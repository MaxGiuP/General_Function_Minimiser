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
    f_num = sp.lambdify(tuple(x_syms), expr, 'numpy')

    def f(x):
        return float(f_num(*x))

    logs = []
    trajectory = [base.copy()]
    prev_base = base.copy()

    for k in range(1, num_iterations + 1):
        f_base = f(base)
        explored = base.copy()

        logs.append(f"\nIteration {k}\n")
        logs.append("--------------\n")
        logs.append(f"Base start       = {prev_base.tolist()}, f = {f_base:.6f}\n")

        # Exploratory moves
        for i, xi in enumerate(x_syms):
            for direction in (+1, -1):
                trial = explored.copy()
                trial[i] += direction * h
                f_trial = f(trial)
                logs.append(f" Trial {xi.name} {'+' if direction>0 else '-'}h → {trial.tolist()}, f={f_trial:.6f}")
                if f_trial < f_base:
                    logs.append("  → Accept\n")
                    f_base = f_trial
                    explored = trial
                    break
                else:
                    logs.append("  → Reject\n")
            if f_base != f(prev_base):  # if improved, skip to next coordinate
                continue

        logs.append(f" After exploratory  = {explored.tolist()}, f = {f_base:.6f}\n")

        # Pattern move
        pattern = explored + (explored - prev_base)
        f_pattern = f(pattern)
        logs.append(f" Pattern point     = {pattern.tolist()}, f = {f_pattern:.6f}")
        if f_pattern < f_base:
            logs.append("  → Accept\n")
            next_base = pattern
        else:
            logs.append("  → Reject\n")
            next_base = explored

        logs.append(f" Next base         = {next_base.tolist()}\n")
        logs.append("--------------\n")

        prev_base = next_base.copy()
        base = next_base.copy()
        trajectory.append(base.copy())

    # Optional 2D plot
    if plot and n == 2:
        mins = np.min(trajectory, axis=0) - h
        maxs = np.max(trajectory, axis=0) + h
        xs = np.linspace(mins[0], maxs[0], 200)
        ys = np.linspace(mins[1], maxs[1], 200)
        X, Y = np.meshgrid(xs, ys)
        Z = f_num(X, Y)
        plt.contour(X, Y, Z, levels=40, cmap='viridis')
        traj = np.vstack(trajectory)
        plt.plot(traj[:,0], traj[:,1], 'o-', color='red', label='HJ path')
        plt.title("Hooke–Jeeves on " + func_str)
        plt.xlabel(str(x_syms[0]))
        plt.ylabel(str(x_syms[1]))
        plt.grid(True)
        plt.legend()
        plt.show()

    result = "".join(logs)
    return result

"""
# Example usage:
if __name__ == "__main__":
    log_output = hooke_jeeves(
        func_str="x1 - x2 + 2*x1*x2 + 2*(x1**2) + x2**2",
        initial_base=[0.0, 0.0],
        h=0.25,
        num_iterations=3,
        plot=False
    )
    print(log_output)
"""