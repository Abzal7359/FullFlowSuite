import time

from behave import *

from pages.ChangeCreatedDateOrderInLeadsListPage import ChangeCreatedDateOrderInLeadsListPage
from pages.ChangeLabelsFromLeadsListPage import ChangeLabelsFromLeadsListPage




@when(u'clickon lead button to back toleads')
def step_impl(context):



    context.LeadOwn = ChangeLabelsFromLeadsListPage(context.driver)
    context.LeadOwn.click_lead_menu()


@when(u'click on descending date button')
def step_impl(context):
    context.CD=ChangeCreatedDateOrderInLeadsListPage(context.driver)
    context.CD.click_descending_date_button()


@then(u'validate dates in descending order or not')
def step_impl(context):
    assert context.CD.is_in_descendingOrder()
    time.sleep(3)


@when(u'click on ascending date button')
def step_impl(context):
    context.CD = ChangeCreatedDateOrderInLeadsListPage(context.driver)
    context.CD.click_ascending_date_button()


@then(u'validate dates in ascending order or not')
def step_impl(context):
    context.CD = ChangeCreatedDateOrderInLeadsListPage(context.driver)
    assert context.CD .is_in_ascendingOrder()


