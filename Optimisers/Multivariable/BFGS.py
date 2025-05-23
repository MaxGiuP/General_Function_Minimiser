import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# === User settings ===
f_str = "x0**2 + 3*x1**2 - x0*x1 + 2*x0 - 4*x1 + 1"  # Function as string
initial_guess = [0.5, -1.0]
num_iterations = 5

# === Symbolic setup ===
num_vars = len(initial_guess)
x_syms = sp.symbols(f'x0:{num_vars}')
f_expr = sp.sympify(f_str)

# Gradient and lambdified functions
grad_syms = [sp.diff(f_expr, xi) for xi in x_syms]
f_num = sp.lambdify(x_syms, f_expr, 'numpy')
grad_num = sp.lambdify(x_syms, grad_syms, 'numpy')

# === BFGS Setup ===
x = np.array(initial_guess, dtype=float)
n = num_vars
Hk = np.eye(n)

# Line search parameters
alpha_init = 1.0
rho = 0.8
c1 = 1e-4

def line_search(f, grad, x, p):
    alpha = alpha_init
    fx = f(*x)
    gx = grad(*x)
    while True:
        x_new = x + alpha * p
        if f(*x_new) <= fx + c1 * alpha * np.dot(gx, p):
            break
        alpha *= rho
    return alpha

trajectory = [x.copy()]

# === BFGS Iterations ===
for k in range(1, num_iterations + 1):
    gx = np.array(grad_num(*x), dtype=float)
    pk = -Hk.dot(gx)

    alpha = line_search(f_num, grad_num, x, pk)
    sk = alpha * pk
    x_new = x + sk

    gx_new = np.array(grad_num(*x_new), dtype=float)
    yk = gx_new - gx
    syk = np.dot(yk, sk)

    if syk > 1e-12:  # Update Hessian approximation
        rho_k = 1.0 / syk
        I = np.eye(n)
        Vk = I - rho_k * np.outer(sk, yk)
        Hk = Vk @ Hk @ Vk.T + rho_k * np.outer(sk, sk)

    print(f"\nIteration {k}")
    print("--------------")
    print(f"x[{k-1}] = {x.tolist()}")
    print(f"f(x[{k-1}]) = {f_num(*x):.6f}")
    print(f"∇f(x[{k-1}]) = {gx.tolist()}")
    print(f"Direction p  = {pk.tolist()}")
    print(f"Step α       = {alpha:.6f}")
    print(f"x[{k}]       = {x_new.tolist()}")
    print("--------------")

    x = x_new
    trajectory.append(x.copy())

# === Plotting ===
x0, x1 = x_syms
f_plot = sp.lambdify((x0, x1), f_expr, 'numpy')
x_vals = np.linspace(-2, 2, 200)
y_vals = np.linspace(-2, 2, 200)
X, Y = np.meshgrid(x_vals, y_vals)
Z = f_plot(X, Y)

plt.figure(figsize=(8, 6))
contours = plt.contour(X, Y, Z, levels=50, cmap='viridis')
plt.clabel(contours, inline=True, fontsize=8)

# Trajectory path
traj = np.array(trajectory)
plt.plot(traj[:, 0], traj[:, 1], marker='o', color='red', label='BFGS Path')
plt.quiver(traj[:-1, 0], traj[:-1, 1],
           traj[1:, 0] - traj[:-1, 0],
           traj[1:, 1] - traj[:-1, 1],
           angles='xy', scale_units='xy', scale=1, color='red')

plt.title("BFGS Optimization Path on f(x₀, x₁)")
plt.xlabel("x₀")
plt.ylabel("x₁")
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()
