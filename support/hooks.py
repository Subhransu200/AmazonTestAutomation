from behave import before, after
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

@before.all
def before_all(context):
    # Setup Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-notifications')
    
    # Initialize the driver
    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    context.driver.implicitly_wait(10)
    context.action_chains = webdriver.ActionChains(context.driver)

@after.all
def after_all(context):
    if hasattr(context, 'driver'):
        context.driver.quit()

@before.each
def before_each(context):
    # Clear cookies before each test
    if hasattr(context, 'driver'):
        context.driver.delete_all_cookies()

@after.each
def after_each(context):
    # Take screenshot on failure
    if context.failed and hasattr(context, 'driver'):
        context.driver.save_screenshot(f"failure_{time.strftime('%Y%m%d_%H%M%S')}.png") 