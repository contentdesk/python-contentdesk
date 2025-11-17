import json
import os
import uuid

import service.debug as debug

language = ['de_CH', 'en_US', 'fr_FR', 'it_IT']

def extract():
    with open("../../input/atag/inputSeminarTool.json", "r") as file:
        json_data = file.read()
    return json.loads(json_data)

def extractTarget(products, target):
    backuptProducts = []
    for product in products:
        if 'identifier' in product:
            print(" - Check Object: ", product['identifier'])
            getProduct = target.getProductByCode(product['identifier'])
        if 'sku' in product:
            print(" - Check Object: ", product['sku'])
            getProduct = target.getProductByCode(product['sku'])
        if getProduct:
            print("OK")
            backuptProducts.append(getProduct)
        else:
            print("NOT FOUND")
            
    return backuptProducts

def transform(data):
    # Example transformation: rename a key
    transformed_data = []
    for item in data:
        transformed_item = {
            "identifier": str(uuid.uuid4()),
            #"fid": item["fid"],
            "name": {
                "data": item["title"],
                "locale": "de_CH",
                "scope": "ecommerce"
            },
            "description": {
                "data": item["localityDescription"],
                "locale": "de_CH",
                "scope": "mice"
            },
            "shortDescription": {
                "data": item["shortDescription"],
                "locale": "de_CH",
                "scope": "mice"
            },
            "location": {
                "data": item["contact"]['title'],
                "locale": None,
                "scope": None
            },
            "title": {
                "data": item["contact"]["address"],
                "locale": None,
                "scope": None
            },
            "postalCode": {
                "data": item["contact"]["plzort"].split(" ")[0] if item["contact"]["plzort"] else None,
                "locale": None,
                "scope": None
            },
            "addressLocation": {
                "data": item["contact"]["plzort"].split(" ")[1] if item["contact"]["plzort"] else None,
                "locale": None,
                "scope": None
            },
            "telephone":[
                {
                    "data": item["contact"]["phone"],
                    "locale": None,
                    "scope": "ecommerce"
                },
                {
                    "data": item["contact"]["phone"],
                    "locale": None,
                    "scope": "mice"
                }
            ],
            "email":[
                {
                    "data": item["contact"]["email"],
                    "locale": None,
                    "scope": "ecommerce"
                },
                {
                    "data": item["contact"]["email"],
                    "locale": None,
                    "scope": "mice"
                }
            ],
            "url":[
                {
                    "locale": None,
                    "scope": "mice",
                    "data": item["contact"]["website"]
                },
                {
                    "locale": None,
                    "scope": "ecommerce",
                    "data": item["contact"]["website"]
                }
            ],
        }
        transformed_data.append(transformed_item)
    return transformed_data

def load(products,target):
    for product in products:
        print(product)
        target.patchProductByCode(product['identifier'], product)
    return products

def main(environment, target):
    print("START Import PRODUCTS from ATAG JSON - ", environment)
    
    print(" - Extract Products - Backup!")
    
    # Load List of Products
    extractProducts = extract()
    debug.addToFileFull('import', environment, '','', 'extractProducts', extractProducts)
    
    print(" - Backup exist Products")
    
    # Backup Extracted Products
    backupProducts = extractTarget(extractProducts, target)
    debug.addToFileFull('import', environment, '','', 'backupProducts', backupProducts)
    
    print(" - Transform Products")

    transformedProducts = transform(extractProducts)
    debug.addToFileFull('import', environment, '','', 'transformedProducts', transformedProducts)
    
    print(" - Load Products")
    
    loadProducts = load(transformedProducts, target)
    debug.addToFileFull('import', environment, '','', 'loadProducts', loadProducts)
    
    print("FINISH Import PRODUCTS")

        
