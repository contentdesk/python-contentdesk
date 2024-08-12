import json

# DEBUG
def addToFile(code, data):
    with open("../../output/index/akeneo/families/"+code+".json", "w") as file:
        file.write(json.dumps(data))

# DEBUG - Log
def addToLogFile(code, data):
    with open("../../output/logs/families/"+code+".json", "w") as file:
        file.write(json.dumps(data))
        
# DEBUG - Migration
def addToFileMigration(environment, attribute, name, data):
    with open("../../output/migration/"+environment+"/"+attribute+"/"+name+".json", "w") as file:
        file.write(json.dumps(data))