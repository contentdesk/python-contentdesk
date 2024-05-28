import json
import requests
from akeneo.akeneo import Akeneo
import sys
sys.path.append("..")

from service.loadEnv import loadEnv, getEnvironment

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
    with open('../../output/index/ignoreProperties.json', 'r') as f:
        ignoreProperties = json.load(f)

    ignoreProperties = [prop["label"] for prop in ignoreProperties]

    return ignoreProperties

def getFullPropertiesbyType(code):
    with open('../../output/typesFullProperties.json', 'r') as f:
        typeFullProperties = json.load(f)
    
    typeSchema = "schema:"+code
    attributes = []
    #print("Get Full Properties: ", typeSchema)
    #print(typeFullProperties[typeSchema])
    if typeSchema in typeFullProperties:
        for item in typeFullProperties[typeSchema]:
            attributes.append(item.split(":")[1])

    return attributes

def removeIgnoreProperties(properties, ignoreProperties):
    newProperties = {}
    for prop in properties:
        #print("Check Ignore Property: ", prop)
        #print("Ignore Properties: ", ignoreProperties)
        if prop not in ignoreProperties:
            #print("Add Property: ", prop)
            newProperties[prop] = properties[prop]
        #else:
            #print("Ignore Property: ", prop)
    return newProperties

def merge_dicts(dict1, dict2):
    dict1.update(dict2)
    return dict1

def getTypeProperties(code):
    attributes = {}
    print("Get Family Attributes: ", code)
    #typeClass = getTypefromJson(code)
    #typeClass = getTypefromData(code, types)
    typeClassProperties = getFullPropertiesbyType(code)

    #attributes = attributes + typeClassProperties
    # add array to dict
    for prop in typeClassProperties:
        attributes[prop] = prop

    #if "rdfs:subClassOf" in typeClass:
        #print(type(typeClass["rdfs:subClassOf"]))
        #if type(typeClass["rdfs:subClassOf"]) == dict:
        #    attributes = merge_dicts(attributes, getTypeProperties(typeClass["rdfs:subClassOf"]["@id"].split(":")[1]))
        #elif type(typeClass["rdfs:subClassOf"]) == list:
        #    for typeChild in typeClass["rdfs:subClassOf"]:
        #        attributes = merge_dicts(attributes, getTypeProperties(typeChild["@id"].split(":")[1]))

    return attributes

def getFamilyAttributes(code, attributes):
    # Dict to Array
    attributes = merge_dicts(attributes, getTypeProperties(code))
    #print ("Complete Attributes befor Removed: ", attributes)
    ignoreProperties = getIgnoreProperties()
    #print ("Ignore Properties: ")
    #print(ignoreProperties)
    attributes = removeIgnoreProperties(attributes, ignoreProperties)
    # add sku to attributes dict
    attributes["sku"] = "sku"
    #print ("Clear Attributes: ", attributes)
    return attributes

def createFamily(family, akeneo):
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

    # Check if specific attributes are set
    # examples license needs add copyrightHolder and author
    # examples potentialAction needs traget
    if 'license' in attributes:
        attributes['copyrightHolder'] = 'copyrightHolder'
    
    if 'potentialAction' in attributes:
        attributes['target'] = 'target'

    body["attributes"] = attributes

    print("Attributes: ")
    print(body["attributes"])
    try:
        response = akeneo.patchFamily(code, body)
    except Exception as e:
        print("Error: ", e)
        print("patch Family: ", code)
        print("Response: ", response)
    return response

def createFamilies(target):
    families = getFamilies()
    for family in families:
        print ("CREATE - Family: "+ family["label"])
        if family["enabled"] == 1 and family["type"] == None or family["type"] == "additinalTypes":
            print("patch Family: ", family["label"])
            createFamily(family, target)
            print("FINISH - patch Family: ", family["label"])

def main():
    # Load environment variables
    #environments = getEnvironment()
    #environments = ["ziggy"]
    environments = ["demo"]

    print("START PATCH FAMILIES")
    for environment in environments:
        targetCon = loadEnv(environment)
        target = Akeneo(targetCon["host"], targetCon["clientId"], targetCon["secret"], targetCon["user"], targetCon["passwd"])
        createFamilies(target)
    print("FINISH PATCH FAMILIES")

if __name__ == '__main__':
    main()