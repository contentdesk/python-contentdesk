import service.debug as debug
import logging

####################################################################################################
# https://tourismus.atlassian.net/browse/PIM-521
# 1. Export all Products with Attribute openingHoursSpecification
# 2. Manuell Fix openingHoursSpecification
# 3. Upload all Products with Attribute openingHoursSpecification 
####################################################################################################

def getProducts(target):
    #search = 'search={"openingHours_text":[{"operator":"NOT EMPTY","value":"","locale":"de_CH"}]}'
    #search = '{"starRating ":[{"operator":"NOT EMPTY","value":""}]}&attributes=starRating'
    products = target.getProductBySearch()
    return products


def transform(products):
    attribute = "openingHoursSpecification"
    productsUpdated = []
    for product in products:
        if attribute in product and product["values"][attribute]:
            productsUpdated.append(product)
    return productsUpdated

def uploadProducts(target, products):
    # save on file for manual fix
    # stop here
    debug.addToFileMigration("test", "openingHoursSpecification", 'upload', products)