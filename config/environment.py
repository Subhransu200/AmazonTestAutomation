import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Environment:
    # Browser Configuration
    BROWSER = os.getenv("BROWSER", "chrome").lower()
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "10"))
    
    # Chrome Profile Configuration
    USE_CHROME_PROFILE = os.getenv("USE_CHROME_PROFILE", "true").lower() == "true"
    CHROME_PROFILE_NAME = os.getenv("CHROME_PROFILE_NAME", "Default")
    
    # Application URLs
    BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")
    API_URL = os.getenv("API_URL", "https://api.example.com")
    
    # Test Data
    TEST_USER = os.getenv("TEST_USER", "standard_user")
    TEST_PASSWORD = os.getenv("TEST_PASSWORD", "secret_sauce")
    
    # Reporting
    REPORT_DIR = os.getenv("REPORT_DIR", "reports")
    SCREENSHOT_DIR = os.path.join(REPORT_DIR, "screenshots")
    
    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_DIR = os.getenv("LOG_DIR", "logs")
    
    # Test Execution
    PARALLEL = os.getenv("PARALLEL", "false").lower() == "true"
    THREADS = int(os.getenv("THREADS", "1"))
    
    @classmethod
    def setup_directories(cls):
        """Create necessary directories if they don't exist"""
        directories = [
            cls.REPORT_DIR,
            cls.SCREENSHOT_DIR,
            cls.LOG_DIR
        ]
        
        for directory in directories:
            os.makedirs(directory, exist_ok=True) 