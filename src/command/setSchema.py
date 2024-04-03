import requests
import json

# Filter properties with rangeIncludes "schema:Number", "schema:Text", or "schema:URL"
# properties = [prop for prop in data["@graph"] if prop["@type"] == "rdf:Property" and
#              ("schema:Number" in prop["schema:rangeIncludes"] or
#               "schema:Text" in prop["schema:rangeIncludes"] or
#               "schema:URL" in prop["schema:rangeIncludes"])]

# Filter Type Class with @type rdfs:Class
# types = [type for type in data["@graph"] if type["@type"] == "rdfs:Class"]
# List of Class with @type rdfs:Class and 
# Create a Tree with subClassOf
# types = [type for type in data["@graph"] if type["@type"] == "rdfs:Class" and "rdfs:subClassOf" in type]

# Load the JSON-LD file from the URL
def load_jsonld(url):
    response = requests.get(url)
    data = response.json()
    return data

def createTreeTypes(data):
    types = [type for type in data["@graph"] if type["@type"] == "rdfs:Class" and "rdfs:subClassOf" in type]
    return types

def createTreeProperties(data):
    properties = [prop for prop in data["@graph"] if prop["@type"] == "rdf:Property" and
               (
                    "schema:Number" in prop["schema:rangeIncludes"] or
                    "schema:Text" in prop["schema:rangeIncludes"] or
                    "schema:URL" in prop["schema:rangeIncludes"]
                    #"schema:Date" in prop["schema:rangeIncludes"] or
                    #"schema:DateTime" in prop["schema:rangeIncludes"] or
                    #"schema:Time" in prop["schema:rangeIncludes"]
                )
                ]
    return properties

# create json file with Tree Types
def createJson(data, filename="../../output/types.json"):
    with open(filename, 'w') as f:
        json.dump(data, f)

# Create Akeneo attributes for the filtered properties
def checkData(data):
    for prop in data["@graph"]:
        if "rdfs:Class" in prop["@type"]:
            print ("CLASS: " + str(prop["rdfs:label"]))
            # Vererbung
            if "rdfs:subClassOf" in prop:
                print ("subClassOf: " + str(prop["rdfs:subClassOf"]))

        if "rdf:Property" in prop["@type"]:
            print ("PROPERTY: " + str(prop["rdfs:label"]))
            # Properties wird in Typ/Familie verwendet
            # --> Verwerbung beachten bspw. Place -> Hotel
            if "schema:domainIncludes" in prop:
                print ("domainIncludes: " + str(prop["schema:domainIncludes"]))

            # Attribut-Typ oder Verbindungs-Typ
            if "schema:rangeIncludes" in prop:
                print ("rangeIncludes: " + str(prop["schema:rangeIncludes"]))
            
            #create_attribute(prop)
            # Check if the property has a type in rangeIncludes
            #if "schema:DataType" in prop["schema:rangeIncludes"]:
                # Create association type in Akeneo
                #create_association_type(prop)
                #print ("DataType")

def main():
    url = "https://schema.org/version/latest/schemaorg-current-https.jsonld"
    data = load_jsonld(url)
    checkData(data)
    types = createTreeTypes(data)
    properties = createTreeProperties(data)
    createJson(types, filename="../../output/types.json")
    createJson(properties, filename="../../output/properties.json")

if __name__ == '__main__':
    main()