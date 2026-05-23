#!/bin/bash

# Run for Android Termux

echo ""
echo "🔒 Security Audit Platform - Android Termux Launcher"
echo ""

# Navigate to app directory
cd "$HOME/security-audit/security-audit" 2>/dev/null || cd "./security-audit"

# Activate environment
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
else
    echo "[!] Virtual environment not found. Please run: bash android/install.sh"
    exit 1
fi

# Set variables for Termux
export FLASK_APP=backend/app.py
export FLASK_ENV=development
export FLASK_DEBUG=True
export PYTHONUNBUFFERED=1

# Run Flask
echo "[*] Starting server..."
echo ""
echo "╔═══════════════════════════════════════════════════════╗"
echo "║  🔒 PROFESSIONAL SECURITY AUDIT SYSTEM               ║"
echo "║     Running on Android Termux                         ║"
echo "╠═══════════════════════════════════════════════════════╣"
echo "║                                                       ║"
echo "║  🌐 Access: http://localhost:5000                    ║"
echo "║  🔐 Defender: KAIHAAN AFGHAN                         ║"
echo "║  ⚙️  Status: RED LINE ACTIVE                         ║"
echo "║                                                       ║"
echo "║  Press Ctrl+C to stop                                ║"
echo "║                                                       ║"
echo "╚═══════════════════════════════════════════════════════╝"
echo ""

python backend/app.py
