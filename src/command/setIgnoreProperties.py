import pandas as pd
import json

def setJsonData(properties):
    indexIgnoreProperties = {}
    print("Properties: ", properties)
    for prop in properties:
        print ("Property: ", prop)
        indexIgnoreProperties[prop["label"]] = prop["label"]

    return indexIgnoreProperties

def main():
    # Define the CSV URL
    csv_url = "https://docs.google.com/spreadsheets/d/187orB1Qx9YgeS8cVyI29DuGLhr-oj8yIiCIR5wqyqXk/gviz/tq?tqx=out:csv&sheet=setupAttribute"

    # Read the CSV data into a pandas DataFrame
    df = pd.read_csv(csv_url)

    print(df)
    # filter df by enabled = false or enabled = empty
    df = df[(df["enabled"] == False) | (df["attribute"] != True)]

    # Convert the DataFrame to a JSON object
    json_data = df.to_json(orient="records")

    print("JSON Data: ", json_data)
    data = setJsonData(json.loads(json_data))

    # Write the JSON data to a file
    with open("../../output/ignoreProperties.json", "w") as file:
        file.write(json.dumps(data))
        
    # Write the JSON data to a file
    with open("../../output/index/schema/ignoreProperties.json", "w") as file:
        file.write(json.dumps(data))

if __name__ == "__main__":
    main()
