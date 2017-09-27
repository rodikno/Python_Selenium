Feature: Login

Scenario: Log in with correct credentials
    Given user is on the login page
    When I log in with correct credentials
    Then I am logged in