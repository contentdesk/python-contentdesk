import json
from datetime import datetime

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
    # get current date and time
    current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    print("Current date & time : ", current_datetime)
    
    # convert datetime obj to string
    str_current_datetime = str(current_datetime)
    
    with open("../../output/migration/"+environment+"/"+attribute+"/"+name+"-"+str_current_datetime+".json", "w") as file:
        file.write(json.dumps(data))
        
# add now Date and Time to Filename

