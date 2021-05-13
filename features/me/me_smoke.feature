@smoke
Feature: /me Smoke
  Scenario: Get exchange account with name
    Given I GET to me endpoint
    And I send the request
    Then I should get response with status code 200