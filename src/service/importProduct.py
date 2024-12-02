import csv
import os

import service.debug as debug

def extract():
    input_folder = '../../input'
    ##with open("../../output/index/akeneo/families/"+code+".json", "w") as file:
    products = []
    for filename in os.listdir(input_folder):
        if filename.endswith('.csv'):
            with open(os.path.join(input_folder, filename), mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    products.append(row)
    return products

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
        # NAME
        transformed_product['values']['name'] = []
        if 'name-de_CH' in product:
            transformed_product['values']['name'].append({
                'locale': 'de_CH',
                'scope': None,
                'data': product['name-de_CH']
            })
        if 'name-en_US' in product:
            transformed_product['values']['name'].append({
                'locale': 'en_US',
                'scope': None,
                'data': product['name-en_US']
            })
        # DESCRIPTION
        transformed_product['values']['description'] = []
        if 'description-de_CH-ecommerce' in product:
            transformed_product['values']['description'].append({
                'locale': 'de_CH',
                'scope': 'ecommerce',
                'data': product['description-de_CH']
            })
        if 'description-en_US-ecommerce' in product:
            transformed_product['values']['description'].append({
                'locale': 'en_US',
                'scope': 'ecommerce',
                'data': product['description-en_US']
            })
        if 'description-fr_FR-ecommerce' in product:
            transformed_product['values']['description'].append({
                'locale': 'fr_FR',
                'scope': 'ecommerce',
                'data': product['description-fr_FR']
            })
        if 'description-it_IT-ecommerce' in product:
            transformed_product['values']['description'].append({
                'locale': 'it_IT',
                'scope': 'ecommerce',
                'data': product['description-it_IT']
            })
        
        # dynamic Attribut
        for key, value in product.items():
            print (key)
            if '-' in key:
                parts = key.split('-')
                if len(parts) == 2:
                    attribute, locale = parts
                    transformed_product['values'].setdefault(attribute, []).append({
                    'locale': locale,
                    'scope': None,
                    'data': value
                    })
                elif len(parts) == 3:
                    attribute, locale, scope = parts
                    transformed_product['values'].setdefault(attribute, []).append({
                    'locale': locale,
                    'scope': scope,
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
    extractProducts = extract()
    debug.addToFileFull('import', environment, '', 'extractProducts', extractProducts)
    
    transformedProducts = transform(extractProducts)
    
    debug.addToFileFull('import', environment, '', 'transformedProducts', transformedProducts)
    
    loadProducts = load(transformedProducts, target)
    
    debug.addToFileFull('import', environment, '', 'loadProducts', loadProducts)
    
    print("FINISH Import PRODUCTS")

        
