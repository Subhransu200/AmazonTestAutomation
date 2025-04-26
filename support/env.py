import os
from dotenv import load_dotenv
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

# Load environment variables
load_dotenv()

def before_all(context):
    # Setup Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-notifications')
    
    # Add any additional options from environment variables
    if os.getenv('HEADLESS') == 'true':
        chrome_options.add_argument('--headless')
    
    if os.getenv('NO_SANDBOX') == 'true':
        chrome_options.add_argument('--no-sandbox')
    
    # Initialize the driver
    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    context.driver.implicitly_wait(int(os.getenv('IMPLICIT_WAIT', '10')))
    context.action_chains = webdriver.ActionChains(context.driver)

def after_all(context):
    if hasattr(context, 'driver'):
        context.driver.quit()

def before_scenario(context, scenario):
    # Clear cookies before each scenario
    if hasattr(context, 'driver'):
        context.driver.delete_all_cookies()
    
    # Set up any scenario-specific configurations
    if 'mobile' in scenario.tags:
        context.driver.set_window_size(375, 812)  # iPhone X dimensions
    else:
        context.driver.maximize_window()

def after_scenario(context, scenario):
    # Take screenshot on failure
    if scenario.status == 'failed' and hasattr(context, 'driver'):
        screenshot_dir = os.getenv('SCREENSHOT_DIR', 'reports/screenshots')
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(
            screenshot_dir,
            f"failure_{scenario.name}_{time.strftime('%Y%m%d_%H%M%S')}.png"
        )
        context.driver.save_screenshot(screenshot_path) 