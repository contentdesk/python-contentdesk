import json
import pandas as pd
from akeneo.akeneo import Akeneo

import sys
sys.path.append("..")

from service.loadEnv import loadEnv, getEnvironment

def getAttributeGroups():
    # Define the CSV URL
    csv_url = "https://docs.google.com/spreadsheets/d/1HbcevTJlnt7RuoO6qedT6FY_7np-08oLpOAS54kS18E/gviz/tq?tqx=out:csv&sheet=setupAttributeGroup"
    # Read the CSV data into a pandas DataFrame
    df = pd.read_csv(csv_url)
    print(df)
    # filter df by enabled = false or enabled = empty
    df = df[df["enabled"] == True]
    # Convert the DataFrame to a JSON object
    json_data = df.to_json(orient="records")
    # Write the JSON data to a file
    with open("../../output/index/akeneo/attributeGroups.json", "w") as file:
        file.write(json_data)

    return json.loads(json_data)

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

def createAttributeGroupsinAkeneo(attributeGroups, akeneo):
    #attributeGoups = getAttributeGroups()
    for attributeGroup in attributeGroups:
        print("patch AttributGroup "+ attributeGroup["code"])
        createAttributeGroup(attributeGroup, akeneo)

def main():
    attributeGroups = getAttributeGroups()

    # Load environment variables
    #environments = getEnvironment()
    environments = ["viat"]

    print("START PATCH ATTRIBUTE GROUPS")
    for environment in environments:
        targetCon = loadEnv(environment)
        print (targetCon["host"])
        target = Akeneo(targetCon["host"], targetCon["clientId"], targetCon["secret"], targetCon["user"], targetCon["passwd"])
        createAttributeGroupsinAkeneo(attributeGroups,target)
    print("FINISH PATCH ATTRIBUTE GROUPS")

if __name__ == '__main__':
    main()