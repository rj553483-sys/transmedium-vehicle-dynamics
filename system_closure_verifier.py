import numpy as np

def verify_closure():
    masses = [800.0, 400.0, 400.0, 200.0, 200.0]
    total_mass = sum(masses)
    power_mw = (100.0e3 * 50.0) / 1e6
    return total_mass, power_mw

if __name__ == '__main__':
    m, p = verify_closure()
    print(f"Mass: {m} kg, Power: {p} MW")
