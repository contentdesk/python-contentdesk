import csv
import os
from datetime import datetime

def exportCSV(mainpath, environment, folder, attribute, filename, data):
    current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    str_current_datetime = str(current_datetime)
    
    if attribute != "":
        # Check if folder exists
        if not os.path.exists("../../output/"+mainpath+"/"+environment+"/"+folder+"/"+attribute):
            os.makedirs("../../output/"+mainpath+"/"+environment+"/"+folder+"/"+attribute)
            
        createCSV("../../output/"+mainpath+"/"+environment+"/"+folder+"/"+attribute+"/"+str_current_datetime+"/"+filename+".csv", data)
    else:
        # Check if folder exists
        if not os.path.exists("../../output/"+mainpath+"/"+environment+"/"+str_current_datetime+"/"):
            os.makedirs("../../output/"+mainpath+"/"+environment+"/"+str_current_datetime+"/")
        
        createCSV("../../output/"+mainpath+"/"+environment+"/"+str_current_datetime+"/"+filename+".csv", data)
        
def createCSV(filename, data):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data[0].keys())  # Write the header
        for row in data:
            writer.writerow(row.values())