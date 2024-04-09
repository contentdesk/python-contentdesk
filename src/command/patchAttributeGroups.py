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
def getAttributeGroups():
    with open('../../output/index/akeneo/attributeGroups.json', 'r') as f:
        attributeGroups = json.load(f)
    return attributeGroups

def createAttributeGroup(attributeGroup):
    akeneo = Akeneo(
        AKENEO_HOST,
        AKENEO_CLIENT_ID,
        AKENEO_CLIENT_SECRET,
        AKENEO_USERNAME,
        AKENEO_PASSWORD
    )
    code = attributeGroup["code"]
    body = {
        "code": code,
        "sort_order": attributeGroup["sort_order"],
        "labels": {
            "en_US": attributeGroup["labels.en_US"],
            "de_CH": attributeGroup["labels.de_CH"],
            "fr_FR": attributeGroup["labels.fr_FR"],
            "it_IT": attributeGroup["labels.it_IT"],
            }
    }
    return akeneo.patchAttributeGroupsbyCode(code, body)

def createAttributeGroupsinAkeneo():
    attributeGoups = getAttributeGroups()
    for attributeGroup in attributeGoups:
        print("patch AttributGroup "+ attributeGroup["code"])
        createAttributeGroup(attributeGroup)

def main():
    createAttributeGroupsinAkeneo()


if __name__ == '__main__':
    main()