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
def getAssociation():
    with open('../../output/index/akeneo/association.json', 'r') as f:
        association = json.load(f)
    return association

def createAssociation(association):
    akeneo = Akeneo(
        AKENEO_HOST,
        AKENEO_CLIENT_ID,
        AKENEO_CLIENT_SECRET,
        AKENEO_USERNAME,
        AKENEO_PASSWORD
    )
    code = association["label"]

    # Set default values

    # Create body
    body = {
        "code": code,
        "labels": {
            "en_US": association["label.en_US"],
            "de_CH": association["label.de_CH"],
            "fr_FR": association["label.fr_FR"],
            "it_IT": association["label.it_IT"],
            }
    }

    # Type specific attributes
    if association["is_quantified"] == None:
        body["is_quantified"] = False
    if association["is_two_way"] == None:
        body["is_two_way"] = False

    try:
        response = akeneo.patchAssociationTypesByCode(code, body)
    except Exception as e:
        print("Error: ", e)
        print("patch Assocation: ", code)
        print("Response: ", response)
    return response

def createAssociationinAkeneo():
    associations = getAssociation()
    for association in associations:
        if association["enabled"] == True and association["association"] == True:
            print("patch Association: ", association["label"])
            createAssociation(association)

def main():
    createAssociationinAkeneo()

if __name__ == '__main__':
    main()