# Created by Dom L at 11/26/21
Feature: Testing Orders Functionality


  Scenario: Logged out user sees Sign In page upon clicking Orders
    Given Open Amazon page
    When Click Orders
    Then Verify Sign in page opened

