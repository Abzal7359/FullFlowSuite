Feature: Adding and edit profile details
  @lead
  Scenario: editing profile details
    Given user navigates to the loginpage
    When user enters login details mail as "manoj.assetmonk@gmail.com" and the passwordas "Propflo@1234"
    And click the loginbutton
    And click on sales and inside that the clicksleads
    And click on one the leadProfile
    And click on profile
    And click on edit profile
    And first fill the basic details part
    | filepath                            | firstname  | lastname    |  DateOfBirth   |
    |C://Users/abzalhussain/Desktop/download.jpeg|  Addi |   Ramesh  | 26092001  |

    And fill contact details part

    |secondPhoneNum|secondMail|ThirdPhone|ThirdMail |  Address | LinkedIn | facebook | instagram | twitter |
    |1234567890    |adnz@gmail.com |1234567890|adnz@gmail.com| 21/224|https://www.youtube.comL|https://www.youtubeF|https://www.youtube.com/I|https://www.youtube.com/T|
    And fill professional details part
    |companyName|role     |FromD   |ToD   |compnayWeb     |location   |salary     |
    |Bento      |QA        |  07072023 |07072025 |https://www.youtube.|   Banglore   |    4500   |
    And fill educational details part
    |schoolName     |course     |fromD     |toD     |loc       |
    | Naryana    | BIPC    | 06072017    |07042019     |Ongole       |
    And click on save the -button
    Then validate wheater the updates are reflected or not
