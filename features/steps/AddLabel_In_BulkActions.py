from behave import *

from pages.LeadsPage import LeadsPage





@when(u'select four leads in lead list')
def step_impl(context):
    #------------------------------------
    context.LP=LeadsPage(context.driver)
    context.LP.selectFourLeads()

@when(u'click in Add label')
def step_impl(context):
    context.LP.click_add_label_button()


@when(u'select label and click on save')
def step_impl(context):
    context.LP.select_label_item()


@then(u'validate label is added or not')
def step_impl(context):
    assert context.LP.is_labels_selected()
