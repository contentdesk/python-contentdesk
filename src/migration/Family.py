import service.debug as debug
import logging

####################################################################################################
# https://tourismus.atlassian.net/browse/PIM-511
# 1. Export all Products with Family xy
# 2. Migration Family xy to Family xy
# 3. Upload all changed Products
####################################################################################################

def getProducts(target, family):
    #search = 'search={"openingHours_text":[{"operator":"NOT EMPTY","value":"","locale":"de_CH"}]}'
    search = '{"family":[{"operator":"IN","value":["'+family+'"]}]}'
    #products = target.getProductBySearch(search)
    products = target.getProducts(search)
    return products

def removeProperties(product, newFamily):
    updateProduct = {}
    updateProduct['identifier'] = product['identifier']
    updateProduct['family'] = newFamily
    return updateProduct

def transform(products, newFamily):
    print("Transform Products")
    productsUpdated = []
    for product in products:
        if "family" in product:
            updateProduct = removeProperties(product, newFamily)
            productsUpdated.append(updateProduct)
    return productsUpdated

def uploadProducts(target, products):
    for product in products:
        print("Upload Product: ", product['identifier'])
        print("Product: ", product)
        try:
            print("Start Upload")
            response = target.patchProductByCode(product['identifier'], product)
            print("Response: ", response)
        except Exception as e:
            print("Error: ", e)
            # Add To Error Log File
            debug.loggingToFile("error", e)   
             
    print("Upload Products")