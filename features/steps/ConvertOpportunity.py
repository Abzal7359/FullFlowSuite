

from behave import *

from pages.ConvertOpportunityPage import ConvertOpportunityPage




@when(u'click on lead')
def step_impl(context):
    context.COP=ConvertOpportunityPage(context.driver)
    context.COP.click_lead()
    #------------------------------------------------------------------------------




@when(u'click on converted to opportunity')
def step_impl(context):
    context.COP.click_convert()

@when(u'enter budget')
def step_impl(context):
    context.COP.enter_budget("5000000")


@when(u'select configuration type')
def step_impl(context):
    context.COP.select_configuration_type()


@when(u'click on savee button')
def step_impl(context):
    context.COP.click_save()


@then(u'validate in opportunities list')
def step_impl(context):
    assert context.COP.is_lead_converted_to_opportunity()


@when(u'click on leads list')
def step_impl(context):
    context.COP = ConvertOpportunityPage(context.driver)
    context.COP.click_leads_link()




@when(u'change the prefilled detials')
def step_impl(context):
    context.COP.change_prefill_details()



@when(u'fill all the fields with data')
def step_impl(context):
    context.COP.fill_all_the_fields()
