import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x:2')
l = sp.Symbol('l')

# INPUTS
f_str = "x0 - x1 + 2*x0**2 + 2*x0*x1 + x1**3"  # function as string
num_iterations = 1
#NEED TO HAVE DECIMAL POINT AND 0 for starting points
x_k = np.array([0.0, 1.0])


f_expr = sp.sympify(f_str)
grad_expr = [sp.diff(f_expr, x[0]), sp.diff(f_expr, x[1])]

f_lambdified = sp.lambdify((x[0], x[1]), f_expr, 'numpy')

x0_vals = np.linspace(-13, 10, 200)
x1_vals = np.linspace(-13, 10, 200)
X0, X1 = np.meshgrid(x0_vals, x1_vals)
Z = f_lambdified(X0, X1)

trajectory = [x_k.copy()]

for k in range(1, num_iterations + 1):
    grad_k = [g.subs({x[0]: x_k[0], x[1]: x_k[1]}) for g in grad_expr]
    d_k = [-g.evalf() for g in grad_k]

    x_l = [x_k[0] + l * d_k[0], x_k[1] + l * d_k[1]]
    f_l = f_expr.subs({x[0]: x_l[0], x[1]: x_l[1]})
    df_dl = sp.diff(f_l, l)
    l_solutions = sp.solve(df_dl, l)
    l_real = [sol.evalf() for sol in l_solutions if sp.im(sol) == 0]

    if not l_real:
        print(f"Iteration {k}: No real step length found — stopping.")
        break

    l_star = float(l_real[0])
    x_new = x_k + l_star * np.array(d_k, dtype=np.float64)
    f_new = f_expr.subs({x[0]: x_new[0], x[1]: x_new[1]}).evalf()

    print(f"\nSteepest Descent: Iteration {k}")
    print("================================")
    print(f"Starting point:        x{k} = {x_k.tolist()}")
    print(f"Gradient ∇f(x{k}):       {[float(g) for g in grad_k]}")
    print(f"Descent direction d{k}:  {[float(d) for d in d_k]}")
    print(f"Step size (l*):        {l_star:.7f}")
    print(f"New point x{k+1}:          {[float(c) for c in x_new]}")
    print(f"Function value f(x{k+1}):  {float(f_new):.7f}")
    print("================================")

    x_k = x_new
    trajectory.append(x_k.copy())

# Plot contour + path
plt.contour(X0, X1, Z, levels=80, cmap='viridis')
traj = np.array(trajectory)
plt.plot(traj[:, 0], traj[:, 1], marker='o', color='red', label='Descent path')
plt.title("Steepest Descent on f(x₀, x₁)")
plt.xlabel("x₀")
plt.ylabel("x₁")
plt.legend()
plt.grid(True)
plt.show()
