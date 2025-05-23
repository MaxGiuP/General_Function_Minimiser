"""
2. The lift coefficient of an aircraft wing, CL , is given by 0.09(α+2)
where α is the angle of attack in degrees. The drag coefficient,
CD , is given by 0.02+0.055CL
2
. If the lift to drag ratio is to be
maximized what is the optimal angle of attack the aircraft should
fly at and what then is the lift to drag ratio.
If the cruise speed is 40 m/s and the landing speed is 15 m/s,
while the maximum angle of attack is constrained by stall limits to
be no more than 14°, what is the best cruise lift to drag ratio that
can actually be achieved without changing the wing geometry for
landing.
The coefficients are found from the lift and drag by dividing by
½ρV2
A where the symbols have their usual meanings.
"""

import sympy as sp
import numpy as np

# === User inputs ===
cl_coeff            = 0.093    # coefficient in CL = cl_coeff*(alpha + cl_offset)
cl_offset           = 1.0     # offset in the CL expression
cd_const            = 0.032    # constant term in CD = cd_const + cd_quad*CL**2
cd_quad             = 0.055   # quadratic term coefficient in CD
initial_guess_alpha = 5.0     # initial guess (°) for Newton solve
stall_limit_alpha   = 12.0    # maximum allowable angle of attack (degrees)
V_cruise            = 33.0    # cruise speed (m/s)
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
