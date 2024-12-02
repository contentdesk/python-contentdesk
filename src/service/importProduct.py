import csv
import os

import service.debug as debug

def extract():
    input_folder = 'input'
    products = []
    for filename in os.listdir(input_folder):
        if filename.endswith('.csv'):
            with open(os.path.join(input_folder, filename), mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    products.append(row)
    return products

def transform(products):
    return products

def load(products,target):
    for product in products:
        print(product)
        target.patchProductByCode(product['sku'], product)

def main(environment, target):
    print("START Import PRODUCTS")
    products = extract()
    debug.addToFileFull('import', environment, '', 'products', products)
    
    transformed_products = transform(products)
    
    debug.addToFileFull('import', environment, '', 'transformed_products', transformed_products)
    
    load(transformed_products, target)
    
    print("FINISH Import PRODUCTS")

        
