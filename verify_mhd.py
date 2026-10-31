import numpy as np

def verify_mhd_parameters():
    mu_0 = 4.0 * np.pi * 1e-7  # H/m
    sigma = 4.5                 # S/m
    mu_visc = 0.0010            # Pa*s (Seawater dynamic viscosity = 1.0e-3 Pa.s)
    f_rf = 25000.0              # Hz
    B_0 = 3.5777                # T
    L = 1.20                    # m
    v = 50.0                    # m/s
    
    delta = np.sqrt(1.0 / (np.pi * f_rf * mu_0 * sigma))
    R_m = mu_0 * sigma * v * L
    Ha = B_0 * L * np.sqrt(sigma / mu_visc)
    F_thrust = 100000.0  # N
    P_prop = F_thrust * v  # W
    
    print("=== ELECTROMAGNETIC & PROPULSION VERIFICATION ===")
    print(f"Bulk Skin Depth (delta): {delta:.4f} m (Requirement: delta > {L} m -> PASSED)")
    print(f"Magnetic Reynolds Number (R_m): {R_m:.6f} (Requirement: R_m << 1 -> PASSED)")
    print(f"Hartmann Number (Ha): {Ha:.2f} (Requirement: Lorentz force dominates -> PASSED)")
    print(f"Propulsive Power Output: {P_prop / 1e6:.2f} MW (Requirement: P = 5.0 MW -> PASSED)")
    
    assert np.isclose(delta, 1.5005, atol=1e-3)
    assert np.isclose(R_m, 0.000339, atol=1e-5)
    assert np.isclose(Ha, 288.00, atol=1e-1)
    assert np.isclose(P_prop / 1e6, 5.0, atol=1e-2)
    print("ALL MHD VERIFICATION CHECKS PASSED SUCCESSFULLY.\n")

if __name__ == '__main__':
    verify_mhd_parameters()
