"""Main Flask Application for Security Audit Platform"""

from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import sys
from datetime import datetime

# Add backend to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import get_config
from scanner import VulnerabilityScanner
from exploit_analyzer import ExploitAnalyzer
from report_generator import ReportGenerator
from auth import audit_logger

# Initialize Flask
app = Flask(__name__, template_folder='../frontend', static_folder='../frontend')
config = get_config()
app.config.from_object(config)

# Enable CORS
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Initialize security tools
scanner = VulnerabilityScanner()
exploit_analyzer = ExploitAnalyzer()
report_generator = ReportGenerator()

# Routes
@app.route('/')
def index():
    """Main dashboard"""
    try:
        return send_from_directory('../frontend', 'index.html')
    except:
        return jsonify({'error': 'Frontend not found'}), 404

@app.route('/api/dashboard')
def get_dashboard():
    """Get dashboard data"""
    return jsonify({
        "system_status": "OPERATIONAL",
        "defender": config.DEFENDER_NAME,
        "status": config.DEFENDER_STATUS,
        "mission": config.MISSION,
        "principle": config.PRINCIPLE,
        "location": config.DEFENDER_LOCATION,
        "badges": config.DEFENDER_BADGES,
        "timestamp": datetime.now().isoformat()
    }), 200

@app.route('/api/scan', methods=['POST'])
def start_scan():
    """Start vulnerability scan"""
    try:
        data = request.get_json()
        target = data.get('target')
        scan_type = data.get('scan_type', 'full')
        
        if not target:
            return jsonify({'error': 'Target required'}), 400
        
        # Verify authorization
        if not data.get('authorized'):
            return jsonify({'error': 'Authorization required'}), 403
        
        audit_logger.log_activity(
            "scan_initiated",
            f"Target: {target}, Type: {scan_type}"
        )
        
        # Run scan
        vulnerabilities = scanner.scan_vulnerabilities(target, scan_type)
        
        # Analyze exploits
        exploit_chains = exploit_analyzer.analyze_exploit_chain(vulnerabilities)
        attack_paths = exploit_analyzer.get_attack_paths(vulnerabilities)
        impact = exploit_analyzer.analyze_impact(vulnerabilities)
        
        return jsonify({
            "status": "success",
            "vulnerabilities": vulnerabilities,
            "exploit_chains": exploit_chains,
            "attack_paths": attack_paths,
            "impact_analysis": impact,
            "timestamp": datetime.now().isoformat()
        }), 200
    
    except Exception as e:
        audit_logger.log_activity(
            "scan_error",
            f"Error: {str(e)}"
        )
        return jsonify({'error': str(e)}), 500

@app.route('/api/generate-report', methods=['POST'])
def generate_report():
    """Generate security report"""
    try:
        data = request.get_json()
        target = data.get('target')
        vulnerabilities = data.get('vulnerabilities', [])
        exploit_chains = data.get('exploit_chains', [])
        impact = data.get('impact_analysis', {})
        
        # Generate report
        report = report_generator.generate_report(
            target,
            vulnerabilities,
            exploit_chains,
            impact
        )
        
        audit_logger.log_activity(
            "report_generated",
            f"Report ID: {report['report_id']}"
        )
        
        return jsonify(report), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/vulnerability/<severity>', methods=['GET'])
def get_vulnerabilities_by_severity(severity):
    """Get vulnerabilities by severity"""
    filtered = [v for v in scanner.vulnerabilities if v.get('severity') == severity]
    return jsonify({
        "severity": severity,
        "count": len(filtered),
        "vulnerabilities": filtered
    }), 200

@app.route('/api/logs')
def get_logs():
    """Get activity logs"""
    try:
        with open('logs/activity.log', 'r') as f:
            logs = f.readlines()[-50:]  # Last 50 entries
        return jsonify({"logs": logs}), 200
    except:
        return jsonify({"logs": []}), 200

@app.route('/api/compliance')
def get_compliance():
    """Get compliance information"""
    return jsonify({
        "frameworks": [
            "OWASP Top 10",
            "CWE (Common Weakness Enumeration)",
            "CVE (Common Vulnerabilities and Exposures)",
            "CVSS (Common Vulnerability Scoring System)",
            "GDPR",
            "PCI DSS"
        ],
        "standards": "ISO 27001, NIST, SOC2"
    }), 200

@app.route('/api/health')
def health_check():
    """Health check"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "defender": config.DEFENDER_NAME,
        "mission": config.MISSION
    }), 200

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    audit_logger.log_activity('error', str(error))
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Create necessary directories
    os.makedirs('logs', exist_ok=True)
    os.makedirs('reports', exist_ok=True)
    os.makedirs('data', exist_ok=True)
    
    port = config.API_PORT
    
    print("""
    ╔═══════════════════════════════════════════════════════╗
    ║  🔒 PROFESSIONAL SECURITY AUDIT SYSTEM               ║
    ║     AI-Powered Vulnerability Assessment              ║
    ║     For Authorized Testing & Defense                 ║
    ╠═══════════════════════════════════════════════════════╣
    ║                                                       ║
    ║  🎓 Authorized Personnel Only                        ║
    ║  🔐 Defender: KAIHAAN AFGHAN                         ║
    ║  ⚙️  Status: RED LINE ACTIVE                         ║
    ║                                                       ║
    ║  Starting on port {port}...                          ║
    ║  Access: http://localhost:{port}                     ║
    ║                                                       ║
    ║  🕊️ PEACE FOR THE INNOCENT                          ║
    ║  ⚖️ ILLEGAL IS ILLEGAL                              ║
    ║                                                       ║
    ╚═══════════════════════════════════════════════════════╝
    """)
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=config.DEBUG,
        use_reloader=config.DEBUG
    )
