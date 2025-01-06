import service.debug as debug

def importMigrationSettings(attribute):
    if(attribute == "AttributeOptions"):
        import migration.AttributeOptions as migration
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