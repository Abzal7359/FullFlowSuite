Feature: checking bulk import functionality which add leads in bulk
  @lead
  Scenario: Bulk import functionality to add leads in bulk
    When click on Bulk import
    And upload csv file in which lead details will present
    And now select Auto select Fields and click validate CSV
    And now click upload button
    Then validate leads are added or not