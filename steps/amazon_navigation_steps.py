from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver_factory import DriverFactory
from pages.amazon_page import AmazonPage
import time

@given('I am on the Amazon homepage')
def step_impl(context):
    context.driver = DriverFactory.get_driver()
    context.amazon = AmazonPage(context.driver)
    context.amazon.navigate_to_amazon()

@when('I click the hamburger menu')
def step_impl(context):
    context.amazon.click_hamburger_menu()

@then('The hamburger menu should expand displaying main categories')
def step_impl(context):
    assert context.amazon.is_menu_expanded(), "Hamburger menu did not expand"

@when('I click the "{category}" category from the hamburger menu')
def step_impl(context, category):
    context.amazon.navigate_to_category(category)

@then('I should be redirected to the {category} category page')
def step_impl(context, category):
    assert category.lower() in context.driver.title.lower(), f"Not on {category} page" 