Feature:  Adding site visit on lead profile
  @lead
  Scenario: Add site visit of feauter
    Given user navigates to -loginpage
    When user enters login details mail as "manoj.assetmonk@gmail.com" and -passwordas "Propflo@1234"
    And click -loginbutton
    And click on sales and inside that -clicksleads
    And click on one -leadProfile
    And click on site Visits
    And click on Add site visit option
    And fill site visit details
    |date        |time   |
    |30-11-2023  |  1130     |
    And click save button
    Then check site visit is added or not

  @lead
  Scenario: Add site visit of past
    When click on Add site visitoption
    And fill site visit past details
    |date        |time   |
    |05-08-2023  |  1630     |
    Then check site visit is added or not





