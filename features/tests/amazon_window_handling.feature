# Created by Dom L. at 12/21/21

Feature: Amazon window handling Test cases


  Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon T&C page
    When Click on Amazon Privacy Notice link
    And Store original windows
    And Switch to the newly opened window
    Then Verify Amazon Privacy Notice page is opened
    And User can close new window and switch back to original

