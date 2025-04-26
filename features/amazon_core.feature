@amazon
Feature: Amazon Core Navigation
  As a user, I want to interact with Amazon's core navigation features
  So that I can browse and search products efficiently.

  @smoke
  Scenario: Verify hamburger menu functionality
    Given I am on the Amazon homepage
    When I click the hamburger menu
    Then The hamburger menu should expand displaying main categories

  @functional
  Scenario: Verify search functionality
    Given I am on the Amazon homepage
    When I enter "laptop" in the search bar
    And I press Enter
    Then The search results page should display products related to "laptop"

  @ui
  Scenario: Verify account navigation
    Given I am on the Amazon homepage
    When I hover over the "Account & Lists" dropdown
    Then The dropdown should display options including "Your Account" and "Sign In"

  @integration
  Scenario: Verify cart integration
    Given I am on the Amazon homepage
    When I search for "book" and add an item to the cart
    And I check the cart icon in the navigation bar
    Then The cart icon should show the correct item count 