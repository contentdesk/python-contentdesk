import service.debug as debug

def filter(products, attribute): 
    #attribute = "openingHoursSpecification"
    productsUpdated = []
    for product in products:
        if attribute in product["values"]:
            productsUpdated.append(product)
    return productsUpdated

def skuList(products, attribute):
    skuList = []
    for product in products:
        if attribute in product["values"]:
            productData = [
                product["identifier"], 
                product["values"][attribute][0]["data"]
            ]
            skuList.append(productData)
        else:
            skuList.append(product["identifier"])
    return skuList

def uuidList(products):
    uuidList = []
    for product in products:
        uuidList.append(product["uuid"])
    return uuidList

def main(environment, target, attributes):
    for attribute in attributes:
        print("START Export PRODUCTS for: ", attribute)
        #migration = importMigrationSettings(attribute)
        print("Get all Products")
        products = target.getProducts()
        debug.addToFileExport(environment, attribute, 'products', products)
        print("Filter Products")
        productsTranform = filter(products, attribute)
        debug.addToFileExport(environment, attribute, 'transform', productsTranform)
        
        productsSku = skuList(productsTranform, attribute)
        debug.addToFileExport(environment, attribute, 'sku', productsSku)
        
        productsUuid = uuidList(productsTranform)
        debug.addToFileExport(environment, attribute, 'uuid', productsUuid)
        
        # Stop for Export
        #print("Upload Products")
        #productsUpload = migration.uploadProducts(target, productsTranform)
        #print("FINISH PATCH PRODUCTS for: ", attribute)
        
