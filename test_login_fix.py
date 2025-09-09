#!/usr/bin/env python3
"""
Test script to verify login template rendering fix
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app

def test_login_template():
    """Test that login template can be rendered without errors"""
    with app.test_client() as client:
        try:
            response = client.get('/login')
            print(f"Login page status code: {response.status_code}")
            
            if response.status_code == 200:
                print("[PASS] Login template renders successfully!")
                # Check if the response contains expected content
                if b'SmartFee' in response.data or b'login' in response.data.lower():
                    print("[PASS] Login page contains expected content")
                else:
                    print("[WARN] Login page rendered but may be using fallback HTML")
            else:
                print(f"[FAIL] Login page returned status code: {response.status_code}")
                
        except Exception as e:
            print(f"[ERROR] Error testing login template: {e}")

if __name__ == '__main__':
    print("Testing login template fix...")
    test_login_template()