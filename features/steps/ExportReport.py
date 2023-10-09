from behave import*


from pages.ExportReportPage import ExportReportPage


@when(u'click on Export')
def step_impl(context):
    #-----------------------------------------------
    context.EP=ExportReportPage(context.driver)
    context.EP.click_export_button()


@when(u'now select which columns you need in report')
def step_impl(context):
    context.EP.select_export_column()

@when(u'click on export button')
def step_impl(context):
    context.EP.click_SAVE_button()


@when(u'now go to downloads section')
def step_impl(context):
    context.EP.navigate_to_downloads_section()



@then(u'here validate report generated or not')
def step_impl(context):
    assert context.EP.is_report_created()




