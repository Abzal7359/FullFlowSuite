import configparser
import time

from behave import *

from pages.ApplyingFilter_createTabPage import ApplyingFilterCreateTab
from pages.DashboardPage import DashboardPage
config = configparser.ConfigParser()
config.read(r'config.txt')



@when(u'click onleads')
def step_impl(context):
    # -----------------------------------------------
    context.DP = DashboardPage(context.driver)
    context.DP.clickOnLeads()
    time.sleep(float(config.get('waiting_time', 'avg_wait')))

@then(u'check in leads page that it automatically in openfilter')
def step_impl(context):
    context.AFCT = ApplyingFilterCreateTab(context.driver)
    assert context.AFCT.isDefault_in_openFilter()

@when(u'click on filterbutton')
def step_impl(context):
    context.AFCT = ApplyingFilterCreateTab(context.driver)
    context.AFCT.click_add_filters_button()

@when(u'select attributes you want to filter "{source}" and "{type}" andtabName "{name}"')
def step_impl(context,source,type,name):
    context.AFCT.select_filter_type(source, type)
    context.AFCT.click_create_tab()
    context.AFCT.enter_tab_name(name)

@when(u'click _create')
def step_impl(context):
    context.AFCT.click_create_button()

@when(u'validate tab is created or _not')
def step_impl(context):
    assert context.AFCT.is_TAB_Created()



@when(u'click on new filter tab and _delte')
def step_impl(context):
    context.AFCT = ApplyingFilterCreateTab(context.driver)
    context.AFCT.click_delete_filter()

@When(u'now check tab is deleted or _not')
def step_impl(context):
    assert context.AFCT.is_FIlterTab_Delted()

@When(u'edit filter name and check name is updated or not')
def step_impl(context):

    context.AFCT = ApplyingFilterCreateTab(context.driver)
    assert context.AFCT.edit_new_filter_name()