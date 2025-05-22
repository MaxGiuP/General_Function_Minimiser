import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# User inputs
var_names    = ['x','y','z']
f_str        = 'x**2 + y**2 + z**2'
eq_constraints   = ['x*y - 1', '2*y*z - 1']
ineq_constraints = ['3*x*z - 1', 'x', 'y', 'z']  # x,y,z >= 0

# Symbolic setup
vars = sp.symbols(var_names)
f    = sp.sympify(f_str, locals=dict(zip(var_names,vars)))
eqs  = [sp.sympify(c,   locals=dict(zip(var_names,vars))) for c in eq_constraints]
ineq = [sp.sympify(c,   locals=dict(zip(var_names,vars))) for c in ineq_constraints]

lam = sp.symbols(f'lam0:{len(eqs)}')
L   = f - sum(l*e for l,e in zip(lam, eqs))
kkt_eqs = [sp.diff(L, v) for v in vars] + eqs
sols = sp.solve(kkt_eqs, list(vars)+list(lam), dict=True)

# Feasibility check
feasible = []
for sol in sols:
    if all(sol[v].is_real for v in vars) and all((ineq_i.subs(sol) >= 0) for ineq_i in ineq):
        feasible.append(sol)

# Plot 3D
if feasible:
    sol = feasible[0]
    x_val, y_val, z_val = [float(sol[v]) for v in vars]
    f_val = float(f.subs(sol))

    print(f"x = {x_val:.5f}, y = {y_val:.5f}, z = {z_val:.5f}")
    print(f"f = {f_val:.5f}")

    # Lambdify f for plotting
    f_func = sp.lambdify((vars[0], vars[1], vars[2]), f, 'numpy')

    # Meshgrid for plotting f(x, y, z) on a 3D surface
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    # Fix z to z_val and plot f(x, y, z_val)
    x_vals = np.linspace(0.1, 2.0, 100)
    y_vals = np.linspace(0.1, 2.0, 100)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = f_func(X, Y, z_val)  # f(x, y, fixed z)

    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    ax.scatter(x_val, y_val, f_val, color='red', s=50, label="Feasible Point")

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title(f"3D Plot of f(x, y, z)")
    ax.legend()
    plt.tight_layout()
    plt.show()

else:
    print("No feasible solution found.")
