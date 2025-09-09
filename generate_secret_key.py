#!/usr/bin/env python3
"""
Generate a secure secret key for Flask application
"""
import secrets

# Generate a secure random secret key
secret_key = secrets.token_urlsafe(32)
print(f"SECRET_KEY={secret_key}")
print("\nCopy the above line and add it to your Render environment variables.")