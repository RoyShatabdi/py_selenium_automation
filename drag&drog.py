from selenium import webdriver
import time
import selenium.webdriver.common.keys as Keys
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.seleniumeasy.com/test/drag-and-drop-demo.html')

source = driver.find_elements_by_name('Draggable 2')
destination = driver.find_elements_by_id('mydropzone')


actions = ActionChains(driver)

actions.drag_and_drop(source, destination).perform()

time.sleep(2)
# driver.close()
