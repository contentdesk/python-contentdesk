import requests
import json
import sys
sys.path.append("..")

import setting

ignoreProperties = setting.ignorePropertiesList
indexPropertiesAllneededTypes = setting.indexPropertiesAllneededTypesList

# Load the JSON-LD file from the URL
def load_jsonld(url):
    response = requests.get(url)
    data = response.json()
    return data

def getProperties(data):
    properties = [prop for prop in data["@graph"] if prop["@type"] == "rdf:Property"] or prop["@id"] not in ignoreProperties
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

def createJsonProperties(data, properties, filepath):
    indexProperties = {}
    clearFolder(filepath + "*.json")
    for prop in properties:
        print("Check properties: ", prop["@id"])
        if prop["@id"] not in ignoreProperties:
            print("Create JSON file for properties: ", prop["@id"])
            filename = filepath + prop["@id"].split(":")[1] + ".json"
            createJson(prop, filename)
            # Create Index Types
            indexProperties[prop["@id"]] = prop
    
    # Create Index JSON file
    filename = "../../output/index/properties.json"
    createJson(indexProperties, filename)

def main():
    url = setting.schemaorgURL
    data = load_jsonld(url)
    properties = getProperties(data)
    createJsonProperties(data, properties, "../../output/properties/")
    print("properties created successfully")

if __name__ == '__main__':
    main()