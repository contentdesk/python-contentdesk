import json
import requests
import pandas as pd
from akeneo.akeneo import Akeneo
import sys
sys.path.append("..")

from service.loadEnv import loadEnv
import service.debug as debug
import service.cliArguments as cliArguments
import service.patchAkeneoFamily as patchAkeneoFamily
import service.deleteProduct as delete

LodgingBusiness = "https://docs.google.com/spreadsheets/d/1_gYfX_VIyoJF9g4K6ZMXkcquAoZeJ2g1zPj_vfanpfs/gviz/tq?tqx=out:csv&sheet=LodgingBusiness"
Place = "https://docs.google.com/spreadsheets/d/1_gYfX_VIyoJF9g4K6ZMXkcquAoZeJ2g1zPj_vfanpfs/gviz/tq?tqx=out:csv&sheet=Place"
FoodEstablishment = "https://docs.google.com/spreadsheets/d/1_gYfX_VIyoJF9g4K6ZMXkcquAoZeJ2g1zPj_vfanpfs/gviz/tq?tqx=out:csv&sheet=FoodEstablishment"


def getProductDemos(url, filename):
    # Define the CSV URL
    df = pd.read_csv(url)
    print(df)
    # Convert the DataFrame to a JSON object
    json_data = df.to_json(orient="records")

    # Write the JSON data to a file
    with open("../../output/index/akeneo/products/"+filename+".json", "w") as file:
        file.write(json_data)

    return json.loads(json_data)

def createBodybyValues(product):
    
    body = {}
    print("Create Body")
    for productbody in product:
        print(productbody)
    
    return body

def createProducts(target, products):
    for product in products:
        
        print (product['identifier'])
        body = createBodybyValues(product)
        print ("PATCH - Product:")
        #Akeneo.patchProductByCode(product, products, target)

def main():
    environments = cliArguments.getEnvironment(sys)
    #arguments = cliArguments.getArguments(sys)

    # Set Familie Settings
    #products = getProductDemos(LodgingBusiness, "LodgingBusiness")

    print("START PATCH PRODUCTS")
    for environment in environments:
        targetCon = loadEnv(environment)
        target = Akeneo(targetCon["host"], targetCon["clientId"], targetCon["secret"], targetCon["user"], targetCon["passwd"])
        #createProducts(target, products)
        delete.main(environment, target)
    print("FINISH PATCH PRODUCTS")

if __name__ == '__main__':
    main()