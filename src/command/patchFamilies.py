import json
import requests
import pandas as pd
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

# DEBUG
def addToFile(code, data):
    with open("../../output/index/akeneo/families/"+code+".json", "w") as file:
        file.write(json.dumps(data))

# DEBUG - Log
def addToLogFile(code, data):
    with open("../../output/logs/families/"+code+".json", "w") as file:
        file.write(json.dumps(data))

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
    # add sku to attributes dict
    attributes["sku"] = "sku"
    attributes["name"] = "name"
    #print ("Clear Attributes: ", attributes)
    return attributes

def removeProperties(code, attributes):
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

def searchParentType(type, types, searchType, check = False):
    if 'parent' in type:
        if type['parent'] != None:
            #print("Parent Type: ", type['parent'])
            if type['parent'] == searchType:
                #print("Found Parent Type: ", type['parent'])
                check = True
            else:
                # find in types array type['parent'] as type['label']
                parent = [parent for parent in types if parent["label"] == type['parent']]
                #print("Check Parent: ")
                #print(parent)
                check = searchParentType(parent, types, searchType, check)
                #print("END CHECK Next PARENT")
    else:
        check = False
    return check

def getParentAttributes(type, types, attributes):
    if type['attributes'] != None:
        #print("Merge Parent Attributes:")
        # make type['attributes'] to dict with two values
        typeAttributes = {attr: attr for attr in type['attributes'].split(",")}
        # Merge Attributes
        #print(typeAttributes)
        attributes = merge_dicts(attributes, typeAttributes)
    if 'parent' in type:
        if type['parent'] != None:
            #print("Parent Type: ", type['parent'])
            # find in types array type['parent'] as type['label']
            parent = [parent for parent in types if parent["label"] == type['parent']]
            #print("Check Parent: ")
            #print(parent)
            getParentAttributes(parent[0], types, attributes)

    return attributes

def getParentAttributesRequirements(type, types, attribute_requirements):
    if type['attribute_requirements.ecommerce'] != None:
        #print("Merge Parent Attributes Requirements:")
        # make type['attributes'] to dict with two values
        typeAttributes = {attr: attr for attr in type['attribute_requirements.ecommerce'].split(",")}
        # Merge Attributes
        #print(typeAttributes)
        attribute_requirements = merge_dicts(attribute_requirements, typeAttributes)
    if 'parent' in type:
        if type['parent'] != None:
            #print("Parent Type: ", type['parent'])
            # find in types array type['parent'] as type['label']
            parent = [parent for parent in types if parent["label"] == type['parent']]
            #print("Check Parent: ")
            #print(parent)
            attribute_requirements = getParentAttributesRequirements(parent[0], types, attribute_requirements)

    return attribute_requirements

