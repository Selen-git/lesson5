from selenium import webdriver

browser = webdriver.Firefox()

browser.get('http://the-internet.herokuapp.com/login')

username = browser.find_element_by_id('username')
username.send_keys('tomsmith')

password = browser.find_element_by_id('password')
password.send_keys('SuperSecretPassword!')

login_button = browser.find_element('//button[@type="submit"]')
login_button.click()

succes_message = browser.find_element('.flash.succes').text
print(succes_message)

browser.quit()






















