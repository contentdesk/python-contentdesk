def importMigrationSettings(target, attribute):

    if (attribute == "license"):
        import migration.license as migration
    elif (attribute == "openingHours"):
        import migration.openingHours as migration
    elif(attribute == "amenityFeature"):
        import migration.amenityFeature as migration
    return migration

def main(target, attributes):
    for attribute in attributes:
        print("START PATCH PRODUCTS for: ", attribute)
        migration = importMigrationSettings(attribute)
        products = migration.getProducts(target, attribute)
        productsTranform = migration.transform(products)
        productsUpload = migration.uploadProducts(productsTranform)
        print("FINISH PATCH PRODUCTS for: ", attribute)