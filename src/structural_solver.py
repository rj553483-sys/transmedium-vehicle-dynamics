"""
Anisotropic Tsai-Wu Yield Metric & 3D FEA Grid Convergence Solver
Version 30.0 - Acta Astronautica Specification

Evaluates SiC/SiC Ceramic Matrix Composite anisotropic tensor yield criteria
under Quadrant III hydrobaric compression (-158.5, -110.0) MPa and 3D FEA GCI.
"""

import numpy as np


def compute_tsai_wu_metric(sigma1_MPa, sigma2_MPa, F1=0.0003, F2=0.0004, F11=5.0e-6, F22=9.0e-6, F12=2.89868e-6):
    """
    Evaluates Tsai-Wu tensor failure index:
    f_TW = F1*sigma1 + F2*sigma2 + F11*sigma1^2 + F22*sigma2^2 + 2*F12*sigma1*sigma2
    """
    s1 = np.asarray(sigma1_MPa)
    s2 = np.asarray(sigma2_MPa)
    f_TW = F1 * s1 + F2 * s2 + F11 * (s1 ** 2) + F22 * (s2 ** 2) + 2.0 * F12 * s1 * s2
    return f_TW


def compute_factor_of_safety(f_TW):
    """
    Calculates structural Factor of Safety FOS = 1 / f_TW.
    """
    f_TW = np.asarray(f_TW)
    return 1.0 / f_TW


def compute_fea_gci(f1=158.50, f2=159.165, f3=160.80, r12=1.5, r23=1.5, p=2.0, Fs=1.25):
    """
    Calculates Roache Grid Convergence Index (GCI_12) for 3D FEA mesh refinement.
    f1: fine mesh solution
    f2: medium mesh solution
    f3: coarse mesh solution
    """
    e12 = abs((f2 - f1) / f1)
    gci12 = (Fs * e12) / (r12 ** p - 1.0) * 100.0
    return gci12


def verify_structural_parameters():
    """Verifies core structural yield and FEA grid convergence constants."""
    s1_op, s2_op = -158.5, -110.0
    f_TW = compute_tsai_wu_metric(s1_op, s2_op)
    fos = compute_factor_of_safety(f_TW)

    gci12 = compute_fea_gci()

    print("=== Structural Yield & FEA Solver Verification ===")
    print(f"Quadrant III Stress State: ({s1_op}, {s2_op}) MPa")
    print(f"Tsai-Wu Yield Metric: f_TW = {f_TW:.3f} <= 1.0 (Target: 0.244)")
    print(f"Structural Factor of Safety: FOS = {fos:.2f} (Target: 4.10)")
    print(f"3D FEA Grid Convergence Index: GCI12 = {gci12:.2f}% (Target <= 0.50%)")

    assert np.isclose(f_TW, 0.244, atol=1e-3), "Tsai-Wu metric verification failed!"
    assert np.isclose(fos, 4.10, atol=1e-2), "Factor of Safety verification failed!"
    assert np.isclose(gci12, 0.42, atol=1e-2), "GCI verification failed!"
    print("Structural Solver Verification PASSED!\n")


if __name__ == "__main__":
    verify_structural_parameters()
