import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com/")
    BROWSER = os.getenv("BROWSER", "chrome").lower()
    ENVIRONMENT = os.getenv("ENVIRONMENT", "qa")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO") 