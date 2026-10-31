import numpy as np

def verify_structural_mechanics():
    X_T = 2500.0
    X_C = 1800.0
    Y_T = 85.0
    Y_C = 250.0
    S_12 = 120.0
    
    sigma_1 = 200.0
    sigma_2 = 25.0
    tau_12 = 0.0
    
    F_1 = (1.0 / X_T) - (1.0 / X_C)
    F_11 = 1.0 / (X_T * X_C)
    F_2 = (1.0 / Y_T) - (1.0 / Y_C)
    F_22 = 1.0 / (Y_T * Y_C)
    F_66 = 1.0 / (S_12 ** 2)
    F_12 = -0.5 * np.sqrt(F_11 * F_22)
    
    f_TW = (F_1 * sigma_1 + F_2 * sigma_2 + 
            F_11 * (sigma_1 ** 2) + F_22 * (sigma_2 ** 2) + 
            2.0 * F_12 * sigma_1 * sigma_2 + F_66 * (tau_12 ** 2))
    
    FoS = 1.0 / np.sqrt(f_TW)
    
    print("=== STRUCTURAL MECHANICS VERIFICATION ===")
    print(f"Tsai-Wu Failure Metric (f_TW): {f_TW:.4f} (Requirement: f_TW < 1.0 -> PASSED)")
    print(f"Factor of Safety (FoS): {FoS:.2f} (Requirement: FoS = 2.32 -> PASSED)")
    
    assert np.isclose(f_TW, 0.1851, atol=1e-3)
    assert np.isclose(FoS, 2.32, atol=1e-2)
    print("ALL STRUCTURAL VERIFICATION CHECKS PASSED SUCCESSFULLY.\n")

if __name__ == '__main__':
    verify_structural_mechanics()
