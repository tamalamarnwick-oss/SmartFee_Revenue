#!/bin/bash

# Exit on error
set -e

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Install gunicorn if not already installed
if ! command -v gunicorn &> /dev/null; then
    echo "Installing gunicorn..."
    pip install gunicorn
fi

# Initialize the database
echo "Initializing database..."
python init_db.py

# Run database migrations
echo "Running database migrations..."
python migrate_database.py

echo "Build completed successfully!"
