Feature: change created Date order in leads list page and check
  @lead
  Scenario: change created Date to descending order
    When clickon lead button to back toleads
    And click on descending date button
    Then validate dates in descending order or not
  @lead
  Scenario: change created Date to Ascending order
    When click on ascending date button
    Then validate dates in ascending order or not
