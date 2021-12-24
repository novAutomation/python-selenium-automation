# Created by Dom L. at 12/20/21

Feature: Test cases for wholefoods page

  Scenario: Wholefoods products have regular prices and names

    Given Open Amazon Wholefoods page
    Then Verify that every product has a text Regular
