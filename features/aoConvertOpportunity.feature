Feature: converting lead into opportunity
  @lead
  Scenario: converting lead to opportunity without changing prefilled details
    When click on lead
    And click on converted to opportunity
    And enter budget
    And select configuration type
    And click on savee button
    Then validate in opportunities list
  @lead
  Scenario: converting lead to opportunity with changing prefilled details
    When click on leads list
    When click on lead
    And click on converted to opportunity
    And change the prefilled detials
    And enter budget
    And select configuration type
    And click on savee button
    Then validate in opportunities list
  @lead
  Scenario: converting lead to opportunity with changing prefilled details and filling all details
    When click on leads list
    When click on lead
    And click on converted to opportunity
    And change the prefilled detials
    And enter budget
    And select configuration type
    And fill all the fields with data
    And click on savee button
    Then validate in opportunities list




