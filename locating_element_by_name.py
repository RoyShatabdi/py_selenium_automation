from selenium import webdriver
driver = webdriver.Chrome()
driver.get(
    "file:////Users/shatabdir/Documents/Personal Development/Python Selenium Binding /html_code.html")
login_form = driver.find_element_by_id('loginForm')
username = driver.find_element_by_name('username')
print(f'Input element: {username}')


driver.close()
