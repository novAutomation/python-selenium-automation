from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

path= "/Users/northshore/Desktop/Automation/python-selenium-automation/chromedriver"
driver = webdriver.Chrome(executable_path=path)

driver.get('https://www.amazon.com/gp/help/customer/display.html ')


driver.find_element(By.ID, 'helpsearch').send_keys('Cancel order', Keys.ENTER)

actual_text = driver.find_element(By.XPATH, "//div[@class = 'help-content']/h1").text
expected_text = 'Cancel Items or Orders'

assert expected_text == actual_text, f' Error, expected {expected_text} but got: {actual_text}'

driver.close()