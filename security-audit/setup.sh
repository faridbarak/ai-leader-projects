#!/bin/bash

# Professional Security Audit Platform - Setup Script
# For Android Termux & Desktop Linux

echo ""
echo "╔═══════════════════════════════════════════════════════╗"
echo "║  🔒 PROFESSIONAL SECURITY AUDIT SYSTEM               ║"
echo "║     Setup Script                                      ║"
echo "╚═══════════════════════════════════════════════════════╝"
echo ""

# Check Python
echo "[*] Checking Python installation..."
python3 --version
if [ $? -ne 0 ]; then
    echo "[!] Python 3 not found"
    exit 1
fi

# Create virtual environment
echo "[*] Creating virtual environment..."
python3 -m venv venv

# Activate
echo "[*] Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "[*] Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "[*] Installing dependencies..."
pip install -r backend/requirements.txt

# Create directories
echo "[*] Creating necessary directories..."
mkdir -p logs data reports

# Create sample data
echo "[*] Creating sample data files..."
cat > data/cve_database.json << 'EOF'
{}
EOF

cat > data/cwe_mapping.json << 'EOF'
{}
EOF

cat > data/exploits.json << 'EOF'
{}
EOF

# Create .env file
echo "[*] Creating .env file..."
if [ ! -f .env ]; then
    cp .env.example .env 2>/dev/null || cat > .env << 'EOF'
FLASK_ENV=development
FLASK_DEBUG=True
API_PORT=5000
EOF
fi

echo ""
echo "[✓] Setup complete!"
echo ""
echo "Next steps:"
echo "  1. source venv/bin/activate"
echo "  2. python backend/app.py"
echo "  3. Open browser: http://localhost:5000"
echo ""
echo "🕊️ PEACE FOR THE INNOCENT"
echo "⚖️ ILLEGAL IS ILLEGAL"
echo "🔴 RED LINE DEFENDER"
echo ""
