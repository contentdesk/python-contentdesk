
# Alle Produktfamilien Typen die nicht nach discover.swiss Typen sind von einer Instanz in einem CSV und JSON File speichern

import json
import pandas as pd
import sys
from akeneo.akeneo import Akeneo

sys.path.append("..")
import service.cliArguments as cliArguments
from service.loadEnv import loadEnv
import service.debug as debug

def getAllFamilyNotDefined():
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
    df = pd.concat([df_discover, df])

    # merge row with same colum label
    #df = df.groupby("label").first().reset_index()
    #df = df.drop_duplicates(subset=['label'])

    df = df[df["enabled"] == True]

    print(df)

    # Convert the DataFrame to a JSON object
    json_data = df.to_json(orient="records")

    # Write the JSON data to a file
    with open("../../output/index/discover/types.json", "w") as file:
        file.write(json_data)

    return json.loads(json_data)

def main():
    environments = cliArguments.getEnvironment(sys)
    arguments = cliArguments.getArguments(sys)
    
    print("START EXPORT FAMIL")
    for environment in environments:
        targetCon = loadEnv(environment)
        target = Akeneo(targetCon["host"], targetCon["clientId"], targetCon["secret"], targetCon["user"], targetCon["passwd"])
        akeneoFamilies = target.getFamilies()
        discoverFamilies = getAllFamilyNotDefined()
        
        # Compare colum code from akeneoFamilies with colum label from discoverFamilies and save the difference in a JSON file
        # Save the difference in a JSON file
        differenceFamilies = [family for family in akeneoFamilies if family["code"] not in [df["label"] for df in discoverFamilies]]
        
        debug.addToFileExport(environment, 'all', 'family', differenceFamilies)
        
        onlyCode = []
        for family in differenceFamilies:
            onlyCode.append(family["code"])
        
        debug.addToFileExport(environment, 'family', family["code"], onlyCode)
        
    print("FINISH EXPORT FAMILIES")
    
if __name__ == "__main__":
    main()