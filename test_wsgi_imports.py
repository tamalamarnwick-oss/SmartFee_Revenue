#!/usr/bin/env python3
"""
Test script to verify WSGI imports work correctly
"""
import os
import sys

# Add project root to path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

def test_wsgi_imports():
    """Test different WSGI import scenarios"""
    print("Testing WSGI imports...")
    
    # Test 1: Root wsgi.py
    try:
        print("\n1. Testing root wsgi.py import...")
        import wsgi
        app = wsgi.application
        print(f"[OK] Root WSGI import successful: {type(app)}")
    except Exception as e:
        print(f"[FAIL] Root WSGI import failed: {e}")
    
    # Test 2: your_application wsgi.py
    try:
        print("\n2. Testing your_application wsgi.py import...")
        from your_application import wsgi as your_wsgi
        app = your_wsgi.application
        print(f"[OK] your_application WSGI import successful: {type(app)}")
    except Exception as e:
        print(f"[FAIL] your_application WSGI import failed: {e}")
    
    # Test 3: Direct app.py import
    try:
        print("\n3. Testing direct app.py import...")
        from app import app
        print(f"[OK] Direct app.py import successful: {type(app)}")
    except Exception as e:
        print(f"[FAIL] Direct app.py import failed: {e}")
    
    # Test 4: your_application create_app
    try:
        print("\n4. Testing your_application create_app...")
        from your_application import create_app
        app = create_app()
        print(f"[OK] your_application create_app successful: {type(app)}")
    except Exception as e:
        print(f"[FAIL] your_application create_app failed: {e}")
    
    print("\nWSGI import tests completed.")

if __name__ == "__main__":
    test_wsgi_imports()