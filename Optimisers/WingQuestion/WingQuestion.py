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
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def optimise_wing(
    cl_coeff,
    cl_offset,
    cd_const,
    cd_quad,
    initial_guess_alpha,
    stall_limit_alpha,
    V_cruise,
    V_landing,
    plot=False
):
    """
    Compute unconstrained and stall‐limited L/D optimums,
    but instead of printing to console, returns a single string
    with all the results.
    """
    # 0) ensure numeric
    cl_coeff            = float(cl_coeff)
    cl_offset           = float(cl_offset)
    cd_const            = float(cd_const)
    cd_quad             = float(cd_quad)
    initial_guess_alpha = float(initial_guess_alpha)
    stall_limit_alpha   = float(stall_limit_alpha)
    V_cruise            = float(V_cruise)
    V_landing           = float(V_landing)

    # 1) symbolic variable
    alpha = sp.symbols('alpha', real=True)

    # 2) define CL, CD, L/D
    CL = cl_coeff * (alpha + cl_offset)
    CD = cd_const + cd_quad * CL**2
    LD = CL / CD

    # 3) unconstrained optimum
    dLD = sp.diff(LD, alpha)
    alpha_opt = float(sp.nsolve(dLD, initial_guess_alpha))
    CL_opt    = float(CL.subs(alpha, alpha_opt))
    LD_opt    = float(LD.subs(alpha, alpha_opt))

    # 4) stall‐limited cruise
    CL_max   = cl_coeff * (stall_limit_alpha + cl_offset)
    CL_cr    = CL_max * (V_landing / V_cruise)**2
    alpha_cr = float(CL_cr / cl_coeff - cl_offset)
    CD_cr    = cd_const + cd_quad * CL_cr**2
    LD_cr    = CL_cr / CD_cr

    # 5) build result string
    lines = []
    lines.append("Unconstrained optimum:\n")
    lines.append(f"  α*    = {alpha_opt:.6f}°\n")
    lines.append(f"  C_L*  = {CL_opt:.6f}\n")
    lines.append(f"  (L/D)* = {LD_opt:.6f}\n\n")
    lines.append("Stall‐limited cruise:\n")
    lines.append(f"  α_cr   = {alpha_cr:.6f}°\n")
    lines.append(f"  C_L    = {CL_cr:.6f}\n")
    lines.append(f"  (L/D)  = {LD_cr:.6f}\n")

    result = "".join(lines)

    # 6) optional plot
    if plot:
        alphas = np.linspace(0, stall_limit_alpha, 300)
        LD_vals = (cl_coeff * (alphas + cl_offset)) / (
                    cd_const + cd_quad * (cl_coeff*(alphas + cl_offset))**2
                  )
        plt.plot(alphas, LD_vals, '-', label='L/D vs α')
        plt.axvline(alpha_opt, color='green', linestyle='--', label='α* unconstrained')
        plt.axvline(alpha_cr,  color='red',   linestyle='--', label='α_cr cruise limit')
        plt.xlabel("α (degrees)")
        plt.ylabel("L/D")
        plt.title("Lift‐to‐Drag Ratio vs Angle of Attack")
        plt.legend()
        plt.grid(True)
        plt.show()

    return result


"""
# Example usage:
if __name__ == "__main__":
    res = optimize_lift_drag(
        cl_coeff=0.093,
        cl_offset=1.0,
        cd_const=0.032,
        cd_quad=0.055,
        initial_guess_alpha=5.0,
        stall_limit_alpha=14.0,
        V_cruise=40.0,
        V_landing=15.0,
        plot=True
    )
    print("Unconstrained optimum:")
    print(f" α*    = {res['unconstrained']['alpha']:.4f}°")
    print(f" L/D*  = {res['unconstrained']['LD']:.4f}")
    print("\nStall-limited cruise:")
    print(f" α_cr  = {res['cruise_limited']['alpha']:.4f}°")
    print(f" L/D_cr = {res['cruise_limited']['LD']:.4f}")
"""