
from selenium.webdriver.common.by import By
from behave import then, when, given
from selenium.webdriver.support import expected_conditions as EC


PRIVACY_NOTICE_LINK = (By.XPATH, "//a[@href='https://www.amazon.com/privacy']")
TITLE_ELEMENT = (By.CSS_SELECTOR, 'div.help-content h1')


@given('Open Amazon T&C page')
def open_amazon_tc_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_original_windows(context):
    context.orig_windows = context.driver.current_window_handle


@when('Click on Amazon Privacy Notice link')
def click_amazon_privacy_notice_link(context):
    ele = context.driver.find_element(*PRIVACY_NOTICE_LINK)
    ele.click()


@when('Switch to the newly opened window')
def switch_to_newly_opened_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles
    context.driver.switch_to.window(windows[1])


@then('Verify Amazon Privacy Notice page is opened')
def verify_amazon_privacy_notice_page_opened(context):
    expected_title = 'Amazon.com Privacy Notice'
    actual_title = context.driver.find_element(*TITLE_ELEMENT).text
    assert actual_title == expected_title, f'Expected {expected_title}, but got {actual_title}'
    print(f'ACTUAL TITLE: {actual_title}')


@then('User can close new window and switch back to original')
def close_new_window(context):
    context.driver.close()
    context.driver.switch_to.window(context.orig_windows)




