# PROMPT:
# Create a Array with all Types from schema.org with Properties by Type from url https://schema.org/version/latest/schemaorg-current-https.jsonld and save in a JSON file

import json
import urllib.request

def fetchJSONLD():
    url = "https://schema.org/version/latest/schemaorg-current-https.jsonld"
    response = urllib.request.urlopen(url)
    return json.loads(response.read())

def getType(data):
    types = {}
    for item in data["@graph"]:
        if item["@type"] == "rdfs:Class":
            types[item["@id"]] = []
            #properties_by_type[item["@id"]] = []
            if "rdfs:subClassOf" in item:
                sublcass = item["rdfs:subClassOf"]
                if isinstance(sublcass, list):
                    for subclass in sublcass:
                        types[item["@id"]] = []
                        types[item["@id"]].append(subclass["@id"])
                else:
                    if item["rdfs:subClassOf"]["@id"] not in types:
                        types[item["rdfs:subClassOf"]["@id"]] = []
                    types[item["@id"]].append(item["rdfs:subClassOf"]["@id"])

    return types

def getProperties(data):
    properties_by_type = {}
    for item in data["@graph"]:
        if item["@type"] == "rdf:Property":
                print("Check Property")
                print(item["@id"])
                if "schema:domainIncludes" in item:
                    domain_includes = item["schema:domainIncludes"]
                    if isinstance(domain_includes, list):
                        for domain in domain_includes:
                            if domain["@id"] not in properties_by_type:
                                properties_by_type[domain["@id"]] = []
                            properties_by_type[domain["@id"]].append(item["@id"])
                    else:
                        if domain_includes["@id"] not in properties_by_type:
                            properties_by_type[domain_includes["@id"]] = []
                        properties_by_type[domain_includes["@id"]].append(item["@id"])
    return properties_by_type

def getPropertiesByType(data):
    
    return 

def getSubclass(data):
    #
    return

def getTypesAndProperties(data):
    types = getType(data)
    properties_by_type = getProperties(data)
    return types, properties_by_type

def setTypesProperties(types, properties_by_type):
    typesProperties = {}

    for type in types:
        print(type)
        print(types[type])
        # if type a array
        if isinstance(types[type], list):
            for subclass in types[type]:
                print(subclass)
                if subclass in properties_by_type:
                    print(properties_by_type[subclass])
                    typesProperties[type] = properties_by_type[subclass]
        else:
            if subclass in properties_by_type:
                print(properties_by_type[types[type]])
                typesProperties[type] = properties_by_type[types[type]]

    return typesProperties


def main():
    dataURL = fetchJSONLD()
    types, properties_by_type = getTypesAndProperties(dataURL)

    typeProperties = setTypesProperties(types, properties_by_type)

    with open("../../output/typesProperties.json", "w") as file:
        json.dump(properties_by_type, file)
    
    with open("../../output/typesSubclass.json", "w") as file:
        json.dump(types, file)

    print(typeProperties)

    with open("../../output/typesFullProperties.json", "w") as file:
        json.dump(typeProperties, file)

if __name__ == "__main__":
    main()
    pass