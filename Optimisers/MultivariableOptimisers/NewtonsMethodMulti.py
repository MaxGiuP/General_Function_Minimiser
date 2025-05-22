import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# === User settings ===
initial_guess  = [0.5, -1.0]
num_iterations = 3

# === Symbolic setup ===
num_vars = len(initial_guess)
x_syms   = sp.symbols(f'x0:{num_vars}')
x0, x1 = x_syms
f_expr = x0**2 + 3*x1**2 - x0*x1 + 2*x0 - 4*x1 + 1

# Gradient and Hessian
grad_syms = [sp.diff(f_expr, xi) for xi in x_syms]
hess_syms = [[sp.diff(g, xj) for xj in x_syms] for g in grad_syms]

# Numeric lambdified functions
f_num    = sp.lambdify(x_syms, f_expr, 'numpy')
grad_num = sp.lambdify(x_syms, grad_syms, 'numpy')
hess_num = sp.lambdify(x_syms, hess_syms, 'numpy')

# Store points for trajectory
trajectory = [np.array(initial_guess, dtype=float)]

# === Newton's Method ===
x = np.array(initial_guess, dtype=float)

for i in range(1, num_iterations+1):
    fx = f_num(*x)
    g  = np.array(grad_num(*x), dtype=float)
    H  = np.array(hess_num(*x), dtype=float)

    if np.linalg.matrix_rank(H) < len(x):
        print(f"Iteration {i}: Hessian singular — stopping early.")
        break

    delta = np.linalg.solve(H, g)
    x_new = x - delta

    print(f"\nIteration {i}")
    print("--------------")
    print(f"x[{i-1}]        = {x.tolist()}")
    print(f"f(x[{i-1}])     = {fx:.6f}")
    print(f"∇f(x[{i-1}])    = {g.tolist()}")
    print("Hessian matrix:")
    print(H)
    print(f"Newton step δ  = {delta.tolist()}")
    print(f"x[{i}]        = {x_new.tolist()}")
    print("--------------")

    x = x_new
    trajectory.append(x.copy())

# === Plotting ===
# Create contour grid
f_plot = sp.lambdify((x0, x1), f_expr, 'numpy')
x_vals = np.linspace(-2, 2, 200)
y_vals = np.linspace(-2, 2, 200)
X, Y = np.meshgrid(x_vals, y_vals)
Z = f_plot(X, Y)

# Plot contour and path
plt.figure(figsize=(8,6))
contours = plt.contour(X, Y, Z, levels=50, cmap='viridis')
plt.clabel(contours, inline=True, fontsize=8)

# Trajectory
traj = np.array(trajectory)
plt.plot(traj[:,0], traj[:,1], marker='o', color='red', label='Newton Path')
plt.quiver(traj[:-1,0], traj[:-1,1],
           traj[1:,0] - traj[:-1,0],
           traj[1:,1] - traj[:-1,1],
           angles='xy', scale_units='xy', scale=1, color='red')

plt.title("Newton's Method on f(x₀, x₁)")
plt.xlabel("x₀")
plt.ylabel("x₁")
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()
