import json
from akeneo.akeneo import Akeneo
from os import getenv
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

AKENEO_HOST = getenv('AKENEO_HOST')
AKENEO_CLIENT_ID = getenv('AKENEO_CLIENT_ID')
AKENEO_CLIENT_SECRET = getenv('AKENEO_CLIENT_SECRET')
AKENEO_USERNAME = getenv('AKENEO_USERNAME')
AKENEO_PASSWORD = getenv('AKENEO_PASSWORD')

# Load properties.json
def getAttributes():
    with open('../../output/index/akeneo/attributes.json', 'r') as f:
        attributes = json.load(f)
    return attributes

def createAttribute(attribute):
    akeneo = Akeneo(
        AKENEO_HOST,
        AKENEO_CLIENT_ID,
        AKENEO_CLIENT_SECRET,
        AKENEO_USERNAME,
        AKENEO_PASSWORD
    )
    code = attribute["label"]

    # Set default values
    if attribute["available_locales"] == None:
        attribute["available_locales"] = []

    if attribute["allowed_extensions"] == None:
        attribute["allowed_extensions"] = []

    if attribute["localizable"] == None:
        attribute["localizable"] = False
    
    if attribute["scopable"] == None:
        attribute["scopable"] = False
    
    if attribute["unique"] == None:
        attribute["unique"] = False

    if attribute["useable_as_grid_filter"] == None:
        attribute["useable_as_grid_filter"] = False

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

    try:
        response = akeneo.patchAttribut(code, body)
    except Exception as e:
        print("Error: ", e)
        print("patch Attribute: ", code)
        print("Response: ", response)
    return response

def createAttributesinAkeneo():
    attributes = getAttributes()
    for attribute in attributes:
        print ("Check Property if Attribut: "+ attribute["label"])
        if attribute["pimType"] == "attribute":
            print("patch Attribute: ", attribute["label"])
            createAttribute(attribute)

def main():
    createAttributesinAkeneo()

if __name__ == '__main__':
    main()