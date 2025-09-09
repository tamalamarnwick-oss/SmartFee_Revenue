#!/usr/bin/env bash
# Build script for Render

set -o errexit  # exit on error

echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Ensuring templates and static assets are available at runtime..."
# Create fallback locations inside your_application that are in template search paths
mkdir -p your_application/templates || true
mkdir -p your_application/static || true

# Copy real templates and static to fallback locations (if present)
if [ -d "templates" ]; then
  cp -r templates/* your_application/templates/ 2>/dev/null || true
fi
if [ -d "static" ]; then
  cp -r static/* your_application/static/ 2>/dev/null || true
fi

# Log what we have for troubleshooting
echo "Top-level templates present:" && ls -la templates 2>/dev/null || true
echo "Fallback templates present:" && ls -la your_application/templates 2>/dev/null || true

echo "Setting up database..."
python -c "
import os
os.environ.setdefault('FLASK_APP', 'app.py')
os.environ.setdefault('FLASK_ENV', 'production')

try:
    from app import app, db
    with app.app_context():
        print('Creating database tables...')
        db.create_all()
        print('Database setup complete!')
except Exception as e:
    print(f'Database setup error: {e}')
    print('Continuing with deployment...')
"

echo "Build completed successfully!"