import sympy as sp
import numpy as np

# === User inputs ===
cl_coeff            = 0.09    # coefficient in CL = cl_coeff*(alpha + cl_offset)
cl_offset           = 2.0     # offset in the CL expression
cd_const            = 0.02    # constant term in CD = cd_const + cd_quad*CL**2
cd_quad             = 0.055   # quadratic term coefficient in CD
initial_guess_alpha = 5.0     # initial guess (°) for Newton solve
stall_limit_alpha   = 14.0    # maximum allowable angle of attack (degrees)
V_cruise            = 40.0    # cruise speed (m/s)
V_landing           = 15.0    # landing speed (m/s)
# ====================

# Define symbolic variable
alpha = sp.symbols('alpha', real=True)

# Lift and drag coefficients
CL = cl_coeff * (alpha + cl_offset)
CD = cd_const + cd_quad * CL**2

# Lift-to-drag ratio
LD = CL / CD

# Find unconstrained optimum by solving d(L/D)/dα = 0
dLD = sp.diff(LD, alpha)
alpha_opt = float(sp.nsolve(dLD, initial_guess_alpha))
CL_opt    = float(CL.subs(alpha, alpha_opt))
LD_opt    = float(LD.subs(alpha, alpha_opt))

print("Unconstrained optimum:")
print(f" α*    = {alpha_opt:.6f}°")
print(f" C_L*  = {CL_opt:.6f}")
print(f"(L/D)* = {LD_opt:.6f}\n")

# Stall-limited cruise performance
CL_max  = cl_coeff * (stall_limit_alpha + cl_offset)
CL_cr   = CL_max * (V_landing / V_cruise)**2
alpha_cr = CL_cr / cl_coeff - cl_offset
CD_cr   = cd_const + cd_quad * CL_cr**2
LD_cr   = CL_cr / CD_cr

print("Constraint-limited cruise:")
print(f" α_cr  = {alpha_cr:.6f}°")
print(f" C_L   = {CL_cr:.6f}")
print(f"(L/D)  = {LD_cr:.6f}")
