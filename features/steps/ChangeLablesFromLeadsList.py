
from behave import *

from pages.ChangeLabelsFromLeadsListPage import ChangeLabelsFromLeadsListPage


# from pages import ChangeLabelsFromLeadsListPage


@when(u'click on lead button to back to leads')
def step_impl(context):
    pass
    # context.Label=ChangeLabelsFromLeadsListPage(context.driver)
    # context.Label.click_lead_menu()


@when(u'go on labels column and change labels')
def step_impl(context):
    context.Label = ChangeLabelsFromLeadsListPage(context.driver)
    context.Label.changeLabels()


@Then(u'validate in Activity area wheather labels are changed or not')
def step_impl(context):
    assert context.Label.are_labels_changed()

