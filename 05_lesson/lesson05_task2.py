from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/dynamicid")

button = driver.find_element("//button[contains(@onclick, 'buttonClick')]")

bitton.click()

driver.quit()
