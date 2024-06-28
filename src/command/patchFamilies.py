import json
import requests
import pandas as pd
from akeneo.akeneo import Akeneo
import sys
sys.path.append("..")

from service.loadEnv import loadEnv
import service.debug as debug
import service.cliArguments as cliArguments
import service.patchAkeneoFamily as patchAkeneoFamily

def getSettings():
    # Define the CSV URL
    csv_url = "https://docs.google.com/spreadsheets/d/1-vZI8rZxwbUVqvxU9tn5dVhZG282LXF7KvDTTvyuOfY/gviz/tq?tqx=out:csv&sheet=setupTypes"
    addition_csv_url = "https://docs.google.com/spreadsheets/d/1-vZI8rZxwbUVqvxU9tn5dVhZG282LXF7KvDTTvyuOfY/gviz/tq?tqx=out:csv&sheet=additionalTypes"
    discover_csv_url = "https://docs.google.com/spreadsheets/d/1-vZI8rZxwbUVqvxU9tn5dVhZG282LXF7KvDTTvyuOfY/gviz/tq?tqx=out:csv&sheet=discoverTypes"

    df = pd.read_csv(csv_url)
    df_addition = pd.read_csv(addition_csv_url)
    print("Add Disocver.swiss Types") 
    df_discover = pd.read_csv(discover_csv_url)

    df_discover = df_discover[df_discover["enabled"] == True]
    print(df_discover)

    df = pd.concat([df, df_addition])
    # concat df and df_discover by column label
    df = pd.concat([df, df_discover], ignore_index=True)

    # merge row with same colum label
    #df = df.groupby("label").first().reset_index()
    #df = df.drop_duplicates(subset=['label'])

    df = df[df["enabled"] == True]

    print(df)

    # Convert the DataFrame to a JSON object
    json_data = df.to_json(orient="records")

    # Write the JSON data to a file
    with open("../../output/index/akeneo/families.json", "w") as file:
        file.write(json_data)

    return json.loads(json_data)

def createFamilies(target, families, importFamilies = None):
    #filter families by label = Hotel
    #families = [family for family in families if family["label"] == "Hotel"]

    for family in families:
        if importFamilies != None:
            if family["label"] in importFamilies:
                print("Pass")
                pass
            else:
                #print("Continue")
                continue
        print ("CREATE - Family: "+ family["label"])
        if family["enabled"] == 1 and family["type"] == None or family["type"] == "additinalTypes":
            patchAkeneoFamily.patchAkeneoFamily(family, families, target)

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