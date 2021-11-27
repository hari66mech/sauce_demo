Feature: Saucedemo login

    Background:
        Given The saucedemo login page is displayed


    Scenario: Validate the cart page when the user login with standard_user credential
        When I login with the standard_user credentials
        Then I validate the home page

    Scenario Outline: Login
        When I login with the user credentials "<username>" and "<Password>"

        Examples:
          | username      | Password     |
          | standard_user | secret_sauce |