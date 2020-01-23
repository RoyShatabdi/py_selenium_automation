from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

search_locator = driver.find_elements_by_id(
    "id-search-field").send_keys("python")
search_locator.send_keys(Keys.RETURN)
time.sleep(5)

driver.close()
