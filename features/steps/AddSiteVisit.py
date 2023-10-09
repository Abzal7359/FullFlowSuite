import configparser
import time

from behave import *
from selenium.webdriver.common.by import By

from pages.AddSiteVisitPage import AddSiteVisitPage
config = configparser.ConfigParser()
config.read(r'config.txt')

@given(u'user navigates to -loginpage')
def step_impl(context):
    pass


@when(u'user enters login details mail as "{email}" and -passwordas "{password}"')
def step_impl(context,email,password):
    #LOP=login page
    pass


@when(u'click -loginbutton')
def step_impl(context):
    #DP = dashboard page
    pass


@when(u'click on sales and inside that -clicksleads')
def step_impl(context):
    #LP=LeadsPage
    pass


@when(u'click on one -leadProfile')
def step_impl(context):
    pass


@when(u'click on site Visits')
def step_impl(context):
    context.ASVP=AddSiteVisitPage(context.driver)
    context.ASVP.clickOnSiteVisits_bar()



@when(u'click on Add site visit option')
def step_impl(context):
    context.ASVP.createSite_Visit()


@when(u'fill site visit details')
def step_impl(context):
    for row in context.table:
        context.ASVP.fill_siteVisit_details(row["date"],row["time"])

@when(u'click save button')
def step_impl(context):
    context.ASVP.click_On_Save()


@then(u'check site visit is added or not')
def step_impl(context):
    assert context.ASVP.is_siteVisitAdded()

#site visit Add past scenario

@when(u'click on Add site visitoption')
def step_impl(context):
    context.ASVP = AddSiteVisitPage(context.driver)
    context.ASVP.createSite_Visit()


@when(u'fill site visit past details')
def step_impl(context):
    for row in context.table:
        context.ASVP.fill_siteVisit_details(row["date"], row["time"])
        context.driver.find_element(By.XPATH,"(//textarea[@id='notes'])[1]").send_keys("so much interested")

        time.sleep(float(config.get('waiting_time', 'min_wait')))

        context.ASVP.click_On_Save()





