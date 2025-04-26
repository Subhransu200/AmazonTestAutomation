from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time

@given('I am on the Amazon homepage')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.amazon.in')
    context.driver.maximize_window()
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'nav-hamburger-menu'))
    )

@given('I am on the Amazon homepage using Chrome')
def step_impl(context):
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.get('https://www.amazon.in')
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'nav-hamburger-menu'))
    )

@when('I click the hamburger menu')
def step_impl(context):
    menu = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'nav-hamburger-menu'))
    )
    menu.click()

@when('I enter "{text}" in the search bar')
def step_impl(context, text):
    search_box = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'twotabsearchtextbox'))
    )
    search_box.clear()
    search_box.send_keys(text)

@when('I press Enter')
def step_impl(context):
    search_box = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'twotabsearchtextbox'))
    )
    search_box.send_keys(Keys.RETURN)

@when('I use the Tab key to navigate to the hamburger menu')
def step_impl(context):
    search_box = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'twotabsearchtextbox'))
    )
    search_box.send_keys(Keys.TAB)

@when('I press Enter to expand it')
def step_impl(context):
    menu = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'nav-hamburger-menu'))
    )
    menu.send_keys(Keys.RETURN)

@when('I hover over the "{dropdown}" dropdown')
def step_impl(context, dropdown):
    # First find the element
    element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'nav-link-accountList'))
    )
    # Then hover over it
    ActionChains(context.driver).move_to_element(element).perform()
    # Wait for dropdown to appear
    time.sleep(1)

@when('I inspect the hamburger menu')
def step_impl(context):
    menu = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'nav-hamburger-menu'))
    )
    context.menu = menu

@when('I hover over the "Departments" category in the hamburger menu')
def step_impl(context):
    menu = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'nav-hamburger-menu'))
    )
    menu.click()
    time.sleep(1)
    departments = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Departments')]"))
    )
    ActionChains(context.driver).move_to_element(departments).perform()

@when('I apply the "{category}" category filter')
def step_impl(context, category):
    filter_link = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//span[contains(text(), '{category}')]"))
    )
    filter_link.click()

@when('I search for "{product}" and add an item to the cart')
def step_impl(context, product):
    search_box = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'twotabsearchtextbox'))
    )
    search_box.clear()
    search_box.send_keys(product)
    search_box.send_keys(Keys.RETURN)
    first_item = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.s-result-item'))
    )
    first_item.click()
    add_to_cart = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'add-to-cart-button'))
    )
    add_to_cart.click()

@when('I check the cart icon in the navigation bar')
def step_impl(context):
    cart_icon = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'nav-cart'))
    )
    context.cart_icon = cart_icon

@when('I navigate to the "{category}" category')
def step_impl(context, category):
    menu = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'nav-hamburger-menu'))
    )
    menu.click()
    time.sleep(1)
    category_link = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(), '{category}')]"))
    )
    category_link.click()

@then('The hamburger menu should expand displaying main categories')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#hmenu-content .hmenu-item'))
    )

@then('The search results page should display products related to "{search_term}"')
def step_impl(context, search_term):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.s-result-item'))
    )

@then('The dropdown should display options including "{option1}" and "{option2}"')
def step_impl(context, option1, option2):
    # Wait for the dropdown menu to be visible
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'nav-flyout-accountList'))
    )
    # Verify the options are present
    assert option1 in context.driver.page_source
    assert option2 in context.driver.page_source

@then('The menu should be visible and properly aligned')
def step_impl(context):
    assert context.menu.is_displayed()
    assert context.menu.is_enabled()

@then('The dropdown should display sub-categories smoothly')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.hmenu-item'))
    )

@then('The search results should update to show {product} in the {category} category')
def step_impl(context, product, category):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.s-result-item'))
    )

@then('The cart icon should show the correct item count')
def step_impl(context):
    assert context.cart_icon.is_displayed()
    cart_count = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'nav-cart-count'))
    )
    assert int(cart_count.text) > 0

@then('The {category} category page should load correctly')
def step_impl(context, category):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//h1[contains(text(), '{category}')]"))
    )

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit() 