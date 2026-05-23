"""Audit Logging System"""

import logging
import json
from datetime import datetime
import os
from functools import wraps

# Create logs directory
os.makedirs('logs', exist_ok=True)

class AuditLogger:
    """Comprehensive audit logging"""
    
    def __init__(self):
        # Main activity logger
        self.activity_logger = self._setup_logger(
            'activity',
            'logs/activity.log'
        )
        # Scan logger
        self.scan_logger = self._setup_logger(
            'scan',
            'logs/scans.log'
        )
        # Vulnerability logger
        self.vuln_logger = self._setup_logger(
            'vulnerability',
            'logs/vulnerabilities.log'
        )
    
    def _setup_logger(self, name, log_file):
        """Setup logger with file handler"""
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        
        # File handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s | %(name)s | %(levelname)s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        return logger
    
    def log_activity(self, action, details, user="system"):
        """Log activity"""
        message = f"User: {user} | Action: {action} | Details: {details}"
        self.activity_logger.info(message)
    
    def log_scan(self, scan_type, target, result, status):
        """Log scan activity"""
        message = f"Scan: {scan_type} | Target: {target} | Status: {status} | Result: {result}"
        self.scan_logger.info(message)
    
    def log_vulnerability(self, vuln_type, severity, target, details):
        """Log found vulnerability"""
        message = f"Type: {vuln_type} | Severity: {severity} | Target: {target} | Details: {details}"
        self.vuln_logger.warning(message)
    
    def log_exploit_attempt(self, exploit_type, target, success, details):
        """Log exploit analysis"""
        status = "SUCCESS" if success else "BLOCKED"
        message = f"Exploit: {exploit_type} | Target: {target} | Status: {status} | Details: {details}"
        self.vuln_logger.warning(message)

# Global logger instance
audit_logger = AuditLogger()

def audit_action(action_name):
    """Decorator to audit actions"""
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            try:
                result = f(*args, **kwargs)
                audit_logger.log_activity(
                    action_name,
                    f"Success: {str(result)[:100]}"
                )
                return result
            except Exception as e:
                audit_logger.log_activity(
                    action_name,
                    f"Error: {str(e)}"
                )
                raise
        return wrapped
    return decorator
