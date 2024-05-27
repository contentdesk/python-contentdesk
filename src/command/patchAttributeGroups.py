import json
from akeneo.akeneo import Akeneo

import sys
sys.path.append("..")

from service.loadEnv import loadEnv, getEnvironment

# Load properties.json
def getAttributeGroups():
    with open('../../output/index/akeneo/attributeGroups.json', 'r') as f:
        attributeGroups = json.load(f)
    return attributeGroups

def createAttributeGroup(attributeGroup, akeneo):
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

def createAttributeGroupsinAkeneo(akeneo):
    attributeGoups = getAttributeGroups()
    for attributeGroup in attributeGoups:
        print("patch AttributGroup "+ attributeGroup["code"])
        createAttributeGroup(attributeGroup, akeneo)

def main():
    # Load environment variables
    #environments = getEnvironment()
    environments = ["ziggy"]
    #environments = ["demo"]

    print("START PATCH ATTRIBUTE GROUPS")
    for environment in environments:
        targetCon = loadEnv(environment)
        print (targetCon["host"])
        target = Akeneo(targetCon["host"], targetCon["clientId"], targetCon["secret"], targetCon["user"], targetCon["passwd"])
        createAttributeGroupsinAkeneo(target)
    print("FINISH PATCH ATTRIBUTE GROUPS")


if __name__ == '__main__':
    main()