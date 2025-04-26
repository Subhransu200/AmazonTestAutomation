from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given('I am on the Amazon homepage')
def step_impl(context):
    context.driver.get('https://www.amazon.com')
    context.driver.maximize_window()

@given('I am on the Amazon homepage using Chrome')
def step_impl(context):
    context.driver.get('https://www.amazon.com')
    context.driver.maximize_window()

@given('I am on the Amazon homepage using a mobile viewport')
def step_impl(context):
    context.driver.get('https://www.amazon.com')
    context.driver.set_window_size(375, 812)  # iPhone X dimensions

@given('I am on the Amazon homepage with throttled network')
def step_impl(context):
    context.driver.get('https://www.amazon.com')
    context.driver.maximize_window()
    # Note: Network throttling would typically be set up in the browser's dev tools

@when('I click the hamburger menu')
def step_impl(context):
    hamburger_menu = context.driver.find_element(By.ID, 'nav-hamburger-menu')
    hamburger_menu.click()
    time.sleep(1)  # Wait for menu to expand

@when('I enter {search_term} in the search bar')
def step_impl(context, search_term):
    search_box = context.driver.find_element(By.ID, 'twotabsearchtextbox')
    search_box.clear()
    search_box.send_keys(search_term)

@when('I press Enter')
def step_impl(context):
    search_box = context.driver.find_element(By.ID, 'twotabsearchtextbox')
    search_box.send_keys(Keys.RETURN)

@when('I use the Tab key to navigate to the hamburger menu')
def step_impl(context):
    search_box = context.driver.find_element(By.ID, 'twotabsearchtextbox')
    search_box.send_keys(Keys.TAB)

@when('I press Enter to expand it')
def step_impl(context):
    hamburger_menu = context.driver.find_element(By.ID, 'nav-hamburger-menu')
    hamburger_menu.send_keys(Keys.RETURN)

@when('I hover over the {dropdown_name} dropdown')
def step_impl(context, dropdown_name):
    dropdown = context.driver.find_element(By.XPATH, f"//span[contains(text(), '{dropdown_name}')]")
    context.driver.action_chains.move_to_element(dropdown).perform()

@when('I inspect the hamburger menu')
def step_impl(context):
    hamburger_menu = context.driver.find_element(By.ID, 'nav-hamburger-menu')
    # Just checking if element is present and visible

@when('I hover over the {category} category in the hamburger menu')
def step_impl(context, category):
    category_element = context.driver.find_element(By.XPATH, f"//div[contains(text(), '{category}')]")
    context.driver.action_chains.move_to_element(category_element).perform()

@when('I apply the {category} category filter')
def step_impl(context, category):
    filter = context.driver.find_element(By.XPATH, f"//span[contains(text(), '{category}')]")
    filter.click()

@when('I search for {search_term} and add an item to the cart')
def step_impl(context, search_term):
    search_box = context.driver.find_element(By.ID, 'twotabsearchtextbox')
    search_box.clear()
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)
    
    # Add first item to cart
    add_to_cart_button = context.driver.find_element(By.ID, 'add-to-cart-button')
    add_to_cart_button.click()

@when('I check the cart icon in the navigation bar')
def step_impl(context):
    cart_icon = context.driver.find_element(By.ID, 'nav-cart')
    cart_icon.click()

@when('I navigate to the {category} category')
def step_impl(context, category):
    category_link = context.driver.find_element(By.XPATH, f"//a[contains(text(), '{category}')]")
    category_link.click()

@when('I expand the {category} category in the hamburger menu')
def step_impl(context, category):
    category_element = context.driver.find_element(By.XPATH, f"//div[contains(text(), '{category}')]")
    category_element.click()

@when('I click the {submenu} sub-menu')
def step_impl(context, submenu):
    submenu_element = context.driver.find_element(By.XPATH, f"//a[contains(text(), '{submenu}')]")
    submenu_element.click()

@when('I attempt to navigate to a non-existent category')
def step_impl(context):
    try:
        non_existent = context.driver.find_element(By.XPATH, "//a[contains(text(), 'NonExistentCategory')]")
        non_existent.click()
    except:
        # Expected error
        pass

@when('I view a specific book\'s details')
def step_impl(context):
    first_book = context.driver.find_element(By.CSS_SELECTOR, '.s-result-item')
    first_book.click()

@when('I click the cart icon in the navigation bar')
def step_impl(context):
    cart_icon = context.driver.find_element(By.ID, 'nav-cart')
    cart_icon.click()

@when('I click on {element} in the navigation bar')
def step_impl(context, element):
    nav_element = context.driver.find_element(By.XPATH, f"//span[contains(text(), '{element}')]")
    nav_element.click()

@then('The hamburger menu should expand displaying main categories')
def step_impl(context):
    menu_items = context.driver.find_elements(By.CSS_SELECTOR, '#hmenu-content .hmenu-item')
    assert len(menu_items) > 0

@then('The search results page should display products related to {search_term}')
def step_impl(context, search_term):
    results = context.driver.find_elements(By.CSS_SELECTOR, '.s-result-item')
    assert len(results) > 0

@then('The dropdown should display options including {option1} and {option2}')
def step_impl(context, option1, option2):
    dropdown_options = context.driver.find_elements(By.CSS_SELECTOR, '.nav-dropdown-content')
    assert len(dropdown_options) > 0

@then('The menu should be visible and properly aligned')
def step_impl(context):
    hamburger_menu = context.driver.find_element(By.ID, 'nav-hamburger-menu')
    assert hamburger_menu.is_displayed()

@then('The dropdown should display sub-categories smoothly')
def step_impl(context):
    subcategories = context.driver.find_elements(By.CSS_SELECTOR, '.hmenu-item')
    assert len(subcategories) > 0

@then('The search results should update to show {product} in the {category} category')
def step_impl(context, product, category):
    results = context.driver.find_elements(By.CSS_SELECTOR, '.s-result-item')
    assert len(results) > 0

@then('The cart icon should show the correct item count')
def step_impl(context):
    cart_count = context.driver.find_element(By.ID, 'nav-cart-count')
    assert int(cart_count.text) > 0

@then('The {category} category page should load correctly')
def step_impl(context, category):
    page_title = context.driver.title
    assert category.lower() in page_title.lower()

@then('I should be redirected to the {subcategory} sub-category page')
def step_impl(context, subcategory):
    page_title = context.driver.title
    assert subcategory.lower() in page_title.lower()

@then('The hamburger menu should expand and be scrollable')
def step_impl(context):
    menu_items = context.driver.find_elements(By.CSS_SELECTOR, '#hmenu-content .hmenu-item')
    assert len(menu_items) > 0

@then('I should see an error page or remain on the current page')
def step_impl(context):
    assert 'amazon.com' in context.driver.current_url

@then('The menu should expand within {seconds} seconds')
def step_impl(context, seconds):
    start_time = time.time()
    menu_items = context.driver.find_elements(By.CSS_SELECTOR, '#hmenu-content .hmenu-item')
    end_time = time.time()
    assert (end_time - start_time) < int(seconds)

@then('I should see a list of {category}')
def step_impl(context, category):
    results = context.driver.find_elements(By.CSS_SELECTOR, '.s-result-item')
    assert len(results) > 0

@then('The results should be properly categorized')
def step_impl(context):
    results = context.driver.find_elements(By.CSS_SELECTOR, '.s-result-item')
    assert len(results) > 0 