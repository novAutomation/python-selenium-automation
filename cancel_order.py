from selenium import webdriver
from selenium .webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By

path = "/Users/northshore/Desktop/Automation/python-selenium-automation/chromedriver"
driver = webdriver.Chrome(executable_path=path)

driver.get('https://www.amazon.com/gp/help/customer/display.html ')
driver.maximize_window()
driver.find_element(By.ID, 'helpsearch').send_keys('Cancel order')
sleep(2)
act = ActionChains(driver)
act.send_keys(Keys.RETURN).perform()
print(driver.find_element(By.XPATH, "//h1").text + ' text is present on a page')
sleep(2)
driver.close()