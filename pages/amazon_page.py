from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.logger import setup_logger
import time
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, StaleElementReferenceException

class AmazonPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = setup_logger()
        self.url = "https://www.amazon.in/"
        
        # Locators
        self.search_box = (By.ID, "twotabsearchtextbox")
        self.search_button = (By.ID, "nav-search-submit-button")
        self.sign_in_button = (By.ID, "nav-link-accountList")
        self.cart_button = (By.ID, "nav-cart")
        self.orders_button = (By.ID, "nav-orders")
        
        # Navigation Menu Locators
        self.hamburger_menu = (By.ID, "nav-hamburger-menu")
        self.menu_content = (By.ID, "hmenu-content")
        self.menu_categories = (By.CSS_SELECTOR, "#hmenu-content .hmenu-item")
        self.electronics_category = (By.XPATH, "//div[contains(text(), 'Electronics')]")
        self.tv_video_submenu = (By.XPATH, "//a[contains(text(), 'TV & Video')]")
        self.account_lists = (By.ID, "nav-link-accountList")
        self.account_dropdown = (By.CSS_SELECTOR, "#nav-flyout-accountList")
        self.your_account_option = (By.XPATH, "//span[contains(text(), 'Your Account')]")
        self.sign_in_option = (By.XPATH, "//span[contains(text(), 'Sign In')]")
        
        # New Locators
        self.departments_category = (By.XPATH, "//div[contains(text(), 'Departments')]")
        self.category_filter = (By.CSS_SELECTOR, "#s-result-sort-select")
        self.cart_count = (By.ID, "nav-cart-count")
        self.add_to_cart_button = (By.ID, "add-to-cart-button")
        self.search_results = (By.CSS_SELECTOR, ".s-result-item")
        self.menu_overlay = (By.ID, "hmenu-canvas-background")
        
        self.category_locators = {
            "Electronics": [
                (By.XPATH, "//div[@id='hmenu-content']//div[contains(@class, 'hmenu-item') and normalize-space()='Electronics']"),
                (By.XPATH, "//div[@id='hmenu-content']//a[contains(@class, 'hmenu-item') and normalize-space()='Electronics']"),
                (By.XPATH, "//div[@id='hmenu-content']//div[contains(@class, 'hmenu-item')]//a[contains(text(), 'Electronics')]"),
                (By.CSS_SELECTOR, "#hmenu-content a.hmenu-item[href*='electronics']"),
                (By.LINK_TEXT, "Electronics")
            ],
            "Books": [
                (By.XPATH, "//div[@id='hmenu-content']//div[contains(@class, 'hmenu-item') and normalize-space()='Books']"),
                (By.XPATH, "//div[@id='hmenu-content']//a[contains(@class, 'hmenu-item') and normalize-space()='Books']"),
                (By.XPATH, "//div[@id='hmenu-content']//div[contains(@class, 'hmenu-item')]//a[contains(text(), 'Books')]"),
                (By.CSS_SELECTOR, "#hmenu-content a.hmenu-item[href*='books']"),
                (By.LINK_TEXT, "Books")
            ]
        }

    def navigate_to_amazon(self):
        """Navigate to Amazon.in"""
        self.logger.info("Navigating to Amazon.in")
        self.driver.get(self.url)
        
    def search_product(self, product_name):
        """Search for a product"""
        self.logger.info(f"Searching for product: {product_name}")
        self.enter_text(self.search_box, product_name)
        self.click_element(self.search_button)
        
    def go_to_cart(self):
        """Navigate to cart"""
        self.logger.info("Navigating to cart")
        self.click_element(self.cart_button)
        
    def go_to_orders(self):
        """Navigate to orders"""
        self.logger.info("Navigating to orders")
        self.click_element(self.orders_button)
        
    def go_to_sign_in(self):
        """Navigate to sign in page"""
        self.logger.info("Navigating to sign in page")
        self.click_element(self.sign_in_button)
        
    def click_hamburger_menu(self):
        """Click the hamburger menu and ensure it's fully expanded"""
        self.logger.info("Clicking hamburger menu")
        try:
            # Wait for hamburger menu to be clickable
            menu = self.wait.until(EC.element_to_be_clickable(self.hamburger_menu))
            
            # Try multiple times if needed
            max_attempts = 3
            for attempt in range(max_attempts):
                try:
                    menu.click()
                    break
                except (ElementClickInterceptedException, StaleElementReferenceException) as e:
                    if attempt == max_attempts - 1:
                        raise e
                    time.sleep(1)
            
            # Wait for menu content to be visible and stable
            self.wait.until(EC.visibility_of_element_located(self.menu_content))
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#hmenu-content .hmenu-item")))
            
            # Additional wait for menu animation and content loading
            time.sleep(3)
            
            return True
        except Exception as e:
            self.logger.error(f"Error clicking hamburger menu: {str(e)}")
            return False

    def is_menu_expanded(self):
        """Check if the hamburger menu is expanded"""
        return self.is_element_visible(self.menu_categories)
        
    def navigate_to_category(self, category):
        """Navigate to a specific category using multiple strategies"""
        self.logger.info(f"Navigating to category: {category}")
        
        # Ensure menu is open
        if not self.click_hamburger_menu():
            raise TimeoutException("Failed to open hamburger menu")
            
        # Wait for menu to be fully expanded
        if not self.wait_for_menu_overlay(True, 10):
            raise TimeoutException("Menu overlay did not appear")
            
        # Additional wait for dynamic content
        time.sleep(2)
        
        # Get list of locator strategies for the category
        locators = self.category_locators.get(category, [(By.LINK_TEXT, category)])
        
        # Try each locator strategy
        for locator in locators:
            try:
                self.logger.info(f"Trying locator strategy: {locator}")
                
                # First check if element exists
                elements = self.driver.find_elements(*locator)
                if not elements:
                    self.logger.warning(f"No elements found with locator: {locator}")
                    continue
                    
                # Try clicking each matching element until success
                for element in elements:
                    try:
                        # Scroll element into view
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                        time.sleep(1)  # Brief pause after scroll
                        
                        # Check if element is visible and clickable
                        if not element.is_displayed():
                            continue
                            
                        # Try clicking the element
                        try:
                            element.click()
                            return True
                        except:
                            self.driver.execute_script("arguments[0].click();", element)
                            return True
                            
                    except Exception as e:
                        self.logger.warning(f"Failed to click element: {str(e)}")
                        continue
                        
            except Exception as e:
                self.logger.error(f"Error with locator {locator}: {str(e)}")
                continue
        
        raise TimeoutException(f"Failed to click category {category} with all available locators")
        
    def navigate_to_subcategory(self, subcategory_name):
        """Navigate to a specific subcategory"""
        self.logger.info(f"Navigating to subcategory: {subcategory_name}")
        subcategory_locator = (By.XPATH, f"//a[contains(text(), '{subcategory_name}')]")
        self.click_element(subcategory_locator)
        
    def hover_over_account_lists(self):
        """Hover over Account & Lists dropdown"""
        self.logger.info("Hovering over Account & Lists")
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element(self.account_lists)).perform()
        
    def is_account_dropdown_visible(self):
        """Check if account dropdown is visible"""
        return self.is_element_visible(self.account_dropdown)
        
    def set_mobile_viewport(self):
        """Set viewport to mobile size"""
        self.driver.set_window_size(375, 812)  # iPhone X dimensions
        
    def navigate_with_keyboard(self):
        """Navigate to hamburger menu using keyboard"""
        self.logger.info("Navigating with keyboard")
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.TAB).perform()
        actions.send_keys(Keys.ENTER).perform()
        
    def verify_menu_alignment(self):
        """Verify menu alignment and visibility"""
        menu = self.find_element(self.hamburger_menu)
        return menu.is_displayed() and menu.is_enabled()
        
    def set_network_throttling(self):
        """Set network throttling for performance testing"""
        self.driver.execute_cdp_cmd('Network.enable', {})
        self.driver.execute_cdp_cmd('Network.emulateNetworkConditions', {
            'offline': False,
            'latency': 2000,  # 2 seconds
            'downloadThroughput': 780 * 1024 / 8,  # 780 Kbps
            'uploadThroughput': 330 * 1024 / 8,  # 330 Kbps
        })
        
    def enter_search_query(self, query):
        """Enter search query in the search box"""
        self.logger.info(f"Entering search query: {query}")
        self.enter_text(self.search_box, query)
        
    def submit_search(self):
        """Submit the search query"""
        self.logger.info("Submitting search query")
        self.click_element(self.search_button)
        
    def verify_search_results(self, query):
        """Verify search results contain the query"""
        self.logger.info(f"Verifying search results for: {query}")
        results = self.find_elements(self.search_results)
        return any(query.lower() in result.text.lower() for result in results)
        
    def apply_category_filter(self, category):
        """Apply category filter to search results"""
        self.logger.info(f"Applying category filter: {category}")
        filter_locator = (By.XPATH, f"//span[contains(text(), '{category}')]")
        self.click_element(filter_locator)
        
    def verify_filtered_results(self, product_type, category):
        """Verify filtered results match the category"""
        self.logger.info(f"Verifying filtered results for {product_type} in {category}")
        results = self.find_elements(self.search_results)
        return any(category.lower() in result.text.lower() for result in results)
        
    def search_and_add_to_cart(self, query):
        """Search for a product and add it to cart"""
        self.logger.info(f"Searching and adding to cart: {query}")
        self.enter_search_query(query)
        self.submit_search()
        # Click first result and add to cart
        first_result = (By.CSS_SELECTOR, ".s-result-item:first-child")
        self.click_element(first_result)
        self.click_element(self.add_to_cart_button)
        
    def check_cart_icon(self):
        """Check the cart icon in navigation bar"""
        self.logger.info("Checking cart icon")
        return self.is_element_visible(self.cart_count)
        
    def verify_cart_count(self):
        """Verify the cart count is correct"""
        self.logger.info("Verifying cart count")
        count_element = self.find_element(self.cart_count)
        return count_element.text.isdigit() and int(count_element.text) > 0
        
    def hover_over_departments(self):
        """Hover over Departments category"""
        self.logger.info("Hovering over Departments category")
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element(self.departments_category)).perform()
        
    def verify_departments_dropdown(self):
        """Verify departments dropdown is working properly"""
        self.logger.info("Verifying departments dropdown")
        # Check if subcategories are visible after hover
        subcategories = (By.CSS_SELECTOR, "#hmenu-content .hmenu-item")
        return self.is_element_visible(subcategories)

    def wait_for_menu_overlay(self, should_be_visible=True, timeout=10):
        """Wait for menu overlay to reach desired state"""
        try:
            if should_be_visible:
                # Wait for both the overlay and content
                self.wait.until(EC.visibility_of_element_located(self.menu_overlay))
                self.wait.until(EC.visibility_of_element_located(self.menu_content))
                
                # Wait for menu items to be present
                self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#hmenu-content .hmenu-item")))
                
                # Brief pause to ensure complete loading
                time.sleep(2)
            else:
                self.wait.until(EC.invisibility_of_element_located(self.menu_overlay))
            return True
        except TimeoutException:
            self.logger.warning(f"Menu overlay did not reach desired state (visible={should_be_visible}) within {timeout} seconds")
            return False
            
    def navigate_to_category(self, category):
        """Navigate to a specific category using multiple strategies"""
        self.logger.info(f"Navigating to category: {category}")
        
        # Ensure menu is open
        if not self.click_hamburger_menu():
            raise TimeoutException("Failed to open hamburger menu")
            
        # Wait for menu to be fully expanded
        if not self.wait_for_menu_overlay(True, 10):
            raise TimeoutException("Menu overlay did not appear")
            
        # Additional wait for dynamic content
        time.sleep(2)
        
        # Get list of locator strategies for the category
        locators = self.category_locators.get(category, [(By.LINK_TEXT, category)])
        
        # Try each locator strategy
        for locator in locators:
            try:
                self.logger.info(f"Trying locator strategy: {locator}")
                
                # First check if element exists
                elements = self.driver.find_elements(*locator)
                if not elements:
                    self.logger.warning(f"No elements found with locator: {locator}")
                    continue
                    
                # Try clicking each matching element until success
                for element in elements:
                    try:
                        # Scroll element into view
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                        time.sleep(1)  # Brief pause after scroll
                        
                        # Check if element is visible and clickable
                        if not element.is_displayed():
                            continue
                            
                        # Try clicking the element
                        try:
                            element.click()
                            return True
                        except:
                            self.driver.execute_script("arguments[0].click();", element)
                            return True
                            
                    except Exception as e:
                        self.logger.warning(f"Failed to click element: {str(e)}")
                        continue
                        
            except Exception as e:
                self.logger.error(f"Error with locator {locator}: {str(e)}")
                continue
        
        raise TimeoutException(f"Failed to click category {category} with all available locators") 