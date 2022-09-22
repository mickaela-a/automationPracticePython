Feature: Login demoblaze failed

    As a common user
    I want to Login whit invalid password
    In order to get error message

    Scenario: Login with invalid credentials
        Given the user is on demoblaze page
        When the user tries to login with invalid credentials
        Then the page shows an incorrect password message
