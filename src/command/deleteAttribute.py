import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import sys
sys.path.append("..")
import service.cliArguments as cliArguments
from service.loadEnv import loadEnv

def getAttributes():
    # Define the CSV URL
    csv_url = "https://docs.google.com/spreadsheets/d/187orB1Qx9YgeS8cVyI29DuGLhr-oj8yIiCIR5wqyqXk/gviz/tq?tqx=out:csv&sheet=setupAttribute"
    addition_csv_url = "https://docs.google.com/spreadsheets/d/187orB1Qx9YgeS8cVyI29DuGLhr-oj8yIiCIR5wqyqXk/gviz/tq?tqx=out:csv&sheet=additionalAttribute"

    df = pd.read_csv(csv_url)

    # filter df by enabled = false and attriuibute = false and association = true
    df_association = df[df["association"] == True]
    df_association = df_association[df_association["attribute"] == False]
    df_ignore = df[df["enabled"] == False]
    df_ignore = pd.concat([df_ignore, df_association], ignore_index=True)

    df_addition = pd.read_csv(addition_csv_url)
    df = pd.concat([df, df_addition])

    # filter df by enabled = false or enabled = empty
    df = df[df["enabled"] == True]
    df = df[df["attribute"] == True]

    print(df)

    # Convert the DataFrame to a JSON object
    json_data = df.to_json(orient="records")
    json_data_ignoreProperties = df_ignore.to_json(orient="records")

    # Write the JSON data to a file
    with open("../../output/index/akeneo/attributes.json", "w") as file:
        file.write(json_data)

    with open("../../output/index/ignoreProperties.json", "w") as file:
        file.write(json_data_ignoreProperties)

    return json.loads(json_data)

def startBrowser(target, attributeCode):
    driver = webdriver.Chrome()
    driver.get(target["host"]+"/user/login")

    driver.implicitly_wait(5)

    username = driver.find_element(by=By.ID, value="username_input")
    username.send_keys(target["userLocal"])
    password = driver.find_element(by=By.ID, value="password_input")
    password.send_keys(target["passwdLocal"])
    driver.find_element(by=By.ID, value="_submit").click()

    driver.implicitly_wait(5)

    title = driver.title

    #https://ziggy.pim.tso.ch/#/configuration/attribute/startTime/edit
    print("Go To Attribute Site")
    print (attributeCode)

    driverresponse = driver.get(target["host"]+"/#/configuration/attribute/"+str(attributeCode)+"/edit")
    driver.implicitly_wait(20)
    # check if driver.get not 404 Error
    if driverresponse.su == 404:
        print("Attribute not found")
        driver.close()
    else:
        #inputAttributeRequired = driver.find_element(by=By.TAG_NAME, value="textarea")
        #inputAttributeRequired.send_keys(attribute['guidelines.de_DE'])

        deletelink = driver.find_element(by=By.CLASS_NAME, value="delete").click()
        modal = driver.find_element(by=By.ID, value="modal-root")

        inputAttributeCode = modal.find_element(by=By.TAG_NAME, value="input")
        inputAttributeCode.send_keys(attributeCode)

        #find button with Text "Löschen"
        print("Delete Attribute!")
        deleteButton = modal.find_element(by=By.XPATH, value="//button[text()='Löschen']")
        #deleteButton.click()
        ActionChains(driver)\
            .context_click(deleteButton)\
            .perform()
        
        driver.implicitly_wait(10)

        driver.get(target["host"])

        driver.close()

        print(title)

def main():
    environments = cliArguments.getEnvironment(sys)
    arguemnts = cliArguments.getArguments(sys)
    #attributes = getAttributes()
    for environment in environments:
        print(environment)
        targetCon = loadEnv(environment)
        if arguemnts == None:
            # filter attributes guidlines.de_CH not empty
            print("No Arguments")
        else:
            for arg in arguemnts:
                print("Argument")
                print(arg)
                startBrowser(targetCon, arg)

if __name__ == '__main__':
    main()