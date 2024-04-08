import json

ignoreTypesList = {}

with open('../../output/ignoreTypes.json') as file:
    ignoreTypesFile = json.load(file)

for ignoreType in ignoreTypesFile:
    ignoreTypesList["schema:"+str(ignoreType["label"])] = "schema:"+ignoreType["label"]


ignoreTypes = ignoreTypesList