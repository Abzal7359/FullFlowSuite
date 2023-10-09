from behave import *

from pages.LeadsProfile import LeadsProfile


@given(u'user navigates to loginpage')
def step_impl(context):
    pass


@when(u'user enters login details mail as "{email}" and passwordas "{password}"')
def step_impl(context,email,password):
    #LOP=login page

    pass


@when(u'click loginbutton')
def step_impl(context):
    #DP = dashboard page

    pass

@when(u'click on sales and inside that clicksleads')
def step_impl(context):

    pass


@when(u'click on one leadProfile')
def step_impl(context):
    pass





@when(u'change assignedPerson')
def step_impl(context):
    context.LDP = LeadsProfile(context.driver)
    context.LDP.clickToChangeAssignedPerson()


@when(u'Change label')
def step_impl(context):
    context.LDP.clickTo_Add_label()

@when(u'change source type and source')
def step_impl(context):
    context.LDP.clickTo_Change_source()




@when(u'change campaign')
def step_impl(context):
    context.LDP.clickToChange_CampaignType()




@then(u'verify All Changed or Not')
def step_impl(context):
    assert context.LDP.isLeadProfile_Modified()




