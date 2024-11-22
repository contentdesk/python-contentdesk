
# Alle Produktfamilien Typen die nicht nach discover.swiss Typen sind von einer Instanz in einem CSV und JSON File speichern

import json
import pandas as pd
import sys
from akeneo.akeneo import Akeneo

sys.path.append("..")
import service.cliArguments as cliArguments
from service.loadEnv import loadEnv
import service.debug as debug

def getAllFamilyNotByDiscover():
    # Define the CSV URL
    discover_csv_url = "https://docs.google.com/spreadsheets/d/1-vZI8rZxwbUVqvxU9tn5dVhZG282LXF7KvDTTvyuOfY/gviz/tq?tqx=out:csv&sheet=discoverTypes"

    df = pd.read_csv(discover_csv_url)
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
        discoverFamilies = getAllFamilyNotByDiscover()
        
        # Compare akeneoFamilies colum code with discoverFamilies colum label and save the difference in a JSON file
        families = [family for family in akeneoFamilies if family["code"] not in discoverFamilies["label"]]
        
        debug.addToFileExport(environment, 'all', 'family', families)
        
    print("FINISH EXPORT FAMILIES")
    
if __name__ == "__main__":
    main()