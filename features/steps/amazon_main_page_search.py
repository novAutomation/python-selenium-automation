
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

IPAD_IMAGE = (By.XPATH, "//div[@class='a-section aok-relative s-image-fixed-height']/img[@src='https://m.media-amazon.com/images/I/61con7QLTrL._AC_UY218_.jpg']")


@given('Open Amazon page')
def open_amazon_page(context):
    context.app.homePage.open()


@when('Search for table')
def search_table(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')


@when('Click search icon')
def click_search_icon(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@when('Click Orders')
def click_orders(context):
    context.app.headerComponent.click_orders()


@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.ID, 'nav-cart-count').click()


@when('User search for Ipad')
def search_ipad(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Ipad')


@when('User click on Ipad')
def click_on_ipad_image(context):
    e = context.driver.wait.until(EC.element_to_be_clickable((IPAD_IMAGE)))
    e.click()


@when('Click Add to Cart button')
def click_add_to_cart_button(context):
    context.driver.find_element(By.ID, "submit.add-to-cart").click()


@when('Click Add button')
def click_add_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "span#attachSiAddCoverage span input").click()





