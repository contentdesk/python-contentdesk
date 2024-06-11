import json
import pandas as pd
from akeneo.akeneo import Akeneo

import sys
sys.path.append("..")

from service.loadEnv import loadEnv, getEnvironment
import service.cliArguments as cliArguments

def readCsv(url):
    # Read the CSV data into a pandas DataFrame
    df = pd.read_csv(url)
    return df

def getAttributes():
    # Define the CSV URL
    csv_url = "https://docs.google.com/spreadsheets/d/187orB1Qx9YgeS8cVyI29DuGLhr-oj8yIiCIR5wqyqXk/gviz/tq?tqx=out:csv&sheet=setupAttribute"
    addition_csv_url = "https://docs.google.com/spreadsheets/d/187orB1Qx9YgeS8cVyI29DuGLhr-oj8yIiCIR5wqyqXk/gviz/tq?tqx=out:csv&sheet=additionalAttribute"

    df = readCsv(csv_url)

    # filter df by enabled = false and attriuibute = false and association = true
    df_association = df[df["association"] == True]
    df_association = df_association[df_association["attribute"] == False]
    df_ignore = df[df["enabled"] == False]
    df_ignore = pd.concat([df_ignore, df_association], ignore_index=True)

    df_addition = readCsv(addition_csv_url)
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

# Load properties.json
def getAttributesfromJSON():
    with open('../../output/index/akeneo/attributes.json', 'r') as f:
        attributes = json.load(f)
    return attributes

def createAttribute(attribute, akeneo):
    code = attribute["label"]

    if attribute["group"] == None:
        attribute["group"] = "other"

    # Set default values
    if attribute["available_locales"] == None:
        attribute["available_locales"] = []

    if attribute["allowed_extensions"] == None:
        attribute["allowed_extensions"] = []
    elif type(attribute["allowed_extensions"]) == str:
        attribute["allowed_extensions"] = attribute["allowed_extensions"].split(",")

    if attribute["localizable"] == None:
        attribute["localizable"] = False
    
    if attribute["scopable"] == None:
        attribute["scopable"] = False
    
    if attribute["unique"] == None:
        attribute["unique"] = False

    if attribute["useable_as_grid_filter"] == None:
        attribute["useable_as_grid_filter"] = False

    # Create body
    body = {
        "code": code,
        "type": attribute["type"],
        "group": attribute["group"],
        "localizable": attribute["localizable"],
        "scopable": attribute["scopable"],
        "available_locales": attribute["available_locales"],
        "unique": attribute["unique"],
        "useable_as_grid_filter": attribute["useable_as_grid_filter"],
        "max_characters": attribute["max_characters"],
        #"wysiwyg_enabled": attribute["wysiwyg_enabled"],
        #"decimals_allowed": attribute["decimals_allowed"],
        #"negative_allowed": attribute["negative_allowed"],
        "metric_family": attribute["metric_family"],
        "default_metric_unit": attribute["default_metric_unit"],
        "allowed_extensions": attribute["allowed_extensions"],
        "max_file_size": attribute["max_file_size"],
        "labels": {
            "en_US": attribute["label.en_US"],
            "de_CH": attribute["label.de_CH"],
            "fr_FR": attribute["label.fr_FR"],
            "it_IT": attribute["label.it_IT"],
            }
    }

    # Type specific attributes
    if attribute["type"] == "pim_catalog_textarea":
        if attribute["wysiwyg_enabled"] != None:
            body["wysiwyg_enabled"] = attribute["wysiwyg_enabled"]
        else:
            body["wysiwyg_enabled"] = False
    
    if attribute["type"] == "pim_catalog_number" or attribute["type"] == "pim_catalog_metric" or attribute["type"] == "pim_catalog_price_collection":
        if attribute["decimals_allowed"] != None:
            body["decimals_allowed"] = attribute["decimals_allowed"]
        else:
            body["decimals_allowed"] = False
        
        if attribute["type"] != "pim_catalog_price_collection":
            if attribute["negative_allowed"] != None:
                body["negative_allowed"] = attribute["negative_allowed"]
            else:
                body["negative_allowed"] = False

    try:
        response = akeneo.patchAttribut(code, body)
    except Exception as e:
        print("Error: ", e)
        print("patch Attribute: ", code)
        print("Response: ", response)
    return response

def createAttributesinAkeneo(target, importAttributes = None):
    attributes = getAttributes()
    for attribute in attributes:
        if importAttributes != None:
            if attribute["label"] in importAttributes:
                pass
            else:
                continue   
            print ("Check Property if Attribut: "+ attribute["label"])
            if attribute["attribute"] == True:
                print("patch Attribute: ", attribute["label"])
                createAttribute(attribute, target)

def main():
    environments = cliArguments.getEnvironment(sys)
    arguments = cliArguments.getArguments(sys)

    print("START PATCH ATTRIBUTES")
    for environment in environments:
        targetCon = loadEnv(environment)
        target = Akeneo(targetCon["host"], targetCon["clientId"], targetCon["secret"], targetCon["user"], targetCon["passwd"])
        createAttributesinAkeneo(target, arguments)
    print("FINISH PATCH ATTRIBUTES")

if __name__ == '__main__':
    main()