from selenium import webdriver
driver = webdriver.Chrome()

driver.get(
    "file:////Users/shatabdir/Documents/Personal Development/Python Selenium Binding /html_code.html")

# locator group of element
login_form_class = driver.find_elements_by_class_name("content")

print(f'Login form class element  is: {login_form_class}')
