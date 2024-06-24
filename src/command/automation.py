from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://ziggy.pim.tso.ch/user/login")

driver.implicitly_wait(5)

title = driver.title

username = driver.find_element(by=By.ID, value="username_input")
username.send_keys("thomas.solenthaler@tso.ch")
password = driver.find_element(by=By.ID, value="password_input")
password.send_keys("tso123")
submit_button = driver.find_element(by=By.ID, value="_submit")
submit_button.click()

message = driver.find_element(by=By.CLASS_NAME, value="Messages")
text = message.text
print(text)

driver.quit()

print(title)