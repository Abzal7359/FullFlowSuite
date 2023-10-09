import configparser
import time

from behave import *
from selenium.webdriver.common.by import By
from dataproviders import data


config = configparser.ConfigParser()
config.read(r'config.txt')

@when(u'get count of duplicates')
def step_impl(context):
    # context.DUP=DuplicatesPage(context.driver)
    # context.DUP.get_duplicates_count()
    global before_count
    before_count=context.driver.find_element(By.XPATH, "(//*[@id='duplicates']//span)[2]").text



@when(u'click on leads link to go back to lead list')
def step_impl(context):
    # context.DUP.click_on_lead_link()
    context.driver.find_element(By.XPATH,"//span[normalize-space()='Lead']").click()
    time.sleep(float(config.get('waiting_time', 'avg_wait')))



@when(u'click add lead button to add new lead')
def step_impl(context):
    # context.LP=LeadsPage(context.driver)
    # context.LP.clickAddLead()
    context.driver.find_element(By.XPATH, "//div[@class='flex justify-between px-2' and text()=' Add Lead ']").click()


@when(u'fill the details to add lead with same phone num and save')
def step_impl(context):
    # context.DUP = DuplicatesPage(context.driver)
    for r in context.table:
        # context.DUP.fill_details_same_num(r["firstName"],r["source"])
        global source
        context.driver.find_element(By.XPATH, "//input[@id='first-name ']").send_keys(r["firstName"])
        context.driver.find_element(By.XPATH, "//input[@id='phone-number']").send_keys(data.phone)
        # context.driver.find_element(By.XPATH, "//input[@id='phone-number']").send_keys(config.get('phone_num', 'same_num'))
        context.driver.find_element(By.XPATH, "(//input[@id='voice-search'])[1]").click()
        source=r["source"]
        dd = f"//label[contains(normalize-space(),'{source}')]"
        context.driver.find_element(By.XPATH, dd).click()
        time.sleep(float(config.get('waiting_time', 'min_wait')))
        context.driver.find_element(By.XPATH, "(//input[@id='voice-search'])[2]").click()
        time.sleep(1)
        context.driver.find_element(By.XPATH, "//label[normalize-space()='Instagram']").click()
        time.sleep(1)
        context.driver.find_element(By.XPATH, "(//button[normalize-space()='Save'])[1]").click()
        time.sleep(float(config.get('waiting_time', 'min_wait')))


@then(u'check duplicate count is increased or not')
def step_impl(context):
    # assert context.DUP.check_duplicate_created_or_not()
    #if toaster displayed means below code
    if context.driver.find_element(By.XPATH, "//app-toasts-container/div/div/div/div/div/div[2]/p[2]").is_displayed():
        k = context.driver.find_element(By.XPATH, "//div/form/div[1]/div[1]/div[1]/div[2]")
        context.driver.execute_script("arguments[0].click()", k)
        time.sleep(float(config.get('waiting_time', 'min_wait')))

    context.driver.find_element(By.XPATH, "(//table/tbody/tr/td[2]/div/span)[1]").click()
    time.sleep(float(config.get('waiting_time', 'avg_wait')))
    after_duplicate_count = context.driver.find_element(By.XPATH, "(//*[@id='duplicates']//span)[2]").text
    # print(after_duplicate_count, "after count")

    if int(after_duplicate_count) > int(before_count):
        # print(after_duplicate_count, befor_duplicate_count)
        context.driver.find_element(By.XPATH, "(//*[@id='duplicates']//span)[2]").click()



        time.sleep(float(config.get('waiting_time', 'min_wait')))
        # //app-duplicates/div[2]/div/div[]/div[1]
        zz = context.driver.find_elements(By.XPATH, "//app-duplicates/div[2]/div/div/div[1]")
        cou = len(zz)


        te = context.driver.find_element(By.XPATH, f"//app-duplicates/div[2]/div/div[{cou}]/div[1]").text
        if te == source:
            c=context.driver.find_element(By.XPATH,"(//a[normalize-space()='Activity'])[1]")
            context.driver.execute_script("arguments[0].click()",c)
            valtext=context.driver.find_element(By.XPATH,"//app-activity/div/div[2]/div[1]/div/div/div/div/div/p").text
            activityval=context.driver.find_element(By.XPATH,"//app-activity/div/div[2]/div/div[1]/div/div/p").text
            if "Lead enquired through another source" in valtext and activityval==source:
                assert True
        else:
            d = context.driver.find_element(By.XPATH, "(//a[normalize-space()='Activity'])[1]")
            context.driver.execute_script("arguments[0].click()", d)
            assert False
    else:
        d = context.driver.find_element(By.XPATH, "(//a[normalize-space()='Activity'])[1]")
        context.driver.execute_script("arguments[0].click()", d)
        assert False

