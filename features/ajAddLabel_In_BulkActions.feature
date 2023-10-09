Feature: Adding label in bulk actions
  @lead
  Scenario: In bulk actions adding label
    When select four leads in lead list
    And click in Add label
    And select label and click on save
    Then validate label is added or not


