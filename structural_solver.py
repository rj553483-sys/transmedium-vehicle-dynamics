import numpy as np

def compute_tsai_wu(s1=200.0, s2=25.0, XT=2500.0, XC=1800.0, YT=85.0, YC=250.0, S12=120.0):
    F1 = 1/XT - 1/XC
    F11 = 1/(XT*XC)
    F2 = 1/YT - 1/YC
    F22 = 1/(YT*YC)
    F12 = -0.5 * np.sqrt(F11 * F22)
    f_tw = F1*s1 + F2*s2 + F11*(s1**2) + F22*(s2**2) + 2*F12*s1*s2
    fos = 1.0 / np.sqrt(f_tw)
    return f_tw, fos

if __name__ == '__main__':
    f_tw, fos = compute_tsai_wu()
    print(f"Tsai-Wu index: {f_tw:.4f}, FoS: {fos:.2f}")
