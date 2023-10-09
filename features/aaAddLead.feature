Feature: Adding Lead
  @lead
  Scenario: Add lead with mandatory fields
    Given user navigates to login page
    When user enters login details mail as "manoj.assetmonk@gmail.com" and password as "Propflo@1234"
    And click login button
    And click on sales and inside that clicks leads
    And click Add Lead option
    And enters mandatory fields in add leads page
    |firstname  |lastname      |  mobile         |email             | description |
    |Ramesh |  Addi |     8309144641    | rameshaddi1111@gmail.com         |eager to buy |
    And click on save button
    Then the lead details should added successfully
  @lead
  Scenario: create task
    When click on tasks bar
    And click on create task
    And write task and set task details
    | textbox              | time       |
    | site visit tomorrow  | 1530       |
    And click task save
    Then ckeck task is created or not

  @lead
  Scenario:edit task like clone and adding comment
    When click on tasks bar
    And click clone task and change priority and _save
    And check task is cloned or not validate in activity _area
    And click on view details on task and add _comment
    Then check in activity _area
  @lead
  Scenario: Add notes
    When clickon Notes taskbar
    And click on create notes
    And write description in notes and save
    |notesDescription|
    |today he is busy tommorow site vist wee can go |
    Then check the note is created or not