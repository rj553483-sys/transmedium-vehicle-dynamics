import numpy as np

def compute_fsi():
    mach_water = 50.0 / 1500.0
    eigenvalues = [1.43, 2.06, 3.31]
    return mach_water, eigenvalues

if __name__ == '__main__':
    m, ev = compute_fsi()
    print(f"Water Mach: {m:.4f}, Eigenvalues: {ev}")
