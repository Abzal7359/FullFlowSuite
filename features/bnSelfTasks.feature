Feature: checking Tasks section functionalities
  @lead
  Scenario: back to dashboard click settings back button
    When click on setting link to go dashboard
  @lead
  Scenario: creating task tomorrow date and validating time and date
    When go to leads
    And click one lead
    And create task and get date and time
    And got TASKS section
    And apply filters like assigne and date
    Then check the task is showing or not
  @lead
  Scenario: change status from TASKS page and check in activity area

    When click on status change to completed
    And selecte completed filter and validate it is in completed filter or not
    Then click on that person and check in activity area Task update got or not



  @opportunity @t
  Scenario: creating task tomorrow date and validating time and date for opportunities
    When go on opportunities
    And click one lead
    And create task and get date and time
    And got TASKS section
    And apply filters like assigne and date
    Then check the task is showing or not
  @opportunity @t
  Scenario:  change status from TASKS page and check in activity area for opportunity member
    When click on status change to completed
    And selecte completed filter and validate it is in completed filter or not
    Then click on that person and check in activity area Task update got or not

  @lead
  Scenario:create task in tasks section and validate not associated
    When got TASKS section
    When create task enter details
    And click clear all and filter tomorrow
    Then validate Not Associated is displaying or not
  @lead
  Scenario: search number in input field and check same nuber users are getting displayed or not
    When collect one phone number
    And send input this number in search field
    Then find the users with this numbers got displayed or not

  @lead
  Scenario: clone task and validate in activity area
    When click on clone option of task
    Then validate in activity area

  @lead
  Scenario: Add comment and validate
    When got TASKS section
    And click on task bar and add comment
    Then validate the commnet added or not