def createFamily(family, families, akeneo):
    code = family["label"]

    # Set default values
    if family["attribute_requirements.ecommerce"] != None:
        attribute_requirements = {attrRequ: attrRequ for attrRequ in family["attribute_requirements.ecommerce"].split(",")}
        #attribute_requirements = family["attribute_requirements.ecommerce"].split(",")
    else:
        attribute_requirements = {"sku": "sku", "name": "name", "image": "image"}

    if family["attribute_as_label"] == None:
        family["attribute_as_label"] = "name"

    if family["attribute_as_image"] == None:
        family["attribute_as_image"] = "image"

    
    attribute_requirements = getParentAttributesRequirements(family, families, attribute_requirements)
    
    #print("Attribute Requirements: ")
    #print(attribute_requirements)

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
    if family["attributes"] != None:
        attributes = {attr: attr for attr in family["attributes"].split(",")}
    else:
        attributes = {}
    attributes = getFamilyAttributes(code, attributes)
    #print("Attributes: ")
    #print(attributes)

    # add Parent Attributes
    attributes = getParentAttributes(family, families, attributes)

    # Check if specific attributes are set
    # examples license needs add copyrightHolder and author
    # examples potentialAction needs traget
    if 'image' in attributes:
        attributes['image_description'] = 'image_description'

    if 'openingHoursSpecification' in attributes:
        attributes['google_opening_hours_use'] = 'google_opening_hours_use'

    # StarRating and Type Hotel
    if 'starRating' in attributes and code == "Hotel":
        attributes['garni'] = 'garni'
        attributes['superior'] = 'superior'

    # Type MeetingRoom
    if code == "MeetingRoom":
        attributes['seating_banquet'] = 'seating_banquet'
        attributes['seating_bar_table'] = 'seating_bar_table'
        attributes['seating_block'] = 'seating_block'
        attributes['seating_boardroom'] = 'seating_boardroom'
        attributes['seating_concert'] = 'seating_concert'
        attributes['seating_seminar'] = 'seating_seminar'
        attributes['seating_ushape'] = 'seating_ushape'
        # remove Key attribute petAllowed
        attributes.pop('petsAllowed', None)
        #attributes.pop('petsAllowed', None)
        #attributes.pop('weatherDependency', None)
        #attributes.pop('byMonth', None)
        #attributes.pop('dayOfWeek', None)
        #attributes.pop('daytime', None)
        #attributes.pop('duration', None)
        #attributes.pop('priceRange', None)
        #attributes.pop('openingHoursSpecification', None)
        #attributes.pop('openingHours', None)


    # Image Winter and Summer by Type Hotel
    if code == "Hotel":
        attributes['image_winter'] = 'image_winter'
        attributes['image_summer'] = 'image_summer'

    # Images / Gallery
    if 'image_01_scope' in attributes:
        attributes['google_image_gallery_use_pro_channel'] = 'google_image_gallery_use_pro_channel'
        attributes['image_01_scope_description'] = 'image_01_scope_description'
    if 'image_02_scope' in attributes:
        attributes['image_02_scope_description'] = 'image_02_scope_description'
    if 'image_03_scope' in attributes:
        attributes['image_03_scope_description'] = 'image_03_scope_description'
    if 'image_04_scope' in attributes:
        attributes['image_04_scope_description'] = 'image_04_scope_description'
    if 'image_05_scope' in attributes:
        attributes['image_05_scope_description'] = 'image_05_scope_description'
    if 'image_06_scope' in attributes:
        attributes['image_06_scope_description'] = 'image_06_scope_description'
    if 'image_07_scope' in attributes:
        attributes['image_07_scope_description'] = 'image_07_scope_description'
    if 'image_08_scope' in attributes:
        attributes['image_08_scope_description'] = 'image_08_scope_description'
    if 'image_09_scope' in attributes:
        attributes['image_09_scope_description'] = 'image_09_scope_description'
    if 'image_10_scope' in attributes:
        attributes['image_10_scope_description'] = 'image_10_scope_description'

    if 'geo' in attributes:
        attributes['longitude'] = 'longitude'
        attributes['latitude'] = 'latitude'

    if 'address' in attributes:
        attributes['streetAddress'] = 'streetAddress'
        attributes['postalCode'] = 'postalCode'
        attributes['addressLocality'] = 'addressLocality'
        attributes['addressCountry'] = 'addressCountry'
        attributes['addressRegion'] = 'addressRegion'
        attributes['tourismusregion'] = 'tourismusregion'
        # Contact
        attributes['legalName'] = 'legalName'
        attributes['department'] = 'department'
        attributes['honorificPrefix'] = 'honorificPrefix'
        attributes['givenName'] = 'givenName'
        attributes['familyName'] = 'familyName'
        attributes['email'] = 'email'

    # Add to all
    attributes['search_text_pro_channel'] = 'search_text_pro_channel'
    attributes['promo_sort_order_scope'] = 'promo_sort_order_scope'
    attributes['license'] = 'license'
    attributes['potentialAction'] = 'potentialAction'

    if 'license' in attributes:
        attributes['copyrightHolder'] = 'copyrightHolder'
    
    if 'potentialAction' in attributes:
        attributes['target'] = 'target'

    #print("Attributes: ")
    #print(attributes)

    # Remove Properties
    print("Remove Attributes: ")
    ##print(code)
    attributes = removeProperties(code, attributes)

    # add Attributes to Body
    body["attributes"] = attributes

    #print("Attributes with remove Properties: ")
    #print(body["attributes"])
    try:
        # DEBUG - Write to file
        addToFile(code, body)
        # To Akeneo
        response = akeneo.patchFamily(code, body)
        addToLogFile(code, response)
           
    except Exception as e:
        print("Error: ", e)
        print("patch Family: ", code)
        print("Response: ", response)
        addToLogFile(code, response)
    return response

