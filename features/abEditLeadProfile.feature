Feature: Edit Leads profile and Check Changes applying or not
  @lead
  Scenario: edit leads profile all fields
    Given user navigates to loginpage
    When user enters login details mail as "manoj.assetmonk@gmail.com" and passwordas "Propflo@1234"
    And click loginbutton
    And click on sales and inside that clicksleads
    And click on one leadProfile
    And change assignedPerson
    And Change label
    And change source type and source
    And change campaign
    Then verify All Changed or Not