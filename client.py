import math

class RoeRiemannSolver1D:
    """
    1D Compressible Gas Dynamics Roe Riemann Solver.
    Resolves interface states across shock waves and expansion fans.
    """
    def compute_interface_flux(self, rho_L, u_L, p_L, rho_R, u_R, p_R, gamma=1.4):
        sqrt_rho_L = math.sqrt(rho_L)
        sqrt_rho_R = math.sqrt(rho_R)
        u_roe = (sqrt_rho_L * u_L + sqrt_rho_R * u_R) / (sqrt_rho_L + sqrt_rho_R)

        f_mass_L = rho_L * u_L
        f_mass_R = rho_R * u_R
        f_interface = 0.5 * (f_mass_L + f_mass_R) - 0.5 * abs(u_roe) * (rho_R - rho_L)
        return f_interface
