"""
Simplified WSGI entry point for SmartFee Revenue Collection.
This version has minimal dependencies and better error handling.
"""
import os
import sys

# Add the project directory to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

def create_application():
    """Create the Flask application with proper error handling"""
    main_error = None
    factory_error = None
    
    try:
        # First try to import the main app
        from app import app
        print("WSGI: Successfully loaded main application from app.py")
        return app
    except ImportError as e:
        main_error = str(e)
        print(f"WSGI: Could not import main app: {e}")
        
        try:
            # Try the your_application factory
            from your_application import create_app
            app = create_app()
            print("WSGI: Successfully created application from your_application factory")
            return app
        except ImportError as e2:
            factory_error = str(e2)
            print(f"WSGI: Could not import your_application: {e2}")
            
            # Create a minimal Flask app as fallback
            try:
                from flask import Flask
                app = Flask(__name__)
                
                @app.route('/')
                def status():
                    return f"""
                    <h1>SmartFee Application Status</h1>
                    <p><strong>Status:</strong> Running with minimal configuration</p>
                    <p><strong>Main app error:</strong> {main_error}</p>
                    <p><strong>Factory error:</strong> {factory_error}</p>
                    <p><strong>Solution:</strong> Install missing dependencies or check application structure</p>
                    <hr>
                    <p><em>This is a fallback page. The full application is not available.</em></p>
                    """
                
                @app.route('/health')
                def health():
                    return {'status': 'minimal', 'message': 'Fallback app running'}
                
                print("WSGI: Created minimal fallback Flask application")
                return app
                
            except ImportError:
                # If even Flask is not available, return None
                print("WSGI: CRITICAL - Flask is not available")
                return None

# Create the application instance
application = create_application()

if application is None:
    # Last resort - create a WSGI callable that returns an error
    def application(environ, start_response):
        status = '500 Internal Server Error'
        headers = [('Content-type', 'text/html')]
        start_response(status, headers)
        return [b'<h1>Critical Error</h1><p>Flask is not installed or available.</p>']

if __name__ == "__main__":
    if application and hasattr(application, 'run'):
        port = int(os.environ.get("PORT", 5000))
        application.run(host='0.0.0.0', port=port, debug=os.environ.get('FLASK_DEBUG', '0') == '1')
    else:
        print("Cannot run application - Flask not available")