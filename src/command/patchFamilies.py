import json
import requests
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
# Load properties.json
def getFamilies():
    with open('../../output/index/akeneo/families.json', 'r') as f:
        families = json.load(f)
    return families

def getTypefromJson(type):
    with open('../../output/types/'+type+'.json', 'r') as f:
        type = json.load(f)
    return type

def getTypefromData(type, types):
    print("Get Type: ", type)
    for t in types:
        print("Type: ", t)
        if t["@id"] == type:
            return t
    return None

def getTypes(data):
    types = [types for types in data["@graph"] if types["@type"] == "rdfs:Class"]
    return types

def load_jsonld(url):
    response = requests.get(url)
    data = response.json()
    return data

def getIgnoreProperties():
    with open('../../output/ignoreProperties.json', 'r') as f:
        ignoreProperties = json.load(f)
    return ignoreProperties

def removeIgnoreProperties(properties, ignoreProperties):
    newProperties = {}
    for prop in properties:
        if prop not in ignoreProperties:
            newProperties[prop] = properties[prop]
    return newProperties

def merge_dicts(dict1, dict2):
    dict1.update(dict2)
    return dict1

def getTypeProperties(code):
    attributes = {}
    print("Get Family Attributes: ", code)
    typeClass = getTypefromJson(code)
    #typeClass = getTypefromData(code, types)

    if typeClass["properties"]:
        attributes = merge_dicts(attributes, typeClass["properties"])

    if "rdfs:subClassOf" in typeClass:
        #print(type(typeClass["rdfs:subClassOf"]))
        if type(typeClass["rdfs:subClassOf"]) == dict:
            attributes = merge_dicts(attributes, getTypeProperties(typeClass["rdfs:subClassOf"]["@id"].split(":")[1]))
        elif type(typeClass["rdfs:subClassOf"]) == list:
            for typeChild in typeClass["rdfs:subClassOf"]:
                attributes = merge_dicts(attributes, getTypeProperties(typeChild["@id"].split(":")[1]))

    return attributes

def getFamilyAttributes(code, attributes):
    attributes = merge_dicts(attributes, getTypeProperties(code))
    #print ("Complete Attributes befor Removed: ", attributes)
    ignoreProperties = getIgnoreProperties()
    attributes = removeIgnoreProperties(attributes, ignoreProperties)
    # add sku to attributes dict
    attributes["sku"] = "sku"
    #print ("Clear Attributes: ", attributes)
    return attributes

def createFamily(family):
    code = family["label"]

    # Set default values
    if family["attribute_requirements.ecommerce"] != None:
        attribute_requirements = family["attribute_requirements.ecommerce"].split(",")
    else:
        attribute_requirements = family["attribute_requirements.ecommerce"] = ["sku", "name", "image"]

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
    attributes = {attr: attr for attr in family["attributes"].split(",")}
    attributes = getFamilyAttributes(code, attributes)
    #print("Attributes: ")
    #print(attributes)
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
        print ("CREATE - Family: "+ family["label"])
        if family["enabled"] == 1 and family["type"] == None:
            print("patch Family: ", family["label"])
            createFamily(family)
            print("FINISH - patch Family: ", family["label"])

def main():
    createFamilies()

if __name__ == '__main__':
    main()