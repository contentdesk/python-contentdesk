import service.debug as debug
import migration.AttributeOptions as migration

def main(environment, target, aguments):
    print("START PATCH PRODUCTS")
    print("Arguments: ", aguments)
    attribute = aguments[0]
    oldOption = aguments[1]
    newOptions = aguments[2:]
    print("Get Products")
    products = migration.getProducts(target, attribute, oldOption)
    debug.addToFileMigration(environment, attribute, 'products', products)
    print("Transform Products")
    productsTranform = migration.transform(products, attribute, oldOption, newOptions)
    debug.addToFileMigration(environment, attribute, 'transform', productsTranform)
    print("Upload Products")
    productsUpload = migration.uploadProducts(target, productsTranform)
    print("FINISH PATCH PRODUCTS for: ", attribute)