from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://selenium.dev/")

locate_element_id = driver.find_elements_by_id("q")
locate_element_name = driver.find_elements_by_name("q")
locate_element_xpath = driver.find_elements_by_xpath("//*h1[1]")
locate_element_class = driver.find_elements_by_class_name(
    "banner-notification")

print(
    f'All the elements: {locate_element_id}{locate_element_name}{locate_element_xpath}{locate_element_class}')
driver.close()
