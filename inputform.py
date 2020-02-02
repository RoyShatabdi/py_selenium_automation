from selenium import webdriver
import time
from selenium.webdriver import ActionChains
import selenium.webdriver.common.keys as Keys


driver = webdriver.Chrome()
driver.maximize_window()  # Mazimine the browser window

driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

# Check if in right site
assert 'Selenium Easy Demo - Simple Form to Automate using Selenium' in driver.title

button = driver.find_element_by_class_name('btn-default')

# print(button.get_attribute('innerHTML'))  # printing button name

assert 'Show Message' in driver.page_source

form_field = driver.find_element_by_xpath('//*[@id="user-message"]')
assert 'Please enter your Message' in driver.page_source
form_field.clear()

form_field.send_keys('This is Shatabdi')

button.click()

# output_message = driver.find_elements_by_id('display')
assert 'This is Shatabdi' in driver.page_source

time.sleep(2)
driver.close()
