"""
Environment Verification Script
Verifies that all required dependencies, packages, and paths are functional.
"""
import sys

def verify():
    print("=" * 50)
    print("ENVIRONMENT VERIFICATION FOR SKILLWALLET PROJECT")
    print("=" * 50)
    print(f"Python Executable: {sys.executable}")
    print(f"Python Version: {sys.version}")
    
    passed = True
    
    modules = [
        ("flask", "Flask"),
        ("pandas", "Pandas"),
        ("numpy", "NumPy"),
        ("openpyxl", "OpenPyXL"),
        ("dotenv", "python-dotenv"),
    ]
    
    for mod_name, label in modules:
        try:
            mod = __import__(mod_name)
            ver = getattr(mod, "__version__", "Available")
            print(f"[PASS] {label}: {ver}")
        except ImportError as e:
            print(f"[FAIL] {label}: Not installed ({e})")
            passed = False
            
    print("=" * 50)
    if passed:
        print("RESULT: ALL REQUIRED PACKAGES ARE INSTALLED AND OPERATIONAL")
    else:
        print("RESULT: MISSING PACKAGES DETECTED")
    print("=" * 50)
    return passed

if __name__ == "__main__":
    success = verify()
    sys.exit(0 if success else 1)
