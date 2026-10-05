"""
Flask Application Automated Test Suite
Verifies application initialization, route status codes, template rendering, and API payloads.
"""
import sys
import os

# Add project root to sys.path
sys.path.insert(0, r"C:\Skillwallet")
from flask_app.app import app

def run_tests():
    print("=" * 60)
    print("STARTING FLASK WEB APPLICATION TESTS")
    print("=" * 60)
    
    client = app.test_client()
    passed = 0
    total = 0

    routes = [
        ('/', 'Home Route', 200, b'Analysing Mental Health in Student Ecosystem'),
        ('/dashboard', 'Dashboard Embed Route', 200, b'Interactive Tableau Dashboard'),
        ('/insights', 'Insights Route', 200, b'Empirical Insights'),
        ('/about', 'About Project Route', 200, b'About the Study'),
        ('/api/summary', 'API Summary Endpoint', 200, b'total_students')
    ]

    for route, name, expected_code, expected_content in routes:
        total += 1
        res = client.get(route)
        if res.status_code == expected_code and (expected_content in res.data):
            print(f"[PASS] {name} ({route}) -> Status: {res.status_code}")
            passed += 1
        else:
            print(f"[FAIL] {name} ({route}) -> Got {res.status_code}, expected {expected_code}")

    print("-" * 60)
    print(f"TEST RESULTS: {passed}/{total} Passed")
    print("=" * 60)
    return passed == total

if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
