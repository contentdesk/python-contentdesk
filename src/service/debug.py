import json
from datetime import datetime
import logging
import os

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
    
    # Check if folder exists
    if not os.path.exists("../../output/migration/"+environment+"/"+attribute+"/"+str_current_datetime+"/"):
        os.makedirs("../../output/migration/"+environment+"/"+attribute+"/"+str_current_datetime+"/")
    
    with open("../../output/migration/"+environment+"/"+attribute+"/"+str_current_datetime+"/"+name+".json", "w") as file:
        file.write(json.dumps(data))

# DEBUG - Full
def addToFileFull(mainpath, environment, attribute, name, data):
    # get current date and time
    current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    print("Current date & time : ", current_datetime)
    
    # convert datetime obj to string
    str_current_datetime = str(current_datetime)
    
    if attribute != "":
        # Check if folder exists
        if not os.path.exists("../../output/"+mainpath+"/"+environment+"/attribute/"+attribute):
            os.makedirs("../../output/"+mainpath+"/"+environment+"/attribute/"+attribute)
        
        with open("../../output/"+mainpath+"/"+environment+"/attribute/"+attribute+"/"+name+"-"+str_current_datetime+".json", "w") as file:
            file.write(json.dumps(data))
    else:
        # Check if folder exists
        if not os.path.exists("../../output/"+mainpath+"/"+environment+"/"+str_current_datetime+"/"):
            os.makedirs("../../output/"+mainpath+"/"+environment+"/"+str_current_datetime+"/")
        
        with open("../../output/"+mainpath+"/"+environment+"/"+str_current_datetime+"/"+name+".json", "w") as file:
            file.write(json.dumps(data))

# DEBUG - Export Full neutral
def addToFileExportFull(environment, folder, attribute, name, data):
    # get current date and time
    current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    print("Current date & time : ", current_datetime)
    
    # convert datetime obj to strings
    str_current_datetime = str(current_datetime)
    
    # Check if folder exists
    if not os.path.exists("../../output/export/"+environment+"/"+folder+"/"+attribute+"/"+str_current_datetime+"/"):
        os.makedirs("../../output/export/"+environment+"/"+folder+"/"+attribute+"/"+str_current_datetime+"/")
    
    with open("../../output/export/"+environment+"/"+folder+"/"+attribute+"/"+str_current_datetime+"/"+name+"-.json", "w") as file:
        file.write(json.dumps(data))
        
# DEBUG - Export Family
def addToFileExport(environment, family, name, data):
    # get current date and time
    current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    print("Current date & time : ", current_datetime)
    
    # convert datetime obj to string
    str_current_datetime = str(current_datetime)
    
    # Check if folder family
    if not os.path.exists("../../output/export/"+environment+"/family/"+family):
        os.makedirs("../../output/export/"+environment+"/family/"+family)
    
    with open("../../output/export/"+environment+"/family/"+family+"/"+name+"-"+str_current_datetime+".json", "w") as file:
        file.write(json.dumps(data))
        
# add now Date and Time to Filename
def loggingToFile(type, data):
    # get current date and time
    current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    print("Current date & time : ", current_datetime)
    
    # convert datetime obj to string
    str_current_datetime = str(current_datetime)
    
    logging.basicConfig(
        filename="../../output/logs/migrations/"+str_current_datetime+".log",
        encoding="utf-8",
        filemode="a",
        format="{asctime} - {levelname} - {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M",
    )
    if type == "info":
        logging.info(data)
    elif type == "warning":
        logging.warning(data)
    elif type == "error":
        logging.error(data)
    elif type == "critical":
        logging.critical(data)
    else:
        logging.debug(data)
