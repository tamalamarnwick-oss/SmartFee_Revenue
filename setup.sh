#!/bin/bash
# setup.sh - Setup script for SmartFee Revenue Collection

echo "Starting setup..."

# Install Python dependencies
pip install -r requirements.txt

# Set environment variables
export FLASK_APP=app.py
export FLASK_ENV=production

# Initialize the database
python init_db.py

echo "Setup complete!"
