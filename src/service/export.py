import service.debug as debug

def filter(products, attribute): 
    #attribute = "openingHoursSpecification"
    productsUpdated = []
    for product in products:
        if attribute in product["values"]:
            productsUpdated.append(product)
    return productsUpdated

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
        
        # Stop for Export
        #print("Upload Products")
        #productsUpload = migration.uploadProducts(target, productsTranform)
        #print("FINISH PATCH PRODUCTS for: ", attribute)
        
