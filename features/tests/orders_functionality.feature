# Created by Dom L at 11/26/21
Feature: Testing Orders Functionality

  Scenario: Logged out user sees Sign In page upon clicking Orders
    Given User launch Amazon application
    When User clicks Orders tab
    Then Sign In page is displayed