def createFamilyMeetingRoom(family, families, akeneo):
    code = family["label"]

    if family["attribute_requirements.ecommerce"] != None:
        attribute_requirements = {attrRequ: attrRequ for attrRequ in family["attribute_requirements.ecommerce"].split(",")}
    else:
        attribute_requirements = {"sku": "sku", "name": "name", "image": "image"}

    attribute_requirements = getParentAttributesRequirements(family, families, attribute_requirements)

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

    try:
        # DEBUG - Write to file
        addToFile(code, body)
        # To Akeneo
        response = akeneo.patchFamily(code, body)
        addToLogFile(code, response)   
    except Exception as e:
            print("Error: ", e)
            print("patch Family: ", code)
            print("Response: ", response)
            addToLogFile(code, response)
    return response



def createFamilies(target, families):
    for family in families:
        print ("CREATE - Family: "+ family["label"])
        if family["enabled"] == 1 and family["type"] == None or family["type"] == "additinalTypes":
            if family["label"] == "MeetingRoom":
                print("MeetingRoom")
                print("PATCH Family: ", family["label"])
                createFamilyMeetingRoom(family, families, target)
                print("FINISH - patch Family: ", family["label"])
            else:
                print("PATCH Family: ", family["label"])
                response = createFamily(family, families, target)
                print("FINISH - patch Family: ", family["label"])

def getSettings():
    # Define the CSV URL
    csv_url = "https://docs.google.com/spreadsheets/d/1-vZI8rZxwbUVqvxU9tn5dVhZG282LXF7KvDTTvyuOfY/gviz/tq?tqx=out:csv&sheet=setupTypes"
    addition_csv_url = "https://docs.google.com/spreadsheets/d/1-vZI8rZxwbUVqvxU9tn5dVhZG282LXF7KvDTTvyuOfY/gviz/tq?tqx=out:csv&sheet=additionalTypes"
    discover_csv_url = "https://docs.google.com/spreadsheets/d/1-vZI8rZxwbUVqvxU9tn5dVhZG282LXF7KvDTTvyuOfY/gviz/tq?tqx=out:csv&sheet=discoverTypes"

    df = readCsv(csv_url)
    df_addition = readCsv(addition_csv_url)
    print("Add Disocver.swiss Types") 
    df_discover = readCsv(discover_csv_url)

    df_discover = df_discover[df_discover["enabled"] == True]
    print(df_discover)

    df = pd.concat([df, df_addition])
    # concat df and df_discover by column label
    df = pd.concat([df, df_discover], ignore_index=True)

    # merge row with same colum label
    df = df.groupby("label").first().reset_index()

    df = df[df["enabled"] == True]

    print(df)

    # Convert the DataFrame to a JSON object
    json_data = df.to_json(orient="records")

    # Write the JSON data to a file
    with open("../../output/index/akeneo/families.json", "w") as file:
        file.write(json_data)

    return json.loads(json_data)

def readCsv(url):
    # Read the CSV data into a pandas DataFrame
    df = pd.read_csv(url)
    return df

def main():
    # Set Familie Settings
    families = getSettings()

    # Load environment variables
    #environments = getEnvironment()
    #environments = ["ziggy"]
    environments = ["demo"]

    print("START PATCH FAMILIES")
    for environment in environments:
        targetCon = loadEnv(environment)
        target = Akeneo(targetCon["host"], targetCon["clientId"], targetCon["secret"], targetCon["user"], targetCon["passwd"])
        createFamilies(target, families)
    print("FINISH PATCH FAMILIES")

if __name__ == '__main__':
    main()