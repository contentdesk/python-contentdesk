import service.debug as debug

def importMigrationSettings():
    import migration.Family as migration
    return migration

def main(environment, target, arguments):
    arg0 = arguments[0]
    arg1 = arguments[1]
    
    print("START PATCH PRODUCTS for Family: "+ arg0 + " to Family: "+ arg1) 
    migration = importMigrationSettings()
    print("Get Products with Family: ", arg0)
    products = migration.getProducts(target, arg0)
    debug.addToFileMigration(environment, arg0, 'products', products)
    print("Transform Products")
    productsTranform = migration.transform(products, arg1)
    debug.addToFileMigration(environment, arg0, 'transform', productsTranform)
    print("Upload Products")
    productsUpload = migration.uploadProducts(target, productsTranform)
    print("FINISH PATCH PRODUCTS for Family: "+ arg0 + " to Family: "+ arg1) 