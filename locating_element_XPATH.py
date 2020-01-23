from selenium import webdriver
driver = webdriver.Chrome()

driver.get(
    "file:////Users/shatabdir/Documents/Personal Development/Python Selenium Binding /html_code.html")

login_form_absolute = driver.find_element_by_xpath("/html/body/form[1]")
login_form__relative = driver.find_element_by_xpath("//form[1]")
login_form__id = driver.find_element_by_xpath(
    "//form[@id=loginform]")  # relative file more specified

print(
    f'login form is: {login_form_absolute} {login_form__relative}{login_form__id}')
