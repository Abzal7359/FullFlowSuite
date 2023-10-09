from behave import *

from pages.ChangeLabelsFromLeadsListPage import ChangeLabelsFromLeadsListPage
# from pages import ChangeLabelsFromLeadsListPage
from pages.ChangeLeadOwnerfromLeadsListPage import ChangeLeadOwnerFromLeadsListPage


# from pages import ChangeLeadOwnerFromLeadsListPage


@when(u'click on lead button to back toleads')
def step_impl(context):
   #    --------------------------------------------------------
    context.LeadOwn = ChangeLabelsFromLeadsListPage(context.driver)
    context.LeadOwn.click_lead_menu()

@Then(u'go on Lead owner coloumn change lead owner and Validate')
def step_impl(context):
    context.LeadOwner = ChangeLeadOwnerFromLeadsListPage(context.driver)
    assert context.LeadOwner.changeLeadOwner_and_Validate()

