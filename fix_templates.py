#!/usr/bin/env python3
"""
Template Fix Script for SmartFee Application
This script fixes template loading issues in production deployment
"""

import os
import sys
import shutil

def fix_template_issues():
    """Fix common template loading issues"""
    
    # Get the application directory
    app_dir = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(app_dir, 'templates')
    
    print(f"Application directory: {app_dir}")
    print(f"Templates directory: {templates_dir}")
    
    # Check if templates directory exists
    if not os.path.exists(templates_dir):
        print("ERROR: Templates directory not found!")
        return False
    
    # Check for required template files
    required_templates = [
        'base.html',
        'index.html', 
        'login.html',
        'simple.html'
    ]
    
    missing_templates = []
    for template in required_templates:
        template_path = os.path.join(templates_dir, template)
        if not os.path.exists(template_path):
            missing_templates.append(template)
        else:
            print(f"✓ Found: {template}")
    
    if missing_templates:
        print(f"ERROR: Missing templates: {missing_templates}")
        return False
    
    # Check template permissions
    for template in required_templates:
        template_path = os.path.join(templates_dir, template)
        if not os.access(template_path, os.R_OK):
            print(f"ERROR: Cannot read template: {template}")
            return False
    
    print("✓ All required templates found and readable")
    
    # Create a simple test template to verify template loading
    test_template_path = os.path.join(templates_dir, 'test_template.html')
    test_content = '''<!DOCTYPE html>
<html>
<head><title>Template Test</title></head>
<body>
<h1>Template Loading Test</h1>
<p>If you see this, templates are working correctly.</p>
<p><a href="/login">Back to Login</a></p>
</body>
</html>'''
    
    try:
        with open(test_template_path, 'w', encoding='utf-8') as f:
            f.write(test_content)
        print("✓ Created test template")
    except Exception as e:
        print(f"ERROR: Could not create test template: {e}")
        return False
    
    return True

def check_flask_app():
    """Check Flask app configuration"""
    try:
        # Import the app to check configuration
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from app import app
        
        print(f"Flask app template folder: {app.template_folder}")
        print(f"Template folder exists: {os.path.exists(app.template_folder) if app.template_folder else 'None'}")
        
        if app.template_folder and os.path.exists(app.template_folder):
            templates = os.listdir(app.template_folder)
            print(f"Templates in folder: {templates}")
            return True
        else:
            print("ERROR: Flask app template folder not properly configured")
            return False
            
    except Exception as e:
        print(f"ERROR: Could not import Flask app: {e}")
        return False

if __name__ == '__main__':
    print("SmartFee Template Fix Script")
    print("=" * 40)
    
    success = True
    
    print("\n1. Checking template files...")
    if not fix_template_issues():
        success = False
    
    print("\n2. Checking Flask app configuration...")
    if not check_flask_app():
        success = False
    
    print("\n" + "=" * 40)
    if success:
        print("✓ All template checks passed!")
        print("The application should now work correctly.")
    else:
        print("✗ Template issues found!")
        print("Please fix the issues above before running the application.")
    
    sys.exit(0 if success else 1)