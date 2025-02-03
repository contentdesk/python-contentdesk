import csv
import service.debug as debug
import service.exportCSV as exportCSV

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

def exportProductsWithFamily(environment, target, family):
    print("Get all Products")
    print(family)
    search = '{"enabled":[{"operator":"=","value":true,"scope":null}],"completeness":[{"operator":"=","value":100,"scope":"ecommerce"}],"family":[{"operator":"IN","value":["'+str(family)+'"]}]}&attributes=name'
    products = target.getProducts(search, None, None, 100)
    #products = target.getProducts()
            
    debug.addToFileExportFull(environment, 'products', family, 'products', products)
            
    productsSku = skuList(products)
    debug.addToFileExportFull(environment, 'products', family, 'sku', productsSku)
            
    productsUuid = uuidList(products)
    debug.addToFileExportFull(environment, 'products', family, 'uuid', productsUuid)
            
    print("Exporting to CSV")
    #exportCSV.exportCSV('export',environment, 'products', family, f"{family}_products.csv", products)
    #exportCSV.exportCSV('export',environment, 'products', family, f"{family}_sku.csv", [{'identifier': identifier} for identifier in productsSku])
    #exportCSV.exportCSV('export',environment, 'products', family, f"{family}_uuid.csv", [{'uuid': uuid} for uuid in productsUuid])

def exportProductsDiscvoer(environment, target):
    search = '{"enabled":[{"operator":"=","value":true,"scope":null}],"completeness":[{"operator":"=","value":100,"scope":"ecommerce"}]}&attributes=name'
    products = target.getProductBySearch(search)
    #products = target.getProducts()
            
    debug.addToFileExportFull(environment, 'products', 'discover', 'products', products)
            
    productsSku = skuList(products)
    debug.addToFileExportFull(environment, 'products', 'discover', 'sku', productsSku)
            
    productsUuid = uuidList(products)
    debug.addToFileExportFull(environment, 'products', 'discover', 'uuid', productsUuid)
            
    print("Exporting to CSV")
    #exportCSV.exportCSV('export',environment, 'products', 'discover', f"discover_products.csv", products)
    #exportCSV.exportCSV('export',environment, 'products', 'discover', f"discover_sku.csv", [{'identifier': identifier} for identifier in productsSku])
    #exportCSV.exportCSV('export',environment, 'products', 'discover', f"discover_uuid.csv", [{'uuid': uuid} for uuid in productsUuid])

def main(environment, target, arguments):
    if arguments == None:
        print("START Export PRODUCTS for: ")
        exportProductsDiscvoer(environment, target)
        print("FINISH Export PRODUCTS for: ")
    else:
        for family in arguments:
            print("START Export PRODUCTS for: ", family)
            exportProductsWithFamily(environment, target, family)
            print("FINISH Export PRODUCTS for: ", family)
            
        
