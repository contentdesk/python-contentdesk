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
def getProperties():
    with open('/output/index/properties.json', 'r') as f:
        properties = json.load(f)

    return properties


# Check if properties.json is not in ignoreProperties.json
def getIgnoreProperties():
    with open('/output/ignoreProperties.json', 'r') as f:
        ignore_properties = json.load(f)

    return ignore_properties

def createAttribute(prop):
    akeneo = Akeneo(
        AKENEO_HOST,
        AKENEO_CLIENT_ID,
        AKENEO_CLIENT_SECRET,
        AKENEO_USERNAME,
        AKENEO_PASSWORD
    )
    code = prop["@id"].split(":")[1]
    body = {
        "code": code,
        "type": "pim_catalog_text",
        "group": "schemaorg"
    }
    return akeneo.patchAttribut(prop, body)

def createAttributesinAkeneo():
    properties = getProperties()
    ignoreProperties = getIgnoreProperties()
    for prop in properties:
        print("Check Property: ", prop["@id"])
        if prop not in ignoreProperties:
            print("Create Attribute: ", prop["@id"])
            createAttribute(prop)

def main():
    createAttributesinAkeneo()


if __name__ == '__main__':
    main()