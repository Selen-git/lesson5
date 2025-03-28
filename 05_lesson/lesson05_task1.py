from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/classattr

button = driver.find_element_by("button.btn-primary")
button.click()

driver.quit()
