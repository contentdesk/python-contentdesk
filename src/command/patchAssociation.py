import json
from akeneo.akeneo import Akeneo
import sys
sys.path.append("..")

from service.loadEnv import loadEnv, getEnvironment

# Load properties.json
def getAssociation():
    with open('../../output/index/akeneo/association.json', 'r') as f:
        association = json.load(f)
    return association

def createAssociation(association, akeneo):
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

def createAssociationinAkeneo(akeneo):
    associations = getAssociation()
    for association in associations:
        if association["enabled"] == True and association["association"] == True:
            print("patch Association: ", association["label"])
            createAssociation(association, akeneo)

def main():
    #environments = getEnvironment()
    #environments = ["ziggy"]
    environments = ["demo"]

    print("START PATCH Associatinons")
    for environment in environments:
        targetCon = loadEnv(environment)
        print (targetCon["host"])
        target = Akeneo(targetCon["host"], targetCon["clientId"], targetCon["secret"], targetCon["user"], targetCon["passwd"])
        createAssociationinAkeneo(target)
    print("FINISH PATCH Associatinons")

    

if __name__ == '__main__':
    main()