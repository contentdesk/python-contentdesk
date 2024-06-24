from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
sys.path.append("..")
import service.cliArguments as cliArguments
from service.loadEnv import loadEnv


def main():
    environments = cliArguments.getEnvironment(sys)
    arguemnts = cliArguments.getArguments(sys)
    for environment in environments:
        targetCon = loadEnv(environment)

        driver = webdriver.Chrome()

        driver.get(targetCon["host"]+"/user/login")

        driver.implicitly_wait(5)

        title = driver.title

        username = driver.find_element(by=By.ID, value="username_input")
        username.send_keys(targetCon["userLocal"])
        password = driver.find_element(by=By.ID, value="password_input")
        password.send_keys(targetCon["passwdLocal"])
        driver.find_element(by=By.ID, value="_submit").click()

        driver.implicitly_wait(5)

        message = driver.find_element(by=By.CLASS_NAME, value="Messages")
        text = message.text
        print(text)

        driver.implicitly_wait(5)

        #https://ziggy.pim.tso.ch/#/configuration/attribute/startTime/edit

        print("Go To Attribute Site")

        driver.get(targetCon["host"]+"/#/configuration/attribute/startTime/edit")

        driver.implicitly_wait(5)

        attributeRequired = driver.find_element(by=By.ID, value="input_e46d4907-041e-4f79-aed1-8e8cadc7743b")

        attributeRequired.send_keys("Bswp. 15:00")

        saveButton = driver.find_element(by=By.CLASS_NAME, value="AknButton AknButton--apply save")
        saveButton.click()

        driver.quit()

        print(title)

if __name__ == '__main__':
    main()