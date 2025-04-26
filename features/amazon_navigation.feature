@amazon @navigation
Feature: Amazon Navigation Menu Functionality
  As a user, I want to interact with the Amazon navigation menu
  So that I can browse categories, access account options, and navigate the website efficiently.

  @smoke
  Scenario: Verify hamburger menu is accessible and expandable on desktop (TC_NAV_SMOKE_001)
    Given I am on the Amazon homepage
    When I click the hamburger menu
    Then The hamburger menu should expand displaying main categories

  @functional
  Scenario: Verify search bar returns results for a valid query (TC_NAV_FUNC_001)
    Given I am on the Amazon homepage
    When I enter "laptop" in the search bar
    And I press Enter
    Then The search results page should display products related to "laptop"

  @functional @accessibility
  Scenario: Verify keyboard navigation for accessibility (TC_NAV_FUNC_002)
    Given I am on the Amazon homepage
    When I use the Tab key to navigate to the hamburger menu
    And I press Enter to expand it
    Then The hamburger menu should expand displaying main categories

  @ui
  Scenario: Verify Account & Lists dropdown functionality (TC_NAV_UI_001)
    Given I am on the Amazon homepage
    When I hover over the "Account & Lists" dropdown
    Then The dropdown should display options including "Your Account" and "Sign In"

  @ui
  Scenario: Verify navigation menu alignment and visibility (TC_NAV_UI_002)
    Given I am on the Amazon homepage
    When I inspect the hamburger menu
    Then The menu should be visible and properly aligned

  @ui
  Scenario: Verify dropdown behavior for departments (TC_NAV_UI_003)
    Given I am on the Amazon homepage
    When I hover over the "Departments" category in the hamburger menu
    Then The dropdown should display sub-categories smoothly

  @integration
  Scenario: Verify search and filter flow (TC_NAV_INT_001)
    Given I am on the Amazon homepage
    When I enter "headphones" in the search bar
    And I press Enter
    And I apply the "Electronics" category filter
    Then The search results should update to show headphones in the Electronics category

  @integration
  Scenario: Verify cart integration with navigation (TC_NAV_INT_002)
    Given I am on the Amazon homepage
    When I search for "book" and add an item to the cart
    And I check the cart icon in the navigation bar
    Then The cart icon should show the correct item count

  @browser
  Scenario: Verify navigation functionality in Chrome (TC_NAV_BC_001)
    Given I am on the Amazon homepage using Chrome
    When I click the hamburger menu
    And I navigate to the "Electronics" category
    Then The Electronics category page should load correctly

  @smoke @category
  Scenario: Verify navigation to a top-level category (TC_NAV_SMOKE_002)
    Given I am on the Amazon homepage
    When I click the "Books" category from the hamburger menu
    Then I should be redirected to the Books category page

  @subcategory
  Scenario: Verify sub-menu navigation (TC_NAV_SUB_001)
    Given I am on the Amazon homepage
    When I expand the "Electronics" category in the hamburger menu
    And I click the "TV & Video" sub-menu
    Then I should be redirected to the TV & Video sub-category page

  @mobile
  Scenario: Verify navigation menu responsiveness on mobile (TC_NAV_MOB_001)
    Given I am on the Amazon homepage using a mobile viewport
    When I click the hamburger menu
    Then The hamburger menu should expand and be scrollable

  @error
  Scenario: Verify navigation with invalid category selection (TC_NAV_ERR_001)
    Given I am on the Amazon homepage
    When I attempt to navigate to a non-existent category
    Then I should see an error page or remain on the current page

  @performance
  Scenario: Verify navigation menu performance under low network conditions (TC_NAV_PERF_001)
    Given I am on the Amazon homepage with throttled network
    When I click the hamburger menu
    Then The menu should expand within 5 seconds

  @book @functional
  Scenario: Verify book category navigation and filtering (TC_NAV_BOOK_001)
    Given I am on the Amazon homepage
    When I navigate to the "Books" category
    And I apply the "Fiction" filter
    Then I should see a list of fiction books
    And The results should be properly categorized

  @book @functional
  Scenario: Verify book search with author name (TC_NAV_BOOK_002)
    Given I am on the Amazon homepage
    When I enter "J.K. Rowling" in the search bar
    And I select "Books" from the category dropdown
    And I press Enter
    Then The search results should display books by J.K. Rowling
    And The results should be properly sorted

  @book @ui
  Scenario: Verify book category dropdown menu (TC_NAV_BOOK_003)
    Given I am on the Amazon homepage
    When I hover over the "Books" category in the hamburger menu
    Then The dropdown should display sub-categories like "Fiction", "Non-Fiction", "Children's Books"
    And Each sub-category should be clickable

  @book @integration
  Scenario: Verify book recommendation system (TC_NAV_BOOK_004)
    Given I am on the Amazon homepage
    When I navigate to the "Books" category
    And I view a specific book's details
    Then I should see "Customers who bought this item also bought" section
    And The recommendations should be relevant to the current book

  @book @mobile
  Scenario: Verify book category navigation on mobile (TC_NAV_BOOK_005)
    Given I am on the Amazon homepage using a mobile viewport
    When I click the hamburger menu
    And I navigate to the "Books" category
    Then The books category page should load correctly
    And The mobile interface should be properly formatted

  @electronics @functional
  Scenario: Verify electronics category navigation and filtering (TC_NAV_ELEC_001)
    Given I am on the Amazon homepage
    When I navigate to the "Electronics" category
    And I apply the "Smartphones" filter
    Then I should see a list of smartphones
    And The results should be properly categorized

  @fashion @functional
  Scenario: Verify fashion category navigation and filtering (TC_NAV_FASH_001)
    Given I am on the Amazon homepage
    When I navigate to the "Fashion" category
    And I apply the "Men's Clothing" filter
    Then I should see a list of men's clothing items
    And The results should be properly categorized

  @home @functional
  Scenario: Verify home and kitchen category navigation (TC_NAV_HOME_001)
    Given I am on the Amazon homepage
    When I navigate to the "Home & Kitchen" category
    And I apply the "Kitchen Appliances" filter
    Then I should see a list of kitchen appliances
    And The results should be properly categorized

  @search @functional
  Scenario: Verify advanced search functionality (TC_NAV_SEARCH_001)
    Given I am on the Amazon homepage
    When I click the search bar
    Then I should see recent search history
    And I should see popular search suggestions

  @cart @functional
  Scenario: Verify cart functionality from navigation (TC_NAV_CART_001)
    Given I am on the Amazon homepage
    When I click the cart icon in the navigation bar
    Then The cart page should load correctly
    And I should see my cart contents if any items are present

  @account @functional
  Scenario: Verify account navigation options (TC_NAV_ACC_001)
    Given I am on the Amazon homepage
    When I click on "Account & Lists" in the navigation bar
    Then I should see options for "Your Account", "Your Orders", "Your Wish List"
    And Each option should be clickable

  @deals @functional
  Scenario: Verify deals and promotions navigation (TC_NAV_DEALS_001)
    Given I am on the Amazon homepage
    When I click on "Today's Deals" in the navigation bar
    Then The deals page should load correctly
    And I should see current promotions and discounts

  @prime @functional
  Scenario: Verify Prime membership navigation (TC_NAV_PRIME_001)
    Given I am on the Amazon homepage
    When I click on "Prime" in the navigation bar
    Then The Prime membership page should load correctly
    And I should see Prime benefits and membership options 