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

# Load properties.json
def getFamilies():
    with open('../../output/index/akeneo/families.json', 'r') as f:
        families = json.load(f)
    return families

def getTypefromJson(type):
    with open('../../output/types/'+type+'.json', 'r') as f:
        type = json.load(f)
    return type

def getFamilyAttributes(code):
    attributes = []
    print("Get Family Attributes: ", code)
    type = getTypefromJson(code)

    if type["properties"]:
        attributes = type["properties"]

    if type["rdfs:subClassOf"]:
        parentType = getTypefromJson(type["rdfs:subClassOf"]["@id"].split(":")[1])
        if parentType["properties"]:
            attributes = attributes.update(parentType["properties"])
    
    return attributes


def createFamily(family):
    code = family["label"]

    # Set default values

    # Create body
    body = {
        "code": code,
        "attribute_as_label": family["attribute_as_label"],
        "attribute_as_image": family["attribute_as_image"],
        "attribute_requirements": {
            "ecommerce": family["attribute_requirements.ecommerce"].split(","),
            },
        "labels": {
            "en_US": family["label.en_US"],
            "de_CH": family["label.de_CH"],
            "fr_FR": family["label.fr_FR"],
            "it_IT": family["label.it_IT"],
            }
    }

    # Type specific attributes
    body["attributes"] = getFamilyAttributes(code)

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