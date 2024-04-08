import requests
import json
import sys
sys.path.append("..")

import config

ignoreTypes = config.ignoreTypes

# Load the JSON-LD file from the URL
def load_jsonld(url):
    response = requests.get(url)
    data = response.json()
    return data

def getTypes(data):
    types = [type for type in data["@graph"] if type["@type"] == "rdfs:Class"] and type["@id"] not in ignoreTypes
    return types

def createJsonTypes(types, filepath):
    for type in types:
        print("Check type: ", type["@id"])
        if type["@id"] not in ignoreTypes:
            print("Create JSON file for type: ", type["@id"])
            filename = filepath + type["@id"].split(":")[1] + ".json"
            with open(filename, 'w') as f:
                json.dump(type, f)
    
def main():
    url = config.schemaorgURL
    data = load_jsonld(url)
    types = getTypes(data)
    createJsonTypes(types, "../../output/types/")
    print("Types created successfully")

if __name__ == '__main__':
    main()