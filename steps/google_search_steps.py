from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver_factory import DriverFactory
import time

@given('I am on the Google homepage')
def step_impl(context):
    context.driver = DriverFactory.get_driver()
    context.driver.get("https://www.google.com")
    time.sleep(2)  # Wait for page to load

@when('I enter "{search_term}" in the search box')
def step_impl(context, search_term):
    search_box = context.driver.find_element(By.NAME, "q")
    search_box.send_keys(search_term)

@when('I click the search button')
def step_impl(context):
    search_box = context.driver.find_element(By.NAME, "q")
    search_box.submit()
    time.sleep(2)  # Wait for search results

@then('I should see search results containing "{search_term}"')
def step_impl(context, search_term):
    assert search_term in context.driver.title, f"Search results should contain {search_term}"
    context.driver.quit() 