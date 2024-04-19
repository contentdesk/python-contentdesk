# PROMPT:
# Create a Array with all Types from schema.org with Properties by Type from url https://schema.org/version/latest/schemaorg-current-https.jsonld and save in a JSON file

import json
import urllib.request

# Fetch the JSON-LD file from the URL
url = "https://schema.org/version/latest/schemaorg-current-https.jsonld"
response = urllib.request.urlopen(url)
data = json.loads(response.read())

# Extract the types and properties from the JSON-LD data
types = []
properties_by_type = {}

for item in data["@graph"]:
    if item["@type"] == "rdf:Property":
        continue

    if item["@type"] == "rdfs:Class":
        types.append(item["@id"])
        properties_by_type[item["@id"]] = []

    if "schema:domainIncludes" in item:
        domain_includes = item["schema:domainIncludes"]
        if isinstance(domain_includes, list):
            for domain in domain_includes:
                properties_by_type[domain["@id"]].append(item["@id"])
        else:
            properties_by_type[domain_includes["@id"]].append(item["@id"])

# Save the types and properties in a JSON file
with open("../../output/types_properties.json", "w") as file:
    json.dump(properties_by_type, file)

# Print the types and their properties
for type_name, properties in properties_by_type.items():
    print(type_name)
    print(properties)