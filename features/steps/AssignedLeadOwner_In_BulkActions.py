from behave import *

from pages.LeadsPage import LeadsPage





@when(u'select four leads in leadlist')
def step_impl(context):


    #----------------------------------------------
    context.LP = LeadsPage(context.driver)
    context.LP.selectFourLeads()


@when(u'click on Assigned lead owner button')
def step_impl(context):
    context.LP.click_assign_lead_owner_button()

@when(u'select assigned leader and click save')
def step_impl(context):
    context.LP.select_lead_owner()


@then(u'validate assigned leader is changed or not')
def step_impl(context):
    assert context.LP.isAssignedLeader_Changed()




#-------------------------
#code to send mail to bulk pepole
#
# @when(u'select two leads in leadlist')
# def step_impl(context):
#     context.LP = LeadsPage(context.driver)
#     context.LP.select_two_leads()
#
#
# @when(u'click on send email')
# def step_impl(context):
#     context.LP.click_send_email_button()
#
#
# @when(u'select sender')
# def step_impl(context):
#     context.LP.select_sender()
#
#
# @when(u'write subject line of mail as "{subject}"')
# def step_impl(context,subject):
#     context.LP.enter_subject(subject)
#
#
#
# @when(u'check tab pop is working or not in to area')
# def step_impl(context):
#
#     assert context.LP.is_popUp_displayed()
#
#
#
# @when(u'select placeholders')
# def step_impl(context):
#     context.LP = LeadsPage(context.driver)
#     context.LP.select_placeholders()
#
#
# @when(u'attach any documnet and validate document added or not')
# def step_impl(context):
#     context.LP.attach_document("C://Users/abzalhussain/Desktop/download.jpeg")
#
#     assert context.LP.is_document_added()
#
#
#
# @when(u'now click delete')
# def step_impl(context):
#     context.LP = LeadsPage(context.driver)
#     context.LP.click_delete_button()
#
#
# @when(u'check delete alert pop up is opened or not and click no on delete alert')
# def step_impl(context):
#     assert  context.LP.is_delete_alert_displayed()
#
#
# @when(u'now send mail button click')
# def step_impl(context):
#     context.LP = LeadsPage(context.driver)
#     context.LP.click_send_button()
#
#
#
# @Then(u'check on messages wheather the mail is send or not')
# def step_impl(context):
#     assert  context.LP.check_mail_isSent_or_not()
#
