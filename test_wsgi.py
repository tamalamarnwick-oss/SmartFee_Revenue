#!/usr/bin/env python3
"""
Test script to verify WSGI configuration
"""
import sys
import os

# Add the project directory to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    print("Testing WSGI import...")
    from wsgi import application
    print("✅ WSGI import successful")
    print(f"Application type: {type(application)}")
    print(f"Application name: {application.name}")
    
    print("\nTesting direct app import...")
    from app import app
    print("✅ Direct app import successful")
    print(f"App type: {type(app)}")
    print(f"App name: {app.name}")
    
    print("\nTesting app configuration...")
    with app.app_context():
        print(f"Secret key configured: {'Yes' if app.config.get('SECRET_KEY') else 'No'}")
        print(f"Database URI configured: {'Yes' if app.config.get('SQLALCHEMY_DATABASE_URI') else 'No'}")
    
    print("\n✅ All tests passed! WSGI configuration is correct.")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)