import service.debug as debug

def importMigrationSettings():
    import migration.Association as migration
    return migration

def main(environment, target, arguments):
    arg0 = arguments[0]
    arg1 = arguments[1]
    
    print("START PATCH PRODUCTS for Association: "+ arg0 + " to Association: "+ arg1) 
    migration = importMigrationSettings()
    print("Get Products with Association: ", arg0)
    products = migration.getProducts(target)
    debug.addToFileMigration(environment, arg0, 'products', products)
    print("Transform Products")
    productsTranform = migration.transform(products, arg0, arg1)
    debug.addToFileMigration(environment, arg0, 'transform', productsTranform)
    print("Upload Products")
    productsUpload = migration.uploadProducts(target, productsTranform)
    print("FINISH PATCH PRODUCTS for Association: "+ arg0 + " to Association: "+ arg1) 