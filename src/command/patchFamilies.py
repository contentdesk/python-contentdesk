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

import sys
sys.path.append("..")
import setting

ignoreProperties = setting.ignorePropertiesList

# Load properties.json
def getFamilies():
    with open('../../output/index/akeneo/families.json', 'r') as f:
        families = json.load(f)
    return families

def getTypefromJson(type):
    with open('../../output/types/'+type+'.json', 'r') as f:
        type = json.load(f)
    return type

def removeIgnoreProperties(properties):
    for prop in properties:
        if prop in ignoreProperties:
            properties.pop(prop)
    return properties

def getFamilyAttributes(code):
    attributes = {}
    print("Get Family Attributes: ", code)
    type = getTypefromJson(code)

    if type["properties"]:
        print("Type Properties: ", type["properties"])
        attributes = type["properties"]

    print ("Attributes: ", attributes)

    if type["rdfs:subClassOf"]:
        print("Parent Type: ", type["rdfs:subClassOf"]["@id"])
        parentType = getTypefromJson(type["rdfs:subClassOf"]["@id"].split(":")[1])
        if parentType["properties"]:
            print("Parent Type Properties: ", parentType["properties"])
            #attributes = attributes + parentType["properties"]
            attributes.update(parentType["properties"])
    
    print ("Attributes: ", attributes)
    return attributes


def createFamily(family):
    code = family["label"]

    # Set default values
    if family["attribute_requirements.ecommerce"] != None:
        attribute_requirements = family["attribute_requirements.ecommerce"].split(",")
    else:
        family["attribute_requirements.ecommerce"] = ["sku", "name", "image"]

    if family["attribute_as_label"] == None:
        family["attribute_as_label"] = "name"

    if family["attribute_as_image"] == None:
        family["attribute_as_image"] = "image"
    
    print("Attribute Requirements: ")
    print(attribute_requirements)

    # Create body
    body = {
        "code": code,
        "attribute_as_label": family["attribute_as_label"],
        "attribute_as_image": family["attribute_as_image"],
        "attribute_requirements": {
            "ecommerce": attribute_requirements,
            },
        "labels": {
            "en_US": family["label.en_US"],
            "de_CH": family["label.de_CH"],
            "fr_FR": family["label.fr_FR"],
            "it_IT": family["label.it_IT"],
            }
    }

    # Type specific attributes
    attributes = getFamilyAttributes(code)
    print("Attributes: ")
    print(attributes)
    body["attributes"] = attributes

    akeneo = Akeneo(
        AKENEO_HOST,
        AKENEO_CLIENT_ID,
        AKENEO_CLIENT_SECRET,
        AKENEO_USERNAME,
        AKENEO_PASSWORD
    )

    try:
        response = akeneo.patchFamily(code, body)
    except Exception as e:
        print("Error: ", e)
        print("patch Family: ", code)
        print("Response: ", response)
    return response

def createFamilies():
    families = getFamilies()
    for family in families:
        print ("Create Family: "+ family["label"])
        if family["enabled"] == 1:
            print("patch Family: ", family["label"])
            createFamily(family)

def main():
    createFamilies()

if __name__ == '__main__':
    main()