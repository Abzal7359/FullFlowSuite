Feature: creating label in labels in configuration and some editing
  @lead
  Scenario: click settings
    When click settings gear image

  @lead
  Scenario: Add label in label configurators->leads
    When click on Lead button in label configurators
    And click on add label
    And enter name of label
    And validate label added or not in same page
    And click on lead list
    Then check here in lead list that label is added or not
  @lead
  Scenario:Drag and drop label to change position and check
    When go to leads label configurator
    And change position of label
    And click on lead list
    Then check in lead list that label position is change or not


  @lead
  Scenario: delete the added label and check deleted or not
    When go to leads label configurator
    And delete the added label
    Then validate here onlly by seeing count of lead labels
  @lead
  Scenario: disable the label and validate in leads list
    When click on disable button
    And click on lead list
    Then check in lead list the label is disabled or not
  @lead
  Scenario: enable the label and check the label is showing or not in leads list
    When go to leads label configurator
    And enable the label
    And click on lead list
    Then check in lead list labels wheather the able is enabled or not
  @lead
  Scenario: changing colour of label and validate
    When go to leads label configurator
    And change colour of one label
    Then validate colour is changed or not

