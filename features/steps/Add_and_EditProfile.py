import configparser
import time

from behave import *
from selenium.webdriver.common.by import By
from dataproviders import data
from pages.Add_and_editProfilePage import AddAndEditProfilePage
from pages.DashboardPage import DashboardPage
from pages.LeadsProfile import LeadsProfile

config = configparser.ConfigParser()
config.read(r'config.txt')


@given(u'user navigates to the loginpage')
def step_impl(context):
    pass


@when(u'user enters login details mail as "{email}" and the passwordas "{password}"')
def step_impl(context,email,password):
    #LOP=login page
    pass


@when(u'click the loginbutton')
def step_impl(context):
    #DP = dashboard page
    pass


@when(u'click on sales and inside that the clicksleads')
def step_impl(context):
    #LP=LeadsPage
    pass


@when(u'click on one the leadProfile')
def step_impl(context):
    pass


@when(u'click on profile')
def step_impl(context):
    #ADD edit profile page
    context.AEP=AddAndEditProfilePage(context.driver)
    context.AEP.clikcOnProfile()



@when(u'click on edit profile')
def step_impl(context):
    context.AEP.clickOnEditProfile()

@when(u'first fill the basic details part')
def step_impl(context):
    global FN
    global LN
    for i in context.table:
        FN=data.c[1]
        LN=data.c[0]
        # FN = i["firstname"]
        # LN = i["lastname"]
        context.AEP.enterBasicDetails(i["filepath"],data.c[1],data.c[0],i["DateOfBirth"])


@when(u'fill contact details part')
def step_impl(context):
    for r in context.table:
        context.AEP.enterContactDetials(r["secondPhoneNum"],r["secondMail"],r["ThirdPhone"],r["ThirdMail"]
                                    ,r["Address"],r["LinkedIn"],r["facebook"]
                                    ,r["instagram"],r["twitter"])

@when(u'fill professional details part')
def step_impl(context):
    for row in context.table:
        context.AEP.enterProfessionalDetails(row["companyName"],row["role"],row["FromD"],
                                             row["ToD"],row["compnayWeb"],row["location"],row["salary"])

@when(u'fill educational details part')
def step_impl(context):
    for j in context.table:
        context.AEP.enterEducationalDetails(j["schoolName"],j["course"],j["fromD"],j["toD"],j["loc"])



@when(u'click on save the -button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"(//button[normalize-space()='Save'])[1]").click()
    time.sleep(2)




@then(u'validate wheater the updates are reflected or not')
def step_impl(context):
    c = context.driver.find_element(By.XPATH, "//a[@id='activities']")
    context.driver.execute_script("arguments[0].click()", c)
    time.sleep(float(config.get('waiting_time', 'min_wait')))
    l=[]
    expected="updated Lead Profile"
    actuall=context.driver.find_element(By.XPATH,"//div[@class='ng-star-inserted']//p").text
    if expected in actuall:
        l.append(True)
    else:
        l.append(False)

    context.driver.refresh()
    time.sleep(float(config.get('waiting_time', 'max_wait')))
    #modified------
    # context.driver.find_element(By.XPATH, "//a[normalize-space()='Leads']").click()
    context.DP=DashboardPage(context.driver)
    context.DP.clickOnLeads()
    time.sleep(float(config.get('waiting_time', 'avg_wait')))
    context.LDP = LeadsProfile(context.driver)

    context.LDP.clickOnLeadsProfile()

    #always give Firstname with capital Letter In validation


    name=FN
    actualName=context.driver.find_element(By.XPATH,"//div[@class='inline-flex']").text
    if name in actualName:
        l.append(True)
    else:
        l.append(False)
    if False not in l:
        assert True
    else:
        assert False





