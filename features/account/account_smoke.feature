@smoke
Feature: /account Smoke

  @account_list @delete
  Scenario: verify that is possible created an account memberships
    Given I POST to member_list endpoints
    And I send the following information file_create for the feature
    And I send the requests
    And  I keep the id the created feature
    Then I should get responses with status code 200

  @account_list @create @delete
  Scenario: verify that is possible show all memberships
    Given I GET to member_list endpoints
    And I send the requests
    Then I should get responses with status code 200

  @account_list @create @delete
  Scenario: verify that is possible show a specific person
    Given I GET to member endpoint with specific id
    And I send the requests
    Then I should get responses with status code 200

  @account_list @create @delete
  Scenario: verify that is possible set an account memberships
    Given I PUT to member endpoint with specific id
    And I send the following information file_update for the feature
    And I send the requests
    Then I should get responses with status code 200

  @account_list @create @delete
  Scenario: verify that is possible delete
    Given I DELETE to member endpoint with specific id
    And I send the requests
    Then I should get responses with status code 204

  Scenario: verify that is possible show all accounts
    Given I GET to account_list endpoint for account
    And I send the requests
    Then I should get responses with status code 200

  @account_list
  Scenario: verify that is possible show an account
    Given I GET to account endpoints
    And I send the requests
    Then I should get responses with status code 200

  Scenario: verify that is possible show all accounts summaries
    Given I GET to account_summaries endpoint for account
    And I send the requests
    Then I should get responses with status code 200

  Scenario: verify that is possible show all accounts summaries
    Given I GET to account_summaries endpoint for account
    And  I sent the with_permission
    And I send the requests
    Then I should get responses with status code 200