import requests
import json
import csv

# URL of the JSON-LD file
url = "https://schema.org/version/latest/schemaorg-current-https.jsonld"

# Fetch the JSON-LD file
response = requests.get(url)
data = response.json()

# Extract types and subtypes from the "Action" category
action_types = set()
checkActionTypes = set()
checkActionTypes.add("schema:Action")
for action in data["@graph"]:
    print(action['@id'])
    if "rdfs:subClassOf" in action:
        print("subClassOf")
        if isinstance(action['rdfs:subClassOf'], list):
            print("List")
            print(action['rdfs:subClassOf'])
            for subclass in action['rdfs:subClassOf']:
                if subclass['@id'] in checkActionTypes:
                    print(subclass['@id'])
                    action_types.add(action['@id'])
                    checkActionTypes.add(action['@id'])
        else:
            print("Not array")
            print(action['rdfs:subClassOf'])
            if action['rdfs:subClassOf']['@id'] in checkActionTypes:
                print(action['@id'])
                action_types.add(action['@id'])
                checkActionTypes.add(action['@id'])

# remove schema: from the action_types
action_types = [t.replace("schema:", "") for t in action_types]

# Print the types and subtypes
print("Types and subtypes of 'Action':")
for t in action_types:
    print(t)

# Save the types and subtypes in a CSV file
csv_file = "../../output/schemaorg/action_types.csv"
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Type"])
    writer.writerows([[t] for t in action_types])

print("CSV file saved successfully!")