Feature: Adding existing lead which makes duplicate
  @lead
  Scenario: Adding existing lead with same phone number
    When get count of duplicates
    When click on leads link to go back to lead list
    And click add lead button to add new lead
    And fill the details to add lead with same phone num and save
    |source    |firstName|
    |Digital   |miller         |
    Then check duplicate count is increased or not


  @lead
  Scenario: Adding existing lead with same email and other phone number
    When get count of duplicates
    When click on leads link to go back to lead list
    And click add lead button to add new lead
    And fill the details to add lead with same mail and other num and save
    |source    |firstName|
    |Referrals  |miller         |
    Then check duplicate count is increased or not

  @lead
  Scenario: Adding existing lead with same email and same phone number
    When get count of duplicates
    When click on leads link to go back to lead list
    And click add lead button to add new lead
    And fill the details to add lead with same mail and same phone number and save
    |source    |firstName|
    |Channel partner |miller         |
    Then check duplicate count is increased or not
