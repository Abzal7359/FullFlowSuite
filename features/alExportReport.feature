Feature: Export functionality for report generation
  @lead
  Scenario: Export report with some choose columns
    When click on Export
    And now select which columns you need in report
    And click on export button
    And now go to downloads section
    Then here validate report generated or not