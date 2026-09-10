from client import RoeRiemannSolver1D

def main():
    print("=== Testing Roe Approximate Riemann Shock Solver ===")
    solver = RoeRiemannSolver1D()

    # Sod Shock Tube condition
    flux = solver.compute_interface_flux(
        rho_L=1.0, u_L=0.75, p_L=1.0,
        rho_R=0.125, u_R=0.0, p_R=0.1
    )
    print("Calculated Roe numerical interface mass flux:", round(flux, 4))
    assert flux > 0.0
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
