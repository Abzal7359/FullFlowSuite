Feature: converting status
  @lead
  Scenario: converting status from Active to lost
    When click on convert button
    And click lost link
    And enter lost reason
    And click on save
    Then validate in Activity area and go to losts page and validate there
  @lead
  Scenario:converting status from lost to active
    When change assigne
    And changes to active validate at same page
    Then validate in open leads page



