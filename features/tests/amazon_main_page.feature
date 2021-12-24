# Created by Dom L. at 11/29/21
Feature: Testing Search functionality

  Scenario: User can search for an item
    Given Open Amazon page
    When Search for table
    And Click search icon
    Then Search results for table shown
