# Created by Dom L. at 12/30/21
Feature:Empty Cart tests

  Scenario: 'Your Amazon Cart is empty' shown if no product added
    Given Open Amazon page
    When Click on cart icon
    Then Verify 'Your Amazon Cart is empty' text present
