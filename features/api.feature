Feature: Testing restcountries API
 
 
Scenario: Happy path
    Given I give the currency code
    When I make a GET request to the restcountries API
    Then the status code should be 200
    And at least one country name should be returned
    And Save the company name
 
Scenario: Unhappy path
    Given I give the invalid currency code
    When I make a GET request to the restcountries API
    Then the status code should be 404
    And the response should contain a message indicating the currency doesn't exist
