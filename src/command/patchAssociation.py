import json
import pandas as pd
from akeneo.akeneo import Akeneo
import sys
sys.path.append("..")

from service.loadEnv import loadEnv, getEnvironment
import service.cliArguments as cliArguments

def readCsv(url):
    # Read the CSV data into a pandas DataFrame
    df = pd.read_csv(url)
    return df

def getSettings():
    # Define the CSV URL
    csv_url = "https://docs.google.com/spreadsheets/d/187orB1Qx9YgeS8cVyI29DuGLhr-oj8yIiCIR5wqyqXk/gviz/tq?tqx=out:csv&sheet=setupAttribute"
    addition_csv_url = "https://docs.google.com/spreadsheets/d/187orB1Qx9YgeS8cVyI29DuGLhr-oj8yIiCIR5wqyqXk/gviz/tq?tqx=out:csv&sheet=additionalAttribute"

    df = readCsv(csv_url)
    df_addition = readCsv(addition_csv_url)
    df = pd.concat([df, df_addition])
    # filter df by enabled = false or enabled = empty
    df = df[df["enabled"] == True]
    df = df[df["association"] == True]

    print(df)

    # Convert the DataFrame to a JSON object
    json_data = df.to_json(orient="records")

    # Write the JSON data to a file
    with open("../../output/index/akeneo/association.json", "w") as file:
        file.write(json_data)

    return json.loads(json_data)

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

def createAssociationinAkeneo(associations, akeneo, arguments = None):
    #associations = getAssociation()
    for association in associations:
        if arguments != None:
            if association["label"] in arguments:
                pass
            else:
                continue
        if association["enabled"] == True and association["association"] == True:
            print("patch Association: ", association["label"])
            createAssociation(association, akeneo)

def main():
    # Set Familie Settings
    associations = getSettings()

    environments = cliArguments.getEnvironment(sys)
    arguments = cliArguments.getArguments(sys)

    print("START PATCH Associatinons")
    for environment in environments:
        targetCon = loadEnv(environment)
        print (targetCon["host"])
        target = Akeneo(targetCon["host"], targetCon["clientId"], targetCon["secret"], targetCon["user"], targetCon["passwd"])
        createAssociationinAkeneo(associations, target, arguments)
    print("FINISH PATCH Associatinons")

    

if __name__ == '__main__':
    main()