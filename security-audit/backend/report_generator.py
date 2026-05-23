"""Professional Report Generator"""

import json
from datetime import datetime
from auth import audit_logger

class ReportGenerator:
    """Generate professional security audit reports"""
    
    def __init__(self):
        self.reports = []
    
    def generate_report(self, target, vulnerabilities, exploit_chains, impact_analysis):
        """Generate comprehensive security audit report"""
        
        report = {
            "report_id": self._generate_report_id(),
            "target": target,
            "timestamp": datetime.now().isoformat(),
            "executive_summary": self._create_executive_summary(vulnerabilities, impact_analysis),
            "vulnerability_details": self._create_vuln_details(vulnerabilities),
            "exploit_analysis": self._create_exploit_section(exploit_chains),
            "risk_assessment": self._create_risk_assessment(vulnerabilities),
            "remediation_recommendations": self._create_remediation(vulnerabilities),
            "timeline": self._create_timeline(vulnerabilities),
            "compliance_mapping": self._create_compliance_mapping(vulnerabilities),
            "defender_info": self._create_defender_info()
        }
        
        self.reports.append(report)
        audit_logger.log_activity(
            "report_generated",
            f"Report: {report['report_id']}, Target: {target}, Vulnerabilities: {len(vulnerabilities)}"
        )
        
        return report
    
    def _generate_report_id(self):
        """Generate unique report ID"""
        return f"RPT-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    def _create_executive_summary(self, vulnerabilities, impact):
        """Create executive summary"""
        critical = len([v for v in vulnerabilities if v.get('severity') == 'Critical'])
        high = len([v for v in vulnerabilities if v.get('severity') == 'High'])
        
        return {
            "overview": f"Security audit identified {len(vulnerabilities)} vulnerabilities",
            "critical_vulns": critical,
            "high_vulns": high,
            "medium_vulns": len([v for v in vulnerabilities if v.get('severity') == 'Medium']),
            "low_vulns": len([v for v in vulnerabilities if v.get('severity') == 'Low']),
            "overall_risk": "Critical" if critical > 0 else ("High" if high > 0 else "Medium"),
            "key_findings": [
                f"Found {critical} critical vulnerabilities requiring immediate attention",
                f"Found {high} high-severity vulnerabilities",
                "Recommend immediate patching of critical issues",
                "Implement security monitoring and WAF"
            ]
        }
    
    def _create_vuln_details(self, vulnerabilities):
        """Create detailed vulnerability section"""
        details = []
        
        for i, vuln in enumerate(vulnerabilities, 1):
            detail = {
                "id": i,
                "type": vuln.get('type', 'Unknown'),
                "severity": vuln.get('severity', 'Unknown'),
                "cvss_score": vuln.get('cvss_score', 0),
                "cve": vuln.get('cve', 'N/A'),
                "cwe": vuln.get('cwe', 'N/A'),
                "description": vuln.get('description', 'N/A'),
                "weakness": vuln.get('weakness', 'N/A'),
                "affected_component": vuln.get('target', 'N/A'),
                "discovery_method": "Automated Scanning",
                "confidence": "High",
                "exploitability": self._calculate_exploitability(vuln),
                "impact_potential": self._calculate_impact(vuln),
                "remediation": vuln.get('remediation', ["See remediation section"])
            }
            details.append(detail)
        
        return details
    
    def _create_exploit_section(self, exploit_chains):
        """Create exploit analysis section"""
        return {
            "chains_found": len(exploit_chains),
            "chains": exploit_chains,
            "critical_paths": self._identify_critical_paths(exploit_chains),
            "attack_scenarios": self._create_attack_scenarios(exploit_chains)
        }
    
    def _create_risk_assessment(self, vulnerabilities):
        """Create risk assessment matrix"""
        critical_count = len([v for v in vulnerabilities if v.get('severity') == 'Critical'])
        
        return {
            "risk_level": "Critical" if critical_count > 0 else "High",
            "exposure_factors": [
                "Multiple critical vulnerabilities present",
                "Direct network exposure",
                "Authenticated and unauthenticated attack vectors",
                "Potential for privilege escalation"
            ],
            "business_impact": {
                "confidentiality": "High",
                "integrity": "High",
                "availability": "Medium",
                "financial_impact": "Critical"
            },
            "urgency": "IMMEDIATE"
        }
    
    def _create_remediation(self, vulnerabilities):
        """Create remediation recommendations"""
        remediation = {
            "immediate_actions": [
                "1. Patch all critical vulnerabilities",
                "2. Apply security updates",
                "3. Implement WAF rules",
                "4. Monitor for exploitation"
            ],
            "short_term": [
                "Deploy intrusion detection system",
                "Implement security monitoring",
                "Conduct security training",
                "Implement secure coding practices"
            ],
            "long_term": [
                "Establish vulnerability management program",
                "Implement continuous security monitoring",
                "Develop incident response plan",
                "Conduct regular security assessments"
            ],
            "detailed_remediation": self._get_detailed_remediation(vulnerabilities)
        }
        return remediation
    
    def _create_timeline(self, vulnerabilities):
        """Create patching timeline"""
        return {
            "critical": "Immediate (within 24 hours)",
            "high": "Within 1 week",
            "medium": "Within 2 weeks",
            "low": "Within 30 days",
            "verification": "Confirm fixes through re-testing"
        }
    
    def _create_compliance_mapping(self, vulnerabilities):
        """Map vulnerabilities to compliance frameworks"""
        return {
            "owasp_top_10": self._map_owasp(vulnerabilities),
            "cwe": self._map_cwe(vulnerabilities),
            "gdpr": "Impacts data protection requirements",
            "pci_dss": "Multiple PCI DSS requirements violated"
        }
    
    def _create_defender_info(self):
        """Add defender information to report"""
        return {
            "defender": "Kaihaan Afghan",
            "status": "RED LINE ACTIVE",
            "credentials": [
                "Google AI Leader Badge",
                "Microsoft Registered Defender",
                "HackerOne Researcher",
                "Bugcrowd Researcher"
            ],
            "mission": "PEACE FOR THE INNOCENT",
            "principle": "ILLEGAL IS ILLEGAL",
            "report_date": datetime.now().isoformat()
        }
    
    def _calculate_exploitability(self, vuln):
        """Calculate exploitability score"""
        severity_to_exploitability = {
            "Critical": "Very High",
            "High": "High",
            "Medium": "Medium",
            "Low": "Low"
        }
        return severity_to_exploitability.get(vuln.get('severity'), 'Unknown')
    
    def _calculate_impact(self, vuln):
        """Calculate potential impact"""
        return "System Compromise" if vuln.get('severity') in ['Critical', 'High'] else "Data Exposure"
    
    def _identify_critical_paths(self, exploit_chains):
        """Identify critical attack paths"""
        return [chain for chain in exploit_chains if 'Critical' in str(chain)]
    
    def _create_attack_scenarios(self, exploit_chains):
        """Create realistic attack scenarios"""
        return [
            {
                "scenario": "Scenario 1: Direct Web Application Attack",
                "description": "Attacker directly exploits web vulnerability to gain code execution",
                "likelihood": "High",
                "impact": "Critical"
            },
            {
                "scenario": "Scenario 2: Network-based Attack",
                "description": "Attacker exploits network service vulnerability for initial access",
                "likelihood": "Medium",
                "impact": "Critical"
            }
        ]
    
    def _map_owasp(self, vulnerabilities):
        """Map to OWASP Top 10"""
        return [
            "A1 - Broken Access Control",
            "A3 - Injection",
            "A5 - Cross-Site Scripting (XSS)",
            "A6 - Security Misconfiguration"
        ]
    
    def _map_cwe(self, vulnerabilities):
        """Map to CWE"""
        return [
            "CWE-89: Improper Neutralization of Special Elements",
            "CWE-79: Cross-site Scripting",
            "CWE-693: Protection Mechanism Failure"
        ]
    
    def _get_detailed_remediation(self, vulnerabilities):
        """Get detailed remediation for each vulnerability"""
        remediation = []
        for vuln in vulnerabilities:
            if 'remediation' in vuln:
                remediation.append({
                    "vulnerability": vuln.get('type'),
                    "steps": vuln['remediation']
                })
        return remediation
    
    def export_report(self, report_id, format="json"):
        """Export report in various formats"""
        report = next((r for r in self.reports if r['report_id'] == report_id), None)
        if not report:
            return None
        
        if format == "json":
            return json.dumps(report, indent=2, default=str)
        
        return report
