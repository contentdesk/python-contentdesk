import json

ignorePropertiesList = {}
indexPropertiesAllneededTypesList = {}

def setIgnoreProperties():
    with open('../../output/ignoreProperties.json') as file:
        ignorePropertiesFile = json.load(file)

    for ignoreProperties in ignorePropertiesFile:
        ignorePropertiesList["schema:"+str(ignoreProperties["label"])] = "schema:"+ignoreProperties["label"]

    return ignorePropertiesList

def setIndexPropertiesAllneededTypes():
    with open('../../output/index/allProperties.json') as file:
        indexPropertiesAllneededTypesFile = json.load(file)

    for indexPropertiesAllneededTypes in indexPropertiesAllneededTypesFile:
        indexPropertiesAllneededTypesList["schema:"+str(indexPropertiesAllneededTypes["label"])] = "schema:"+indexPropertiesAllneededTypes["label"]

    return indexPropertiesAllneededTypesList

def main():
    global ignorePropertiesList
    ignorePropertiesList = setIgnoreProperties()
    global indexPropertiesAllneededTypesList
    indexPropertiesAllneededTypesList = setIndexPropertiesAllneededTypes()

if __name__ == '__main__':
    main()