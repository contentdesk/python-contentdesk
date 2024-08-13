import service.debug as debug

def importMigrationSettings(attribute):
    if (attribute == "license"):
        import migration.license as migration
    elif (attribute == "openingHours"):
        import migration.openingHours as migration
    elif(attribute == "amenityFeature"):
        import migration.amenityFeature as migration
    return migration

def main(environment, target, attributes):
    for attribute in attributes:
        print("START PATCH PRODUCTS for: ", attribute)
        migration = importMigrationSettings(attribute)
        print("Get Products")
        products = migration.getProducts(target, attribute)
        debug.addToFileMigration(environment, attribute, 'products', products)
        print("Transform Products")
        productsTranform = migration.transform(products)
        debug.addToFileMigration(environment, attribute, 'transform', productsTranform)
        print("Upload Products")
        productsUpload = migration.uploadProducts(target, productsTranform)
        print("FINISH PATCH PRODUCTS for: ", attribute)