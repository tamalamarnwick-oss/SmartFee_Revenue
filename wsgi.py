"""
WSGI entry point for SmartFee Revenue Collection.
This file is used by Gunicorn to serve the application.
"""
import os
import sys

# Add the project directory to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    # Import the Flask app directly
    from app import app as application
    print("WSGI: Successfully imported Flask app")
except ImportError as e:
    print(f"WSGI: Error importing app: {e}")
    # Create a minimal Flask app as fallback
    from flask import Flask
    application = Flask(__name__)
    
    @application.route('/')
    def hello():
        return "SmartFee is starting up..."
    
    @application.route('/health')
    def health():
        return {"status": "ok", "message": "Fallback app running"}

# For local development if needed
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    debug = os.environ.get('FLASK_DEBUG', '0') == '1'
    print(f"Starting server on port {port} with debug={debug}")
    try:
        application.run(host='0.0.0.0', port=port, debug=debug)
    except Exception as e:
        print(f"Error starting server: {e}")
        raise