#---------------------------------------------------------------------------
@when(u'fill the details to add lead with same mail and other num and save')
def step_impl(context):
    # context.DUP = DuplicatesPage(context.driver)
    for r in context.table:
        # context.DUP.fill_details_samemail_othernum(r["firstName"], r["source"])
        global source
        context.driver.find_element(By.XPATH, "//input[@id='email']").send_keys(data.email)
        # context.driver.find_element(By.XPATH,"//input[@id='email']").send_keys(config.get('phone_num', 'same_mail'))
        context.driver.find_element(By.XPATH, "//input[@id='first-name ']").send_keys(r["firstName"])
        context.driver.find_element(By.XPATH, "//input[@id='phone-number']").send_keys(data.other_phone)
        # context.driver.find_element(By.XPATH, "//input[@id='phone-number']").send_keys(config.get('email', 'other_num'))

        context.driver.find_element(By.XPATH, "(//input[@id='voice-search'])[1]").click()
        source=r["source"]
        dd = f"//label[contains(normalize-space(),'{source}')]"
        context.driver.find_element(By.XPATH, dd).click()
        time.sleep(float(config.get('waiting_time', 'min_wait')))
        context.driver.find_element(By.XPATH, "(//input[@id='voice-search'])[2]").click()
        time.sleep(1)
        context.driver.find_element(By.XPATH, "//app-select-dropdown/div/div/div/div[2]/label").click()
        time.sleep(1)
        context.driver.find_element(By.XPATH, "(//button[normalize-space()='Save'])[1]").click()
        time.sleep(float(config.get('waiting_time', 'min_wait')))


#----------------------------------------------------------------------------------


@when(u'fill the details to add lead with same mail and same phone number and save')
def step_impl(context):

    # for r in context.table:
        # context.DUP.fill_details_samemail_samenum(r["firstName"], r["source"])
    for r in context.table:
        global source
        # context.driver.find_element(By.XPATH,"//input[@id='email']").send_keys(config.get('phone_num', 'same_mail'))
        context.driver.find_element(By.XPATH, "//input[@id='email']").send_keys(data.email)
        context.driver.find_element(By.XPATH, "//input[@id='first-name ']").send_keys(r["firstName"])
        context.driver.find_element(By.XPATH, "//input[@id='phone-number']").send_keys(data.phone)
        # context.driver.find_element(By.XPATH, "//input[@id='phone-number']").send_keys(config.get('phone_num', 'same_num'))
        context.driver.find_element(By.XPATH, "(//input[@id='voice-search'])[1]").click()
        source=r["source"]
        dd = f"//label[contains(normalize-space(),'{source}')]"
        context.driver.find_element(By.XPATH, dd).click()
        time.sleep(float(config.get('waiting_time', 'min_wait')))
        c=context.driver.find_element(By.XPATH, "(//input[@id='voice-search'])[2]")
        context.driver.execute_script("arguments[0].click()",c)
        time.sleep(1)
        context.driver.find_element(By.XPATH, "//app-select-dropdown/div/div/div/div[2]/label").click()
        time.sleep(1)
        context.driver.find_element(By.XPATH, "(//button[normalize-space()='Save'])[1]").click()
        time.sleep(float(config.get('waiting_time', 'min_wait')))