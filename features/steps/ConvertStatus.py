from behave import*

from pages.ConvertStatusPage import ConvertStatusPage


@when(u'click on convert button')
def step_impl(context):
    context.CSP=ConvertStatusPage(context.driver)
    context.CSP.click_convert_button()



@when(u'click lost link')
def step_impl(context):
    context.CSP.click_lost_link()


@when(u'enter lost reason')
def step_impl(context):
    context.CSP.enter_lost_reason_text("no money")


@when(u'click on save')
def step_impl(context):
    context.CSP.click_savee_button()


@then(u'validate in Activity area and go to losts page and validate there')
def step_impl(context):
    assert context.CSP.isStatus_converted_To_Lost()

@when(u'change assigne')
def step_impl(context):
    context.CSP=ConvertStatusPage(context.driver)
    context.CSP.click_change_assignee()



@when(u'changes to active validate at same page')
def step_impl(context):
    assert context.CSP.isConverted_from_lost_to_Active()

@then(u'validate in open leads page')
def step_impl(context):
    context.CSP = ConvertStatusPage(context.driver)
    assert context.CSP.isActive_check_in_OpenFIlter()
