import pandas as pd

# Define the CSV URL
csv_url = "https://docs.google.com/spreadsheets/d/187orB1Qx9YgeS8cVyI29DuGLhr-oj8yIiCIR5wqyqXk/gviz/tq?tqx=out:csv&sheet=setupAttributes"

# Read the CSV data into a pandas DataFrame
df = pd.read_csv(csv_url)

print(df)
# filter df by enabled = false or enabled = empty
df = df[df["enabled"] == False]

# Convert the DataFrame to a JSON object
json_data = df.to_json(orient="records")

# Write the JSON data to a file
with open("../../output/ignoreProperties.json", "w") as file:
    file.write(json_data)