@crud
Feature: /account CRUD

  @account_list @delete
  Scenario: verify that is possible created an account memberships
    Given I POST to member_list endpoints
    And I send the following information file_create for the feature
    And I send the requests
    And  I keep the id the created feature
    Then I should get responses with status code 200
    And I will validate that the information is correct for membership
    And I will validate that the created fields are the same

  @account_list @create @delete
  Scenario: verify that is possible show a specific person
    Given I GET to member endpoint with specific id
    And I send the requests
    Then I should get responses with status code 200
    And I will validate that the information is correct for membership

  @account_list
  Scenario: verify that is possible show an account
    Given I GET to account endpoints
    And I send the requests
    Then I should get responses with status code 200
    And I will validate that the information is correct for account

  @account_list @create @delete
  Scenario: verify that is possible updated an account memberships
    Given I PUT to member endpoint with specific id
    And I send the following information file_update for the feature
    And I send the requests
    Then I should get responses with status code 200
    And I will validate that the information is correct for membership
    And I will validate that the update fields are the same

  @account_list @create @delete
  Scenario: verify that is possible delete
    Given I DELETE to member endpoint with specific id
    And I send the requests
    Then I will validate that the feature has been deleted
    And I will validate that the information is correct for membership