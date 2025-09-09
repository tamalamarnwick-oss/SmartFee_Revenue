#!/usr/bin/env python3
"""
Test the simplified WSGI implementation
"""
import os
import sys

# Add project root to path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

def test_wsgi_simple():
    """Test the simplified WSGI implementation"""
    print("Testing simplified WSGI implementation...")
    
    # Test 1: Import wsgi_simple
    try:
        print("\n1. Testing wsgi_simple import...")
        import wsgi_simple
        app = wsgi_simple.application
        print(f"[OK] wsgi_simple import successful: {type(app)}")
        
        # Test if it's callable (WSGI requirement)
        if callable(app):
            print("[OK] Application is callable (WSGI compliant)")
        else:
            print("[FAIL] Application is not callable")
            
    except Exception as e:
        print(f"[FAIL] wsgi_simple import failed: {e}")
        return False
    
    # Test 2: Test WSGI interface
    try:
        print("\n2. Testing WSGI interface...")
        
        # Mock WSGI environ
        environ = {
            'REQUEST_METHOD': 'GET',
            'PATH_INFO': '/',
            'SERVER_NAME': 'localhost',
            'SERVER_PORT': '5000',
            'wsgi.version': (1, 0),
            'wsgi.url_scheme': 'http',
            'wsgi.input': None,
            'wsgi.errors': sys.stderr,
            'wsgi.multithread': False,
            'wsgi.multiprocess': True,
            'wsgi.run_once': False
        }
        
        # Mock start_response
        response_data = {}
        def start_response(status, headers):
            response_data['status'] = status
            response_data['headers'] = headers
        
        # Call the WSGI app
        if hasattr(app, 'wsgi_app'):
            # Flask app
            result = app.wsgi_app(environ, start_response)
        else:
            # Direct WSGI callable
            result = app(environ, start_response)
            
        print(f"[OK] WSGI call successful, status: {response_data.get('status', 'Unknown')}")
        
    except Exception as e:
        print(f"[FAIL] WSGI interface test failed: {e}")
    
    # Test 3: Test health endpoint if available
    try:
        print("\n3. Testing health endpoint...")
        
        environ['PATH_INFO'] = '/health'
        response_data = {}
        
        if hasattr(app, 'wsgi_app'):
            result = app.wsgi_app(environ, start_response)
        else:
            result = app(environ, start_response)
            
        print(f"[OK] Health endpoint accessible, status: {response_data.get('status', 'Unknown')}")
        
    except Exception as e:
        print(f"[INFO] Health endpoint test: {e}")
    
    print("\nSimplified WSGI tests completed.")
    return True

def test_fallback_behavior():
    """Test the fallback behavior when dependencies are missing"""
    print("\n" + "="*50)
    print("Testing fallback behavior...")
    
    try:
        import wsgi_simple
        
        # Check if we're using the fallback app
        app = wsgi_simple.application
        
        if hasattr(app, 'name') and 'Flask' in str(type(app)):
            print("[OK] Fallback Flask app is active")
            
            # Test the status route
            with app.test_client() as client:
                response = client.get('/')
                if response.status_code == 200:
                    print("[OK] Status page accessible")
                    if 'SmartFee Application Status' in response.get_data(as_text=True):
                        print("[OK] Status page contains expected content")
                else:
                    print(f"[WARN] Status page returned {response.status_code}")
                
                # Test health endpoint
                response = client.get('/health')
                if response.status_code == 200:
                    print("[OK] Health endpoint accessible")
                else:
                    print(f"[WARN] Health endpoint returned {response.status_code}")
        
    except Exception as e:
        print(f"[FAIL] Fallback behavior test failed: {e}")

if __name__ == "__main__":
    success = test_wsgi_simple()
    if success:
        test_fallback_behavior()