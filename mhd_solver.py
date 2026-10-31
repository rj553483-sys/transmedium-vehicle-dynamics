import numpy as np

def compute_skin_depth(f_hz=25000.0, sigma=4.5, mu_r=1.0):
    mu_0 = 4.0 * np.pi * 1e-7
    return np.sqrt(1.0 / (np.pi * f_hz * mu_0 * mu_r * sigma))

def compute_thrust(s, F_peak=100.0, s_opt=0.33):
    return F_peak * (1.0 - ((s - s_opt) / s_opt)**2)

if __name__ == '__main__':
    print(f"Skin Depth: {compute_skin_depth():.4f} m")
    print(f"Peak Thrust: {compute_thrust(0.33):.1f} kN")
