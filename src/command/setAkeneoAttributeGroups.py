import pandas as pd

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