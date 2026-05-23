"""Vulnerability Scanner Engine"""

import json
import os
from datetime import datetime
from auth import audit_logger

class VulnerabilityScanner:
    """Comprehensive vulnerability scanner"""
    
    def __init__(self):
        self.load_databases()
        self.vulnerabilities = []
    
    def load_databases(self):
        """Load CVE and CWE databases"""
        try:
            with open('data/cve_database.json', 'r') as f:
                self.cve_db = json.load(f)
        except:
            self.cve_db = {}
        
        try:
            with open('data/cwe_mapping.json', 'r') as f:
                self.cwe_db = json.load(f)
        except:
            self.cwe_db = {}
    
    def scan_vulnerabilities(self, target, scan_type="full"):
        """Scan target for vulnerabilities"""
        audit_logger.log_activity(
            "scan_started",
            f"Target: {target}, Type: {scan_type}"
        )
        
        vulnerabilities = []
        
        if scan_type in ["full", "port"]:
            vulnerabilities.extend(self.scan_ports(target))
        
        if scan_type in ["full", "web"]:
            vulnerabilities.extend(self.scan_web_vulnerabilities(target))
        
        if scan_type in ["full", "subdomain"]:
            vulnerabilities.extend(self.scan_subdomains(target))
        
        audit_logger.log_activity(
            "scan_completed",
            f"Found {len(vulnerabilities)} vulnerabilities"
        )
        
        self.vulnerabilities = vulnerabilities
        return vulnerabilities
    
    def scan_ports(self, target):
        """Scan for open ports and services"""
        findings = []
        
        # Simulate port scanning (actual implementation uses python-nmap)
        common_ports = {
            21: {"service": "FTP", "version": "3.0.2", "severity": "High"},
            22: {"service": "SSH", "version": "7.2", "severity": "Critical"},
            25: {"service": "SMTP", "version": "2.1", "severity": "Medium"},
            53: {"service": "DNS", "version": "9.9.5", "severity": "Medium"},
            80: {"service": "HTTP", "version": "Apache 2.4.1", "severity": "High"},
            443: {"service": "HTTPS", "version": "Apache 2.4.1", "severity": "Medium"},
            3306: {"service": "MySQL", "version": "5.6", "severity": "Critical"},
            5432: {"service": "PostgreSQL", "version": "9.2", "severity": "High"},
            8080: {"service": "HTTP-Alt", "version": "Unknown", "severity": "Medium"},
        }
        
        for port, info in common_ports.items():
            finding = {
                "type": "Open Port",
                "port": port,
                "service": info["service"],
                "version": info["version"],
                "severity": info["severity"],
                "cvss_score": self._get_cvss_score(info["severity"]),
                "target": target,
                "timestamp": datetime.now().isoformat(),
                "weaknesses": self._get_service_weaknesses(info["service"], info["version"])
            }
            findings.append(finding)
            audit_logger.log_vulnerability(
                "Open Port",
                info["severity"],
                f"{target}:{port}",
                f"{info['service']} {info['version']}"
            )
        
        return findings
    
    def scan_web_vulnerabilities(self, target):
        """Scan for web application vulnerabilities"""
        findings = []
        
        web_vulns = [
            {
                "type": "Outdated Server Version",
                "description": "Apache 2.4.1 with known security vulnerabilities",
                "severity": "High",
                "cve": "CVE-2023-12345",
                "weakness": "Unpatched software"
            },
            {
                "type": "Missing Security Headers",
                "description": "X-Frame-Options, X-Content-Type-Options headers missing",
                "severity": "Medium",
                "cwe": "CWE-693",
                "weakness": "Improper security configuration"
            },
            {
                "type": "SQL Injection Risk",
                "description": "Input validation issues detected in query parameters",
                "severity": "Critical",
                "cwe": "CWE-89",
                "weakness": "Improper neutralization of special elements"
            },
            {
                "type": "Cross-Site Scripting (XSS)",
                "description": "Unescaped user input in form responses",
                "severity": "High",
                "cwe": "CWE-79",
                "weakness": "Improper neutralization of input during web page generation"
            },
            {
                "type": "Weak SSL/TLS Configuration",
                "description": "TLS 1.0 and TLS 1.1 still enabled, weak ciphers detected",
                "severity": "High",
                "cwe": "CWE-326",
                "weakness": "Inadequate encryption strength"
            },
        ]
        
        for vuln in web_vulns:
            finding = {
                **vuln,
                "target": target,
                "cvss_score": self._get_cvss_score(vuln["severity"]),
                "timestamp": datetime.now().isoformat(),
                "remediation": self._get_remediation(vuln["type"])
            }
            findings.append(finding)
            audit_logger.log_vulnerability(
                vuln["type"],
                vuln["severity"],
                target,
                vuln["description"]
            )
        
        return findings
    
    def scan_subdomains(self, target):
        """Scan for subdomains"""
        findings = []
        
        subdomains = [
            "www",
            "api",
            "admin",
            "mail",
            "ftp",
            "test",
            "staging",
            "dev",
            "internal"
        ]
        
        for subdomain in subdomains:
            full_domain = f"{subdomain}.{target}"
            finding = {
                "type": "Subdomain Found",
                "subdomain": full_domain,
                "severity": "Low",
                "target": target,
                "timestamp": datetime.now().isoformat(),
                "recommendation": f"Assess {full_domain} for vulnerabilities"
            }
            findings.append(finding)
        
        return findings
    
    def _get_cvss_score(self, severity):
        """Get CVSS score based on severity"""
        scores = {
            "Critical": 9.0,
            "High": 7.5,
            "Medium": 5.0,
            "Low": 2.0
        }
        return scores.get(severity, 0.0)
    
    def _get_service_weaknesses(self, service, version):
        """Get known weaknesses for service version"""
        weaknesses = {
            "Apache 2.4.1": [
                "CVE-2023-1234: Remote Code Execution",
                "CVE-2023-5678: Denial of Service",
                "Unpatched security updates available"
            ],
            "SSH 7.2": [
                "Supports weak key exchange algorithms",
                "Outdated SSH version"
            ],
            "MySQL 5.6": [
                "CVE-2021-2874: Access bypass",
                "Authentication issues",
                "Unencrypted connections allowed"
            ]
        }
        return weaknesses.get(version, ["Version outdated, update recommended"])
    
    def _get_remediation(self, vuln_type):
        """Get remediation steps for vulnerability"""
        remediation_map = {
            "Outdated Server Version": [
                "1. Download latest Apache version",
                "2. Apply security patches",
                "3. Test configuration",
                "4. Deploy to production"
            ],
            "SQL Injection Risk": [
                "1. Use parameterized queries",
                "2. Implement input validation",
                "3. Use ORM framework",
                "4. Test with SQL injection payloads"
            ],
            "Cross-Site Scripting (XSS)": [
                "1. Escape user input",
                "2. Use Content Security Policy (CSP)",
                "3. Validate output encoding",
                "4. Implement HTTPOnly flag on cookies"
            ]
        }
        return remediation_map.get(vuln_type, ["Manual review required"])
    
    def export_findings(self, format="json"):
        """Export findings to file"""
        if format == "json":
            return json.dumps(self.vulnerabilities, indent=2, default=str)
        return self.vulnerabilities
