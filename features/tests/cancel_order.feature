# Created by Dom L. at 11/29/21
Feature: Help Search functionality


  Scenario: User gets help using Search Help Library

    Given Open Amazon Help page
    When Search for Cancel order & hit enter
    Then Verify that Cancel Items or Orders text is present
