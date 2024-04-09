import requests
import json
import sys
sys.path.append("..")

import setting

ignoreTypesList = setting.ignoreTypesList
ignoreProperties = setting.ignorePropertiesList

# Load the JSON-LD file from the URL
def load_jsonld(url):
    response = requests.get(url)
    data = response.json()
    return data

def getTypes(data):
    types = [types for types in data["@graph"] if types["@type"] == "rdfs:Class"] or types["@id"] not in ignoreTypesList
    return types

def getPropertiesbyType(data, classType):
    print("Type: ", classType["@id"])
    #if "schema:domainIncludes" in prop:
    properties = {}
    for props in data["@graph"]:
        if props["@type"] == "rdf:Property":
            print("Property: ", props["@id"])
            if "schema:domainIncludes" in props:
                print("schema:domainIncludes: ", props["schema:domainIncludes"])
                print(type(props["schema:domainIncludes"]))
                if type(props["schema:domainIncludes"]) == str:
                    print("String")
                    if classType["@id"] in props["schema:domainIncludes"]["@id"]:
                        properties[props["@id"]] = props
                elif type(props["schema:domainIncludes"]) == dict:
                    print("Dict")
                    print(props["schema:domainIncludes"]["@id"])
                    if classType["@id"] in props["schema:domainIncludes"]["@id"]:
                        properties[props["@id"]] = props

    #properties = [props for props in data["@graph"] if props["@type"] == "rdf:Property" and "schema:domainIncludes" in props and type["@id"] in props["schema:domainIncludes"]]
    return properties

def createJson(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)

def clearFolder(folder):
    import os
    import glob
    files = glob.glob(folder)
    for f in files:
        os.remove(f)

def createJsonTypes(data, types, filepath):
    indexTypes = {}
    indexProperties = {}
    clearFolder(filepath + "*.json")
    for type in types:
        print("Check type: ", type["@id"])
        if type["@id"] not in ignoreTypesList:
            # get Properties by Type
            print ("Get Properties by Type: ", type["@id"])
            properties = getPropertiesbyType(data, type)
            type["properties"] = properties
            print("Create JSON file for type: ", type["@id"])
            filename = filepath + type["@id"].split(":")[1] + ".json"
            createJson(type, filename)
            # Create Index Types
            indexTypes[type["@id"]] = type
            # Create Index Properties
            for prop in properties:
                indexProperties[prop] = properties[prop]
    
    # Create Index JSON file
    filename = "../../output/index/types.json"
    createJson(indexTypes, filename)
    filename = "../../output/index/allProperties.json"
    createJson(indexProperties, filename)

def main():
    url = setting.schemaorgURL
    data = load_jsonld(url)
    types = getTypes(data)
    createJsonTypes(data, types, "../../output/types/")
    print("Types created successfully")

if __name__ == '__main__':
    main()