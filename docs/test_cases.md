# Amazon Navigation Menu Test Cases

## Test Scenarios for Navigation Menu

### 1. Main Navigation Menu Visibility and Accessibility
- **TC_NAV_001**: Verify that the main navigation menu is visible on the homepage
- **TC_NAV_002**: Verify that the "All" menu button is clickable
- **TC_NAV_003**: Verify that hovering over menu items shows submenus
- **TC_NAV_004**: Verify that the navigation menu is responsive

### 2. Category Navigation
- **TC_CAT_001**: Verify navigation to "Electronics" category
- **TC_CAT_002**: Verify navigation to "Books" category
- **TC_CAT_003**: Verify navigation to "Fashion" category
- **TC_CAT_004**: Verify navigation to "Home & Kitchen" category
- **TC_CAT_005**: Verify back navigation from category pages

### 3. Search Functionality
- **TC_SEARCH_001**: Verify search bar is visible and clickable
- **TC_SEARCH_002**: Verify search suggestions appear when typing
- **TC_SEARCH_003**: Verify search with valid product name
- **TC_SEARCH_004**: Verify search with invalid product name
- **TC_SEARCH_005**: Verify search filters functionality

### 4. Account & Lists Navigation
- **TC_ACC_001**: Verify "Account & Lists" dropdown menu
- **TC_ACC_002**: Verify navigation to "Your Orders"
- **TC_ACC_003**: Verify navigation to "Your Addresses"
- **TC_ACC_004**: Verify navigation to "Your Lists"

### 5. Cart Navigation
- **TC_CART_001**: Verify cart icon is visible
- **TC_CART_002**: Verify navigation to cart page
- **TC_CART_003**: Verify cart updates when items are added
- **TC_CART_004**: Verify cart persistence across sessions

## Test Data Requirements
1. Valid Amazon account credentials
2. List of product names for search testing
3. Sample products for cart testing

## Prerequisites
1. Web browser (Chrome/Firefox/Safari)
2. Stable internet connection
3. Valid Amazon account
4. Test environment setup

## Test Environment
- Operating System: Windows/Mac/Linux
- Browsers: Chrome (latest), Firefox (latest)
- Screen Resolution: 1920x1080 (minimum)
- Internet Speed: Minimum 5 Mbps

## Assumptions
1. Tests will be performed on the Amazon website (not mobile app)
2. Test account has no pending orders or empty cart at start
3. Website is accessible and not under maintenance
4. Test execution during non-peak hours
5. Basic product categories are available in all regions 