#!/usr/bin/env python3
"""
Deployment check script for SmartFee Revenue Collection System
Verifies all necessary files and directories are present for deployment
"""

import os
import sys

def check_deployment():
    """Check if all required files and directories exist"""
    print("SmartFee Deployment Check")
    print("=" * 40)
    
    # Required files
    required_files = [
        'app.py',
        'requirements.txt',
        'Procfile',
        'runtime.txt'
    ]
    
    # Required directories
    required_dirs = [
        'templates',
        'static'
    ]
    
    # Critical template files
    critical_templates = [
        'templates/login.html',
        'templates/index.html',
        'templates/base.html',
        'templates/students.html',
        'templates/income.html',
        'templates/expenditure.html'
    ]
    
    all_good = True
    
    # Check required files
    print("\nChecking required files:")
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - MISSING")
            all_good = False
    
    # Check required directories
    print("\nChecking required directories:")
    for dir in required_dirs:
        if os.path.exists(dir) and os.path.isdir(dir):
            file_count = len(os.listdir(dir))
            print(f"✅ {dir}/ ({file_count} files)")
        else:
            print(f"❌ {dir}/ - MISSING")
            all_good = False
    
    # Check critical templates
    print("\nChecking critical template files:")
    for template in critical_templates:
        if os.path.exists(template):
            print(f"✅ {template}")
        else:
            print(f"❌ {template} - MISSING")
            all_good = False
    
    # Check template directory contents
    if os.path.exists('templates'):
        templates = [f for f in os.listdir('templates') if f.endswith('.html')]
        print(f"\nTotal templates found: {len(templates)}")
        if len(templates) < 10:
            print("⚠️  Warning: Less than 10 templates found. Some features may not work.")
    
    # Check static directory contents
    if os.path.exists('static'):
        static_files = []
        for root, dirs, files in os.walk('static'):
            static_files.extend(files)
        print(f"Total static files found: {len(static_files)}")
    
    # Check environment file
    if os.path.exists('.env'):
        print("✅ .env file found (for local development)")
    else:
        print("ℹ️  No .env file (using environment variables)")
    
    print("\n" + "=" * 40)
    if all_good:
        print("✅ Deployment check PASSED - All critical files present")
        return True
    else:
        print("❌ Deployment check FAILED - Missing critical files")
        return False

if __name__ == "__main__":
    success = check_deployment()
    sys.exit(0 if success else 1)