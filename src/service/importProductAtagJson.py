import json
import os
import uuid

import service.debug as debug

language = ['de_CH', 'en_US', 'fr_FR', 'it_IT']

def extract():
    input_folder = '../../input/atag'
    data = []
    for filename in os.listdir(input_folder):
        if filename.endswith('.json'):
            with open(os.path.join(input_folder, filename), mode='r', encoding='utf-8') as file:
                json_data = json.load(file)
                print(" - Read File: ", filename)
                data.extend(json_data)
    return data

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

def transformData(item):
    transformed_item = {}
    transformed_item['identifier'] =  str(uuid.uuid4())
    transformed_item['family'] = "EventVenue"
    transformed_item['values'] = {}
    
    transformed_item['values']['name'] = [{
                "data": item["name"],
                "locale": "de_CH",
                "scope": None
            }]
    transformed_item['values']['description'] = [{
                "data": item["localityDescription"],
                "locale": "de_CH",
                "scope": "mice"
            }]
    
    transformed_item['values']['disambiguatingDescription'] = [{
                "data": item["shortDescription"],
                "locale": "de_CH",
                "scope": "mice"
            }]
    
    transformed_item['values']['location'] = [{
                "data": item["contact"]['title'],
                "locale": None,
                "scope": None
            }]
    
    transformed_item['values']['streetAddress'] = [{
                "data": item["contact"]["address"],
                "locale": None,
                "scope": None
            }]
    
    transformed_item['values']['postalCode'] = [{
                "data": item["contact"]["plzort"].split(" ")[0] if item["contact"]["plzort"] else None,
                "locale": None,
                "scope": None
            }]
    
    transformed_item['values']['addressLocality'] = [{
                "data": item["contact"]["plzort"].split(" ")[1] if item["contact"]["plzort"] else None,
                "locale": None,
                "scope": None
            }]
    
    transformed_item['values']['telephone'] = [{
                    "data": item["contact"]["phone"],
                    "locale": None,
                    "scope": "ecommerce"
                },
                {
                    "data": item["contact"]["phone"],
                    "locale": None,
                    "scope": "mice"
                }
            ]
    transformed_item['values']['email'] = [
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
            ]
    
    if "website" in item["contact"]:
        transformed_item['values']['url'] = [{
                        "locale": None,
                        "scope": "mice",
                        "data": "https://"+item["contact"]["website"]
                    },
                    {
                        "locale": None,
                        "scope": "ecommerce",
                        "data": "https://"+item["contact"]["website"]
                    }
                ]
    return transformed_item

def transform(data):
    # Example transformation: rename a key
    transformed_data = []
    products = data[0]
    for item in data:
        transformed_data.append(transformData(item)) 
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
    
    print(" - Transform Products")

    transformedProducts = transform(extractProducts)
    debug.addToFileFull('import', environment, '','', 'transformedProducts', transformedProducts)
    
    print(" - Load Products")
    
    loadProducts = load(transformedProducts, target)
    debug.addToFileFull('import', environment, '','', 'loadProducts', loadProducts)
    
    print("FINISH Import PRODUCTS")

        
