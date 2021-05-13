@negative
Feature: /account negative

  @account_list
  Scenario Outline: verify that is  not possible created an account memberships
    Given I POST to member_list endpoints
    And I send the following information for create a membership
    """
    {
      "email":<email>,
      "initials": <initials>,
      "name": <name>
    }
    """
    Then I send the requests
    And I should get responses with status code 400
    And  I verify the <message>

    Examples:
      | name          | email              | initials | message                      |
      | test          | test@.com          | Ts       | is not a valid email address |
      | test          | test test@test.com | Ts       | is not a valid email address |
      | test          | testtest.org       | Ts       | is not a valid email address |
      | test          | test@test          | Ts       | is not a valid email address |
      | test          | test@test@test.com | Ts       | is not a valid email address |
      | test          | test@test_test.com | Ts       | is not a valid email address |
