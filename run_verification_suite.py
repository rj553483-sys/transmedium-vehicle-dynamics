import os
import subprocess

def run_all():
    print("Executing complete verification suite...\n")
    subprocess.run(["python3", "src/verify_mhd.py"], check=True)
    subprocess.run(["python3", "src/verify_structural.py"], check=True)
    subprocess.run(["python3", "src/verify_mass_ledger.py"], check=True)
    print("ALL VERIFICATION SUITES COMPLETED SUCCESSFULLY.\n")

if __name__ == '__main__':
    run_all()
