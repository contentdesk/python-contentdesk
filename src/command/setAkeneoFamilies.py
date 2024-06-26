import pandas as pd

def readCsv(url):
    # Read the CSV data into a pandas DataFrame
    df = pd.read_csv(url)
    return df

def main():
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

if __name__ == "__main__":
    main()