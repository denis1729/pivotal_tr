@positive
Feature: /account positive

  @account_list @delete
  Scenario Outline: verify that is possible created an account memberships
    Given I POST to member_list endpoints
    And I send the following information file_create for the feature
    When I update the next fields with <name>,<email>,<initials>
    Then I send the requests
    And  I keep the id the created feature
    And I should get responses with status code 200

    Examples:
      | name                                                                                                 | email               | initials |
      | d                                                                                                    | d@g.com             | D        |
      | #                                                                                                    | d@hotmail.com       | #        |
      | .                                                                                                    | d@erik.org          | .        |
      | /                                                                                                    | f@yahoo.her         | /        |
      | -                                                                                                    | f@PY.py             | -        |
      | 123                                                                                                  | f@py.py             | 12       |
      | Denis Camacho                                                                                        | DENIS@CMho.cama     | DC       |
      | DenisCamacho                                                                                         | DENIS@cho.cama      | DN       |
      | HELLOWORLDIAMDENIS                                                                                   | HELLO@WORDL.test    | HW       |
      | Test Test                                                                                            | test@test.test      | test     |
      | Test Test Test Test TestTestTestTest                                                                 | Tests@Tesst.Test    | Tests    |
      | Test Test Test Test Test Test Test Test                                                              | TesST@TeSsT.TeSsT   | TesTSS   |
      | My word is true My word is true My word is true My word is true My word is true My word is true My w | worksse@gmail.com   | MY       |
      | APITestAPITestAPITestAPITestAPITestAPITestAPITestAPITestAPITestAPITestAPITestAPITestAPITestAPITestAP | APITEST@GOTMAIL.COM | API      |
      | a00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000z | a00z@yahoo.org      | cero     |
