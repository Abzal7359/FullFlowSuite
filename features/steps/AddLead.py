import configparser
import time

from behave import *

from pages.LeadsPage import LeadsPage
from pages.LoginPage import LoginPage
from pages.NotesPage import NotesPage
from pages.TasksPage import TasksPage


from dataproviders import data

config = configparser.ConfigParser()
config.read(r'config.txt')



@given(u'user navigates to login page')
def step_impl(context):
    pass


@when(u'user enters login details mail as "{email}" and password as "{password}"')
def step_impl(context,email,password):
    #LOP=login page
    context.LOP=LoginPage(context.driver)
    context.LOP.enter_mail_and_password(email,password)


@when(u'click login button')
def step_impl(context):
    #DP = dashboard page
    context.DP=context.LOP.clickSignIn()


@when(u'click on sales and inside that clicks leads')
def step_impl(context):
    #LP=LeadsPage
    context.LP=context.DP.clickOnLeads()



@when(u'click Add Lead option')
def step_impl(context):
    context.LP.clickAddLead()

@when(u'enters mandatory fields in add leads page')
def step_impl(context):
    for row in context.table:
        global name
        global mail
        # c = data.name()
        name = data.c[0]
        mail = data.email

        # name=row["firstname"]
        # mail=row["email"]
        # context.LP.enter_Mandatory_Fields(row["firstname"],row["lastname"],row["email"],row["mobile"],row["description"])
        context.LP.enter_Mandatory_Fields(data.c[0], data.c[1], data.email, data.phone,   row["description"])


@when(u'click on save button')
def step_impl(context):
    context.LP.clickAddLeadSave()


@then(u'the lead details should added successfully')
def step_impl(context):

    assert context.LP.isLeadCreated(name,mail)


#tasks features

@when(u'click on tasks bar')
def step_impl(context):
    #TP=tasks page
    context.LP=LeadsPage(context.driver)
    context.TP=context.LP.clickOnTasksPage()

    time.sleep(float(config.get('waiting_time', 'min_wait')))




@when(u'click on create task')
def step_impl(context):
    context.TP.clickOnCreateTask()



@when(u'write task and set task details')
def step_impl(context):
    for r in context.table:
        context.TP.enterTaskDetails(r["textbox"], r["time"])




@when(u'click task save')
def step_impl(context):
    context.TP.clickOnTaskSave()


@then(u'ckeck task is created or not')
def step_impl(context):

    assert context.TP.isTaskCreated()

    time.sleep(float(config.get('waiting_time', 'min_wait')))


#task editing and comment adding feature


@when(u'click clone task and change priority and _save')
def step_impl(context):
    context.TP = TasksPage(context.driver)
    context.TP.click_to_clone_task()




@when(u'check task is cloned or not validate in activity _area')
def step_impl(context):
    context.TP = TasksPage(context.driver)
    assert context.TP.isTaskCreated()


@when(u'click on view details on task and add _comment')
def step_impl(context):
    context.LP = LeadsPage(context.driver)
    context.TP = context.LP.clickOnTasksPage()
    context.TP.add_comment()


@Then(u'check in activity _area')
def step_impl(context):
    context.TP = TasksPage(context.driver)
    assert context.TP.isCommentAddedInTask()


#notes page feature



@when(u'clickon Notes taskbar')
def step_impl(context):
    context.NP=NotesPage(context.driver)
    context.NP.click_onNotes()


@when(u'click on create notes')
def step_impl(context):
    context.NP.click_On_CreateNotes()


@when(u'write description in notes and save')
def step_impl(context):
    for i in context.table:
        context.NP.enter_note_in_box(i["notesDescription"])

@then(u'check the note is created or not')
def step_impl(context):
    context.NP = NotesPage(context.driver)
    assert context.NP.isNoteCreate()
    # context.DP=DashboardPage(context.driver)
    # context.DP.clickSignout()

