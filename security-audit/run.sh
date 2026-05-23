#!/bin/bash

# Professional Security Audit Platform - Run Script

echo ""
echo "╔═══════════════════════════════════════════════════════╗"
echo "║  🔒 PROFESSIONAL SECURITY AUDIT SYSTEM               ║"
echo "║     Launching...                                      ║"
echo "╚═══════════════════════════════════════════════════════╝"
echo ""

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "[!] Virtual environment not found. Running setup..."
    bash setup.sh
fi

# Activate venv
source venv/bin/activate

# Set environment variables
export FLASK_APP=backend/app.py
export FLASK_ENV=development
export FLASK_DEBUG=True

# Run application
echo "[*] Starting Security Audit Platform..."
echo ""
echo "🌐 Access at: http://localhost:5000"
echo "🔐 Press Ctrl+C to stop"
echo ""

python backend/app.py
