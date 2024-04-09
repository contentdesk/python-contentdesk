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

def createFamilie(family):
    akeneo = Akeneo(
        AKENEO_HOST,
        AKENEO_CLIENT_ID,
        AKENEO_CLIENT_SECRET,
        AKENEO_USERNAME,
        AKENEO_PASSWORD
    )
    code = family["label"]

    # Set default values

    # Create body
    body = {
        "code": code,
        "attributes": family["attributes"],
        "attribute_as_label": family["attribute_as_label"],
        "attribute_as_image": family["attribute_as_image"],
        "attribute_requirements": {
            "ecommerce": family["attribute_requirements.ecommerce"],
            },
        "labels": {
            "en_US": family["label.en_US"],
            "de_CH": family["label.de_CH"],
            "fr_FR": family["label.fr_FR"],
            "it_IT": family["label.it_IT"],
            }
    }

    # Type specific attributes

    try:
        response = akeneo.patchAttribut(code, body)
    except Exception as e:
        print("Error: ", e)
        print("patch Attribute: ", code)
        print("Response: ", response)
    return response

def createAttributesinAkeneo():
    attributes = getAttributes()
    for attribute in attributes:
        print ("Check Property if Attribut: "+ attribute["label"])
        if attribute["pimType"] == "attribute":
            print("patch Attribute: ", attribute["label"])
            createAttribute(attribute)

def main():
    createAttributesinAkeneo()

if __name__ == '__main__':
    main()