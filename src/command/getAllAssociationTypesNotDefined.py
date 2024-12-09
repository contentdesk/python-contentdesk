
# Alle Produktfamilien Typen die nicht nach discover.swiss Typen sind von einer Instanz in einem CSV und JSON File speichern

import json
import pandas as pd
import sys
from akeneo.akeneo import Akeneo

sys.path.append("..")
import service.cliArguments as cliArguments
from service.loadEnv import loadEnv
import service.debug as debug

def getAssociationTypesNotDefined():
    # Define the CSV URL
    csv_url = "https://docs.google.com/spreadsheets/d/187orB1Qx9YgeS8cVyI29DuGLhr-oj8yIiCIR5wqyqXk/gviz/tq?tqx=out:csv&sheet=setupAttribute"
    addition_csv_url = "https://docs.google.com/spreadsheets/d/187orB1Qx9YgeS8cVyI29DuGLhr-oj8yIiCIR5wqyqXk/gviz/tq?tqx=out:csv&sheet=additionalAttribute"

    df = pd.read_csv(csv_url)
    df_addition = pd.read_csv(addition_csv_url)
    df = pd.concat([df, df_addition])
    # filter df by enabled = false or enabled = empty
    df = df[df["enabled"] == True]
    df = df[df["association"] == True]

    print(df)

    # Convert the DataFrame to a JSON object
    json_data = df.to_json(orient="records")
    
    # Write the JSON data to a file
    with open("../../output/index/contentdesk/associationTypes.json", "w") as file:
        file.write(json_data)

    return json.loads(json_data)

def main():
    environments = cliArguments.getEnvironment(sys)
    arguments = cliArguments.getArguments(sys)
    
    print("START EXPORT associationType")
    for environment in environments:
        targetCon = loadEnv(environment)
        target = Akeneo(targetCon["host"], targetCon["clientId"], targetCon["secret"], targetCon["user"], targetCon["passwd"])
        
        akeneoAssocationTypes = target.getAssociationTypes()
        getAllAssociationTypesNotDefined = getAssociationTypesNotDefined()
        
        # Compare colum code from akeneoFamilies with colum label from discoverFamilies and save the difference in a JSON file
        # Save the difference in a JSON file
        difference = [type for type in akeneoAssocationTypes if type["code"] not in [df["label"] for df in getAllAssociationTypesNotDefined]]
        
        debug.addToFileExportFull(environment, 'all', '', 'associationType', difference)
        
        onlyCode = []
        for associationType in difference:
            onlyCode.append(associationType["code"])
        
        debug.addToFileExportFull(environment, 'associationType', '', 'associationType', onlyCode)
        
    print("FINISH EXPORT associationType")
    
if __name__ == "__main__":
    main()