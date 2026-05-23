# Security Audit Configuration

import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

class Config:
    """Base configuration"""
    
    # Flask
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    DEBUG = os.getenv('FLASK_DEBUG', False)
    API_PORT = int(os.getenv('API_PORT', 5000))
    
    # Security
    SECRET_KEY = os.getenv('SECRET_KEY', 'security-audit-key-change-in-production')
    
    # Audit Settings
    MAX_SCAN_TIMEOUT = int(os.getenv('MAX_SCAN_TIMEOUT', 300))
    LOG_ALL_ACTIVITIES = True
    REQUIRE_AUTHORIZATION = True
    
    # Database
    DB_PATH = 'data/audit.db'
    CVE_DATABASE = 'data/cve_database.json'
    CWE_DATABASE = 'data/cwe_mapping.json'
    EXPLOITS_DB = 'data/exploits.json'
    
    # Logging
    LOG_DIR = 'logs'
    LOG_FILE = 'logs/activity.log'
    SCAN_LOG = 'logs/scans.log'
    VULN_LOG = 'logs/vulnerabilities.log'
    
    # Reports
    REPORTS_DIR = 'reports'
    
    # CORS
    CORS_ORIGINS = ["*"]
    
    # Scanning
    ENABLE_PORT_SCAN = True
    ENABLE_SUBDOMAIN_SCAN = True
    ENABLE_VULNERABILITY_SCAN = True
    ENABLE_EXPLOIT_ANALYSIS = True
    
    # Defender Info
    DEFENDER_NAME = "Kaihaan Afghan"
    DEFENDER_STATUS = "RED LINE ACTIVE"
    DEFENDER_BADGES = [
        "Google AI Leader",
        "Google Security Expert",
        "Microsoft Defender",
        "HackerOne Researcher",
        "Bugcrowd Researcher"
    ]
    
    # Mission Statement
    MISSION = "PEACE FOR THE INNOCENT"
    PRINCIPLE = "ILLEGAL IS ILLEGAL"
    DEFENDER_LOCATION = "Afghanistan"

class DevelopmentConfig(Config):
    """Development config"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Production config"""
    DEBUG = False
    TESTING = False
    REQUIRE_AUTHORIZATION = True

class TestingConfig(Config):
    """Testing config"""
    DEBUG = True
    TESTING = True
    DB_PATH = ':memory:'

def get_config():
    """Get configuration based on environment"""
    env = os.getenv('FLASK_ENV', 'development')
    configs = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'testing': TestingConfig
    }
    return configs.get(env, DevelopmentConfig)
