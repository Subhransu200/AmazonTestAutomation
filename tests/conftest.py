import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import os
from datetime import datetime
from utils.logger import setup_logger

# Setup logger
logger = setup_logger()

@pytest.fixture(scope="session")
def browser():
    """Fixture to setup and teardown the browser"""
    logger.info("Setting up browser")
    chrome_options = Options()
    
    # Basic Chrome options
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--remote-allow-origins=*")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--ignore-certificate-errors")
    
    # Disable automation info bars and indicators
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_experimental_option('prefs', {
        "profile.default_content_settings.popups": 0,
        "download.default_directory": os.path.join(os.getcwd(), "downloads"),
        "download.prompt_for_download": False,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "autofill.profile_enabled": False,
        # Disable save password popup
        "profile.password_manager_enabled": False,
        # Disable infobar animations
        "disable-popup-blocking": True,
        "disable-infobars": True,
        # Disable the "Chrome is being controlled by automated test software" infobar
        "useAutomationExtension": False,
        "credentials_enable_service": False
    })
    
    # Create a new user data directory for testing
    user_data_dir = os.path.join(os.getcwd(), "chrome_test_profile")
    os.makedirs(user_data_dir, exist_ok=True)
    chrome_options.add_argument(f"user-data-dir={user_data_dir}")
    
    # Add headless mode if needed
    if os.getenv("HEADLESS", "false").lower() == "true":
        chrome_options.add_argument("--headless=new")
    
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.set_page_load_timeout(30)
        
        # Execute CDP command to disable automation
        driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
            'source': '''
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                })
            '''
        })
        
        logger.info("Chrome browser started successfully")
        yield driver
    except Exception as e:
        logger.error(f"Failed to start Chrome browser: {str(e)}")
        raise
    finally:
        try:
            driver.quit()
            logger.info("Chrome browser closed successfully")
        except:
            pass

@pytest.fixture(scope="function")
def take_screenshot(browser, request):
    """Fixture to take screenshot on test failure"""
    yield
    
    if request.node.rep_call.failed:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_dir = os.path.join("reports", "screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)
        
        screenshot_path = os.path.join(screenshot_dir, f"{request.node.name}_{timestamp}.png")
        browser.save_screenshot(screenshot_path)
        logger.info(f"Screenshot saved: {screenshot_path}") 