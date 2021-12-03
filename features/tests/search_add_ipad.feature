# Created by Dom L. at 11/30/21
Feature: Test Search & Add functionality


  Scenario: User can search & add product into Cart
    Given Open Amazon page
    When User search for Ipad
    And Click search icon
    Then Search results for Ipad shown
    When User click on Ipad
    Then Ipad details shown
    When Click Add to Cart button
    When Click Add button
    Then Ipad added to Cart
