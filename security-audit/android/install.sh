#!/bin/bash

# Professional Security Audit Platform - Android Termux Setup

echo ""
echo "╔════════════════════════════════════════════════════════╗"
echo "║  🔒 SECURITY AUDIT PLATFORM - ANDROID SETUP           ║"
echo "║     For Termux on Android                              ║"
echo "╚════════════════════════════════════════════════════════╝"
echo ""

echo "[*] Android Termux Environment Detected"
echo "[*] Installing Termux-specific dependencies..."
echo ""

# Update package manager
echo "[1] Updating package manager..."
pkg update && pkg upgrade -y

# Install Python
echo "[2] Installing Python 3..."
pkg install -y python3 python3-dev

# Install build tools
echo "[3] Installing build tools..."
pkg install -y clang make openssl openssl-dev

# Install Git
echo "[4] Installing Git..."
pkg install -y git

# Create working directory
echo "[5] Creating working directory..."
mkdir -p ~/security-audit
cd ~/security-audit

# Clone or setup repository
echo "[6] Setting up repository..."
if [ ! -d ".git" ]; then
    git clone https://github.com/faridbarak/ai-leader-projects.git . 2>/dev/null || echo "[!] Git clone skipped"
fi

# Setup Python environment
echo "[7] Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "[8] Installing Python dependencies..."
cd security-audit
pip install --upgrade pip
pip install -r backend/requirements.txt

echo ""
echo "[✓] Android Termux Setup Complete!"
echo ""
echo "To run the application:"
echo "  1. cd ~/security-audit/security-audit"
echo "  2. source venv/bin/activate"
echo "  3. python backend/app.py"
echo "  4. Open Termux browser at http://localhost:5000"
echo ""
echo "🔐 Defender: KAIHAAN AFGHAN"
echo "⚙️ Status: RED LINE ACTIVE"
echo ""
