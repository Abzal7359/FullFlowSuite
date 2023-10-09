

from behave import *
from selenium.webdriver.common.by import By
from pages.LeadLabelsConfiguratorPage import LeadLabelsConfiguratorPage
import time


@when(u'click settings gear image')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//app-topbar/div/div/div[2]/div[1]/img").click()
    time.sleep(3)

@when(u'click on Lead button in label configurators')
def step_impl(context):
    context.LLC=LeadLabelsConfiguratorPage(context.driver)
    context.LLC.click_lead_button()

@when(u'click on add label')
def step_impl(context):
    context.LLC.click_add_label()

@when(u'enter name of label')
def step_impl(context):
    context.LLC.enter_label_name()

@when(u'validate label added or not in same page')
def step_impl(context):
    # validation in same page
    assert context.LLC.validate_label_added()

@when(u'click on lead list')
def step_impl(context):
    context.LLC = LeadLabelsConfiguratorPage(context.driver)
    context.LLC.navigate_to_leads_list()



@then(u'check here in lead list that label is added or not')
def step_impl(context):
    assert context.LLC.check_label_in_lead_list()

@when(u'go to leads label configurator')
def step_impl(context):
    context.LLC = LeadLabelsConfiguratorPage(context.driver)
    context.LLC.go_to_leads_label_configurator()



@when(u'change position of label')
def step_impl(context):
    context.LLC.change_label_position()



@then(u'check in lead list that label position is change or not')
def step_impl(context):
    assert context.LLC.check_label_position()


@when(u'delete the added label')
def step_impl(context):
    context.LLC = LeadLabelsConfiguratorPage(context.driver)
    context.LLC.delete_added_label()



@then(u'validate here onlly by seeing count of lead labels')
def step_impl(context):
    assert context.LLC.validate_label_deletion()

@when(u'click on disable button')
def step_impl(context):
    context.LLC = LeadLabelsConfiguratorPage(context.driver)
    context.LLC.disable_label()



@then(u'check in lead list the label is disabled or not')
def step_impl(context):
    assert context.LLC.check_label_disabled()



@when(u'enable the label')
def step_impl(context):
    context.LLC = LeadLabelsConfiguratorPage(context.driver)
    context.LLC.enable_label()

@then(u'check in lead list labels wheather the able is enabled or not')
def step_impl(context):
    assert context.LLC.check_label_enabled()


@when(u'change colour of one label')
def step_impl(context):
    context.LLC = LeadLabelsConfiguratorPage(context.driver)
    context.LLC.change_colour_label()


@then(u'validate colour is changed or not')
def step_impl(context):
    assert context.LLC.is_Colour_Applied()
