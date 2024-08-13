import service.debug as debug

def importMigrationSettings(attribute):
    if (attribute == "license"):
        import migration.license as migration
    elif (attribute == "openingHours"):
        import migration.openingHours as migration
    elif(attribute == "amenityFeature"):
        import migration.amenityFeature as migration
    elif(attribute == "garni"):
        import migration.garni as migration
    elif(attribute == "superior"):
        import migration.superior as migration
    elif(attribute == "starRating"):
        import migration.starRating as migration
    elif(attribute == "target"):
        import migration.target as migration
    elif(attribute == "weatherDependency"):
        import migration.weatherDependency as migration
    elif(attribute == "potentialAction"):
        import migration.potentialAction as migration
    elif(attribute == "servesCuisine"):
        import migration.servesCuisine as migration
    return migration

def main(environment, target, attributes):
    for attribute in attributes:
        print("START PATCH PRODUCTS for: ", attribute)
        migration = importMigrationSettings(attribute)
        print("Get Products")
        products = migration.getProducts(target)
        debug.addToFileMigration(environment, attribute, 'products', products)
        print("Transform Products")
        productsTranform = migration.transform(products)
        debug.addToFileMigration(environment, attribute, 'transform', productsTranform)
        print("Upload Products")
        productsUpload = migration.uploadProducts(target, productsTranform)
        print("FINISH PATCH PRODUCTS for: ", attribute)