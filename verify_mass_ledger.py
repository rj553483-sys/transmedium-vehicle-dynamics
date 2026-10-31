import pandas as pd

def verify_mass_ledger():
    data = {
        'Subsystem Component': [
            'Hull Core (T1000/Epoxy Shell)',
            'MHD Channels & Magnet Loops',
            'PEM Fuel Cell Powerplant Stack',
            'Cryogenic LN2 & Fuel Tankage',
            'Avionics, Sensors, & Payload'
        ],
        'Mass (kg)': [800.0, 400.0, 400.0, 200.0, 200.0],
        'Percentage Share': [40.0, 20.0, 20.0, 10.0, 10.0]
    }
    df = pd.DataFrame(data)
    total_mass = df['Mass (kg)'].sum()
    total_pct = df['Percentage Share'].sum()
    
    print("=== SYSTEM MASS ALLOCATION AUDIT ===")
    print(df.to_string(index=False))
    print(f"\nTotal Vehicle Gross Mass (M_0): {total_mass:.1f} kg")
    print(f"Total Budget Closure: {total_pct:.2f}%")
    
    assert total_mass == 2000.0
    assert total_pct == 100.0
    print("MASS LEDGER AUDIT PASSED SUCCESSFULLY WITH 100.00% CLOSURE.\n")

if __name__ == '__main__':
    verify_mass_ledger()
