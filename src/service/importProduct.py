import csv
import os

import service.debug as debug

def load():
    def load():
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

def main(environment, target):
    products = load()
    debug.addToFileFull('import', environment, '', 'products', products)
    
    transformed_products = transform(products)
    
    for attribute in attributes:
        print("START Import PRODUCTS for: ", attribute)
        #migration = importMigrationSettings(attribute)
        print("Get all Products")
        products = target.getProducts()
        debug.addToFileFull(environment, attribute, 'products', products)
        print("Filter Products")
        productsTranform = filter(products, attribute)
        debug.addToFileFull(environment, attribute, 'transform', productsTranform)
        
        productsSku = skuList(productsTranform, attribute)
        debug.addToFileFull(environment, attribute, 'sku', productsSku)
        
        productsUuid = uuidList(productsTranform)
        debug.addToFileFull(environment, attribute, 'uuid', productsUuid)
        
        # Stop for Export
        #print("Upload Products")
        #productsUpload = migration.uploadProducts(target, productsTranform)
        print("FINISH Import PRODUCTS for: ", attribute)
        
