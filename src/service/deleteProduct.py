import csv
import service.debug as debug

def filter(products, attribute): 
    #attribute = "openingHoursSpecification"
    productsUpdated = []
    for product in products:
        if attribute in product["values"]:
            productsUpdated.append(product)
    return productsUpdated

def skuList(products):
    skuList = []
    for product in products:
        skuList.append(product["identifier"])
    return skuList

def uuidList(products):
    uuidList = []
    for product in products:
        uuidList.append(product["uuid"])
    return uuidList

def exportProducts(environment, target):
    #search = '{"enabled":[{"operator":"=","value":true,"scope":null}],"completeness":[{"operator":"=","value":100,"scope":"ecommerce"}]}&attributes=name'
    extractProducts = target.getAllProducts()
    #products = target.getProducts()
            
    debug.addToFileFull('delete', environment, '','', 'extractProducts', extractProducts)
    

def main(environment, target):
    print("START Export PRODUCTS for: ")
    exportProducts(environment, target)
    print("FINISH Export PRODUCTS for: ")
            