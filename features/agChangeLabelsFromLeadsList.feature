Feature: changing labels from leads List Homepage
  @lead
  Scenario: changing labels selecting non selected labels and deselectin selected labels
    When click on lead button to back to leads
    And go on labels column and change labels
    Then validate in Activity area wheather labels are changed or not
