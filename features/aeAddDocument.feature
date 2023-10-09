Feature: Adding document in leads profile
  @lead
  Scenario: Document is uploading in document  section
    When user clicks on Document option
    And in that page he clicks Add Documents
    And user upload file here
    And clicks save
    Then check wheather the file is uploaded or not