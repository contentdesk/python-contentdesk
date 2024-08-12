def importMigrationSettings(target, attribute):

    if (attribute == "license"):
        import migration.license as migration
    elif (attribute == "openingHours"):
        import migration.openingHours as migration
    elif(attribute == "amenityFeature"):
        import migration.amenityFeature as migration
    return migration

def migrationProducts(target, attribute):
    print("START PATCH PRODUCTS")
    migration = importMigrationSettings(attribute)
    products = migration.getProducts(target, attribute)
    productsTranform = migration.transform(products)
    productsUpload = migration.uploadProducts(productsTranform)
    print("FINISH PATCH PRODUCTS")