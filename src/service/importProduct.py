import csv
import os

import service.debug as debug

language = ['de_CH', 'en_US', 'fr_FR', 'it_IT']

def extract():
    input_folder = '../../input'
    ##with open("../../output/index/akeneo/families/"+code+".json", "w") as file:
    products = []
    for filename in os.listdir(input_folder):
        if filename.endswith('.csv'):
            with open(os.path.join(input_folder, filename), mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter=';')
                for row in reader:
                    print(" - Read Row: ", row)
                    products.append(row)
    return products

def extractTarget(products, target):
    backuptProducts = []
    for product in products:
        print(" - Check Object: ", product['identifier'])
        getProduct = target.getProductByCode(product['identifier'])
        if getProduct:
            print("OK")
            backuptProducts.append(getProduct)
        else:
            print("NOT FOUND")
            
    return backuptProducts

def transform(products):
    transformed_products = []
    for product in products:
        transformed_product = {}
        if 'sku' in product:
            transformed_product['identifier'] = product['sku']
        if 'family' in product:
            transformed_product['family'] = product['family']
        if 'categories' in product:
            transformed_product['categories'] = product['categories']
        if 'enabled' in product:
            transformed_product['enabled'] = product['enabled']
        
        # VALUES
        transformed_product['values'] = {}
        # dynamic Attribut
        for key, value in product.items():
            print (key)
            if key not in ['sku', 'family', 'categories', 'enabled', 'groups', 'parent', 'created', 'updated']:
                if '-' in key:
                    parts = key.split('-')
                    if len(parts) == 2:
                        if parts[1] in language:
                            attribute, locale = parts
                            transformed_product['values'].setdefault(attribute, []).append({
                                'locale': locale,
                                'scope': None,
                                'data': value
                            })
                        else:
                            attribute, scope = parts
                            transformed_product['values'].setdefault(attribute, []).append({
                                'locale': None,
                                'scope': scope,
                                'data': value
                            })
                    elif len(parts) == 3:
                            attribute, locale, scope = parts
                            transformed_product['values'].setdefault(attribute, []).append({
                            'locale': locale,
                            'scope': scope,
                            'data': value
                        })
                else:
                    if "[" in value:
                        print("Array: ", value)
                        transformed_product['values'].setdefault(key, []).append({
                            'locale': None,
                            'scope': None,
                            'data': value.strip('[]').split(',')
                        })
                    else:
                        transformed_product['values'].setdefault(key, []).append({
                            'locale': None,
                            'scope': None,
                            'data': value
                        })
                
        
        transformed_products.append(transformed_product)
    
    return transformed_products

def load(products,target):
    for product in products:
        print(product)
        target.patchProductByCode(product['identifier'], product)
    return products

def main(environment, target):
    print("START Import PRODUCTS")
    
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

        
