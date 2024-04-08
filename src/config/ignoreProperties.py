ignoreProperties = [
    "schema:alternateName",
]

import json

ignorePropertiesList = {}

with open('../../output/ignoreProperties.json') as file:
    ignorePropertiesFile = json.load(file)

for ignoreProperties in ignorePropertiesFile:
    ignorePropertiesList["schema:"+str(ignoreProperties["label"])] = "schema:"+ignoreProperties["label"]


ignoreProperties = ignorePropertiesList