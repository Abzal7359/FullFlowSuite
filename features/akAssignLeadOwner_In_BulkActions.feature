Feature: assign lead owner through bulg action option
  @lead
  Scenario: assigning lead owner by bulk
    When select four leads in leadlist
    And click on Assigned lead owner button
    And select assigned leader and click save
    Then validate assigned leader is changed or not


#  Scenario: sending mail in bulk actions
#    When select two leads in leadlist
#    And click on send email
#    And select sender
#    And write subject line of mail as "payment need to pay"
#    And check tab pop is working or not in to area
#    And select placeholders
#    And attach any documnet and validate document added or not
#    And now click delete
#    And check delete alert pop up is opened or not and click no on delete alert
#    And now send mail button click
#    Then check on messages wheather the mail is send or not
