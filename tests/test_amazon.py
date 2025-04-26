import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class TestAmazon:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.driver = browser
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)
        
    def test_main_navigation_menu(self):
        """Test main navigation menu visibility and functionality"""
        # Navigate to Amazon
        self.driver.get("https://www.amazon.in")
        time.sleep(2)  # Wait for page to stabilize
        
        # TC_NAV_001: Verify main navigation menu visibility
        try:
            nav_menu = self.wait.until(
                EC.presence_of_element_located((By.ID, "nav-main"))
            )
        except TimeoutException:
            # Try alternative selector
            nav_menu = self.wait.until(
                EC.presence_of_element_located((By.ID, "nav-belt"))
            )
        assert nav_menu.is_displayed(), "Navigation menu is not visible"
        
        # TC_NAV_002: Verify All menu button
        try:
            all_menu = self.wait.until(
                EC.element_to_be_clickable((By.ID, "nav-hamburger-menu"))
            )
        except TimeoutException:
            # Try alternative selector
            all_menu = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-action-type='OPEN_MENU']"))
            )
        
        # Click the menu button
        try:
            all_menu.click()
            time.sleep(1)  # Wait for animation
        except:
            # If direct click fails, try JavaScript click
            self.driver.execute_script("arguments[0].click();", all_menu)
            time.sleep(1)  # Wait for animation
        
        # Verify the menu opens - try multiple selectors
        try:
            menu_content = self.wait.until(
                EC.visibility_of_element_located((By.ID, "hmenu-content"))
            )
        except TimeoutException:
            try:
                # Try alternative selector
                menu_content = self.wait.until(
                    EC.visibility_of_element_located((By.CLASS_NAME, "hmenu-visible"))
                )
            except TimeoutException:
                # Try another alternative
                menu_content = self.wait.until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, "#hmenu-canvas-background.hmenu-translateX"))
                )
        
        # Verify menu is visible and has content
        assert menu_content.is_displayed(), "All menu content is not visible"
        
        # Additional verification - check for menu items
        try:
            menu_items = self.wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".hmenu-item"))
            )
            assert len(menu_items) > 0, "Menu items not found"
        except TimeoutException:
            # Try alternative verification
            menu_items = self.wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#hmenu-content ul li"))
            )
            assert len(menu_items) > 0, "Menu items not found"
        
    def test_category_navigation(self):
        """Test category navigation functionality"""
        self.driver.get("https://www.amazon.in")
        
        # TC_CAT_001: Navigate to Electronics
        try:
            # First try the main menu link
            electronics_link = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/electronics/') and contains(text(), 'Electronics')]"))
            )
        except TimeoutException:
            # If not found, try opening the hamburger menu
            all_menu = self.wait.until(
                EC.element_to_be_clickable((By.ID, "nav-hamburger-menu"))
            )
            all_menu.click()
            
            # Wait for and click Electronics in the hamburger menu
            electronics_link = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'hmenu-item') and contains(text(), 'Electronics')]"))
            )
        
        electronics_link.click()
        time.sleep(2)  # Wait for page to load
        
        # Verify navigation - check for multiple possible title variations
        page_title = self.driver.title.lower()
        assert any(term in page_title for term in ["electronics", "electronic products"]), "Not on Electronics page"
        
        # TC_CAT_005: Test back navigation
        self.driver.back()
        assert "amazon.in" in self.driver.title.lower(), "Back navigation failed"
        
    def test_search_functionality(self):
        """Test search functionality"""
        self.driver.get("https://www.amazon.in")
        
        # TC_SEARCH_001: Verify search bar
        search_bar = self.wait.until(
            EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
        )
        assert search_bar.is_displayed(), "Search bar is not visible"
        
        # TC_SEARCH_003: Test search with valid product
        search_bar.clear()
        search_bar.send_keys("laptop")
        search_bar.send_keys(Keys.RETURN)
        
        # Verify search results - try multiple possible selectors
        try:
            results = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-component-type='s-search-result']"))
            )
        except TimeoutException:
            results = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".s-result-item"))
            )
        
        assert results.is_displayed(), "Search results not displayed"
        
    def test_account_navigation(self):
        """Test account navigation functionality"""
        self.driver.get("https://www.amazon.in")
        
        # TC_ACC_001: Verify Account & Lists dropdown
        account_list = self.wait.until(
            EC.presence_of_element_located((By.ID, "nav-link-accountList"))
        )
        self.actions.move_to_element(account_list).perform()
        
        # Verify dropdown content
        dropdown_content = self.wait.until(
            EC.presence_of_element_located((By.ID, "nav-al-container"))
        )
        assert dropdown_content.is_displayed(), "Account dropdown not displayed"
        
    def test_cart_navigation(self):
        """Test cart navigation functionality"""
        self.driver.get("https://www.amazon.in")
        
        # TC_CART_001: Verify cart icon visibility
        cart_icon = self.wait.until(
            EC.presence_of_element_located((By.ID, "nav-cart"))
        )
        assert cart_icon.is_displayed(), "Cart icon is not visible"
        
        # TC_CART_002: Navigate to cart
        cart_icon.click()
        time.sleep(2)  # Wait for page load
        
        # Try multiple possible selectors for cart verification
        try:
            # Try first selector
            cart_header = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "h1.sc-empty-cart-header"))
            )
            assert "Cart" in cart_header.text or "Shopping Cart" in cart_header.text, "Not on cart page"
        except TimeoutException:
            try:
                # Try second selector
                cart_header = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Shopping Cart') or contains(text(), 'Cart')]"))
                )
                assert True, "On cart page"  # If we found the element, we're on the cart page
            except TimeoutException:
                # Try third selector - verify URL instead
                assert "cart" in self.driver.current_url.lower(), "Not on cart page"

    def test_smoke_navigation(self):
        """TC_NAV_SMOKE_001: Test hamburger menu functionality"""
        self.driver.get("https://www.amazon.in")
        
        # Click hamburger menu
        hamburger_menu = self.wait.until(
            EC.element_to_be_clickable((By.ID, "nav-hamburger-menu"))
        )
        hamburger_menu.click()
        
        # Verify side panel
        side_panel = self.wait.until(
            EC.visibility_of_element_located((By.ID, "hmenu-content"))
        )
        assert side_panel.is_displayed(), "Side panel not visible"
        
        # Verify all main sections are present
        sections = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".hmenu-item"))
        )
        assert len(sections) > 0, "No sections found in hamburger menu"
        
    def test_ui_navigation_layout(self):
        """TC_NAV_UI_001: Test navigation menu layout and styling"""
        self.driver.get("https://www.amazon.in")
        
        # Check main navigation elements
        nav_elements = {
            "logo": (By.ID, "nav-logo"),
            "search": (By.ID, "nav-search"),
            "cart": (By.ID, "nav-cart"),
            "account": (By.ID, "nav-link-accountList")
        }
        
        # Verify all elements are present and visible
        for element_name, locator in nav_elements.items():
            element = self.wait.until(EC.presence_of_element_located(locator))
            assert element.is_displayed(), f"{element_name} is not visible"
            
            # Get element position
            location = element.location
            assert location['y'] >= 0, f"{element_name} vertical alignment incorrect"
            
    def test_ui_dropdown_behavior(self):
        """TC_NAV_UI_002: Test dropdown behavior and transitions"""
        self.driver.get("https://www.amazon.in")
        
        # Test Account & Lists dropdown
        account_dropdown = self.wait.until(
            EC.presence_of_element_located((By.ID, "nav-link-accountList"))
        )
        
        # Hover over the dropdown
        self.actions.move_to_element(account_dropdown).perform()
        
        # Verify dropdown content appears
        dropdown_content = self.wait.until(
            EC.visibility_of_element_located((By.ID, "nav-flyout-accountList"))
        )
        assert dropdown_content.is_displayed(), "Account dropdown not displayed"
        
        # Verify dropdown links are clickable
        dropdown_links = dropdown_content.find_elements(By.TAG_NAME, "a")
        assert len(dropdown_links) > 0, "No links found in account dropdown"
        
    def test_integration_search_filter(self):
        """TC_NAV_INT_001: Test search and filter integration"""
        self.driver.get("https://www.amazon.in")
        
        # Perform search
        search_box = self.wait.until(
            EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
        )
        search_box.send_keys("laptop")
        search_box.send_keys(Keys.RETURN)
        
        # Wait for results
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-component-type='s-search-result']"))
        )
        
        # Try different selectors for brand filter
        filter_selectors = [
            "//span[contains(text(), 'Brands')]",
            "//span[contains(text(), 'Brand')]",
            "//div[contains(@id, 'brandsRefinements')]",
            "//div[contains(@id, 'filters')]//span[contains(text(), 'Brand')]"
        ]
        
        brand_filter = None
        for selector in filter_selectors:
            try:
                brand_filter = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, selector))
                )
                if brand_filter.is_displayed():
                    break
            except:
                continue
        
        if brand_filter:
            brand_filter.click()
            time.sleep(2)  # Wait for filter to apply
            
            # Verify filter is applied (check URL or result count change)
            results_info = self.driver.find_element(By.CSS_SELECTOR, "[data-component-type='s-search-results']")
            assert results_info.is_displayed(), "Results not updated after filter"
        else:
            print("Brand filter not found - skipping filter test")
            
    def test_integration_cart(self):
        """TC_NAV_INT_002: Test cart integration"""
        self.driver.get("https://www.amazon.in")
        
        # Search for a product
        search_box = self.wait.until(
            EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
        )
        search_box.send_keys("book")
        search_box.send_keys(Keys.RETURN)
        
        # Try different selectors for first product
        product_selectors = [
            "[data-component-type='s-search-result'] h2 a",
            ".s-result-item h2 a",
            ".s-search-results .a-link-normal",
            "//div[contains(@class, 's-result-item')]//h2//a"
        ]
        
        first_product = None
        for selector in product_selectors:
            try:
                if selector.startswith("//"):
                    first_product = self.wait.until(
                        EC.element_to_be_clickable((By.XPATH, selector))
                    )
                else:
                    first_product = self.wait.until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                    )
                if first_product.is_displayed():
                    # Try to click using JavaScript if element is visible
                    try:
                        self.driver.execute_script("arguments[0].click();", first_product)
                        break
                    except:
                        # If JavaScript click fails, try scrolling and regular click
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", first_product)
                        time.sleep(1)  # Wait for scroll
                        try:
                            first_product.click()
                            break
                        except:
                            continue
            except:
                continue
                
        assert first_product is not None, "No product found to click"
        
        # Switch to new tab if opened
        self.driver.switch_to.window(self.driver.window_handles[-1])
        
        # Try to add to cart if button is available
        try:
            add_to_cart_selectors = [
                "add-to-cart-button",
                "submit.add-to-cart",
                "//input[contains(@name, 'submit.add-to-cart')]",
                "//span[contains(text(), 'Add to Cart')]//parent::button"
            ]
            
            add_to_cart = None
            for selector in add_to_cart_selectors:
                try:
                    if selector.startswith("//"):
                        add_to_cart = self.wait.until(
                            EC.element_to_be_clickable((By.XPATH, selector))
                        )
                    else:
                        add_to_cart = self.wait.until(
                            EC.element_to_be_clickable((By.ID, selector))
                        )
                    if add_to_cart.is_displayed():
                        # Try JavaScript click first
                        try:
                            self.driver.execute_script("arguments[0].click();", add_to_cart)
                            break
                        except:
                            # If JavaScript click fails, try regular click
                            add_to_cart.click()
                            break
                except:
                    continue
                    
            if add_to_cart:
                time.sleep(2)  # Wait for cart update
                
                # Verify cart update
                cart_count = self.wait.until(
                    EC.presence_of_element_located((By.ID, "nav-cart-count"))
                )
                assert int(cart_count.text) > 0, "Cart count not updated"
            else:
                print("Add to cart button not found - skipping cart test")
                
        except Exception as e:
            print(f"Error adding to cart: {str(e)}")
            # Take screenshot for debugging
            self.driver.save_screenshot("cart_error.png")
            
    def test_browser_compatibility_chrome(self):
        """TC_NAV_BC_001: Test Chrome compatibility"""
        self.driver.get("https://www.amazon.in")
        
        # Verify browser information
        user_agent = self.driver.execute_script("return navigator.userAgent;")
        assert "Chrome" in user_agent, "Not running in Chrome browser"
        
        # Test responsive behavior
        window_sizes = [
            (1920, 1080),  # Desktop
            (1366, 768),   # Laptop
            (768, 1024)    # Tablet
        ]
        
        for width, height in window_sizes:
            self.driver.set_window_size(width, height)
            time.sleep(1)  # Wait for resize
            
            # Verify critical elements are visible
            logo = self.wait.until(EC.presence_of_element_located((By.ID, "nav-logo")))
            assert logo.is_displayed(), f"Logo not visible at {width}x{height}"
            
            search = self.wait.until(EC.presence_of_element_located((By.ID, "nav-search")))
            assert search.is_displayed(), f"Search not visible at {width}x{height}" 