import pandas as pd

def readCsv(url):
    # Read the CSV data into a pandas DataFrame
    df = pd.read_csv(url)
    return df

def main():
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

if __name__ == "__main__":
    main()