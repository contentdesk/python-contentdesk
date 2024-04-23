# PROMPT:
# Create a Array with all Types from schema.org with Properties by Type from url https://schema.org/version/latest/schemaorg-current-https.jsonld and save in a JSON file

import json
import urllib.request

def fetchJSONLD():
    url = "https://schema.org/version/latest/schemaorg-current-https.jsonld"
    response = urllib.request.urlopen(url)
    return json.loads(response.read())

def getTypesAndProperties(data):
    types = []
    properties_by_type = {}

    for item in data["@graph"]:
        if item["@type"] == "rdfs:Class":
            types.append(item["@id"])
            #properties_by_type[item["@id"]] = []
        
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

    return types, properties_by_type

def main():
    data = fetchJSONLD()
    types, properties_by_type = getTypesAndProperties(data)

    with open("../../output/types_properties.json", "w") as file:
        json.dump(properties_by_type, file)
    
    with open("../../output/types.json", "w") as file:
        json.dump(types, file)

    for type_name, properties in properties_by_type.items():
        print(type_name)
        print(properties)


if __name__ == "__main__":
    main()
    pass