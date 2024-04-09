import pandas as pd

# Define the CSV URL
csv_url = "https://docs.google.com/spreadsheets/d/17IYrJlJaqJOBIu96oBu23tFYNLEQE7xFnUFlEUqX4Hk/gviz/tq?tqx=out:csv&sheet=setupDatatype"

# Read the CSV data into a pandas DataFrame
df = pd.read_csv(csv_url)

print(df)

# Convert the DataFrame to a JSON object
json_data = df.to_json(orient="records")

# Write the JSON data to a file
with open("../../output/index/datatype.json", "w") as file:
    file.write(json_data)