import json
import requests
import pandas as pd
from akeneo.akeneo import Akeneo
import sys
sys.path.append("..")

from service.loadEnv import loadEnv
import service.debug as debug
import entity.Family.Family as Family
import entity.Family.MeetingRoom as MeetingRoom
import service.cliArguments as cliArguments

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

def patchFamily(code, body, akeneo):
    clearBody = {
        "code": code,
        "attribute_as_label": body["attribute_as_label"],
        "attribute_as_image": body["attribute_as_image"],
        "attribute_requirements": {
            "ecommerce": [
                "sku",
                "name",
                "image",
            ],
            "mice": [],
            "print": [],
            "intern": []

        },
        "labels": {
            "en_US": body["labels"]["en_US"],
            "de_CH": body["labels"]["de_CH"],
            "fr_FR": body["labels"]["fr_FR"],
            "it_IT": body["labels"]["it_IT"],
        },
        "attributes": [
            "sku",
            "name",
            "image",
        ]
    }
    try:
        # Clear Attributes
        print("Clear Attributes")
        response = akeneo.patchFamily(code, clearBody)
        # DEBUG - Write to file
        debug.addToFile(code, body)
        # To Akeneo
        print("Patch family")
        response = akeneo.patchFamily(code, body)
        debug.addToLogFile(code, response)
           
    except Exception as e:
        print("Error: ", e)
        print("patch Family: ", code)
        print("Response: ", response)
        debug.addToLogFile(code, response)
    return response

def createFamilies(target, families, importFamilies = None):
    #filter families by label = Hotel
    #families = [family for family in families if family["label"] == "Hotel"]

    for family in families:
        if importFamilies != None:
            if family["label"] in importFamilies:
                pass
            else:
                continue   
        print ("CREATE - Family: "+ family["label"])
        if family["enabled"] == 1 and family["type"] == None or family["type"] == "additinalTypes":
            if family["label"] == "MeetingRoom":
                print("MeetingRoom")
                print("PATCH Family: ", family["label"])
                body = MeetingRoom.setBody(family, families, target)
                response = patchFamily(family["label"], body, target)
                print("FINISH - patch Family: ", family["label"])
            else:
                print("PATCH Family: ", family["label"])
                body = Family.setBody(family, families)
                response = patchFamily(family["label"], body, target)
                print("FINISH - patch Family: ", family["label"])

def main():
    environments = cliArguments.getEnvironment(sys)
    importFamilies = cliArguments.getArguments(sys)

    # Set Familie Settings
    families = getSettings()

    print("START PATCH FAMILIES")
    for environment in environments:
        targetCon = loadEnv(environment)
        target = Akeneo(targetCon["host"], targetCon["clientId"], targetCon["secret"], targetCon["user"], targetCon["passwd"])
        createFamilies(target, families, importFamilies)
    print("FINISH PATCH FAMILIES")

if __name__ == '__main__':
    main()