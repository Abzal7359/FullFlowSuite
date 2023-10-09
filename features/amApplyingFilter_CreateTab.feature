Feature: Applying filter and createtab
  @lead
  Scenario: when click leads it is in open filter ornot
    When click onleads
    Then check in leads page that it automatically in openfilter
  @lead
  Scenario Outline: create filterTab
    When click on filterbutton
    And select attributes you want to filter "<source>" and "<type>" andtabName "<name>"
    And click _create
    And validate tab is created or _not
    And edit filter name and check name is updated or not
    When click on new filter tab and _delte
    And now check tab is deleted or _not
    Then check in leads page that it automatically in openfilter

    Examples:
    |source     |     type  | name            |
    |Sub        | Face      |  facebook       |
    |Source     | Digi      |  All digital    |
    |Assign     | Venkat    |  Assigne        |
#    |Campa      |Baja       |  campaign       |
#    |Created    | Kishor Kharade |  created   |
