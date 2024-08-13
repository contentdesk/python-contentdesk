import service.debug as debug
import logging

####################################################################################################
# https://tourismus.atlassian.net/browse/PIM-480
# 1. Export all Products with Attribute accommodation_classification_garni
# 2. Copy the value of accommodation_classification_garni to garni
# 3. Upload all Products with Attribute garni
####################################################################################################

def getProducts(target):
    #search = 'search={"openingHours_text":[{"operator":"NOT EMPTY","value":"","locale":"de_CH"}]}'
    search = '{"accommodation_classification_garni":[{"operator":"=","value":true}]}&attributes=accommodation_classification_garni'
    products = target.getProductBySearch(search)
    return products

def removeProperties(product):
    updateProduct = {}
    updateProduct['identifier'] = product['identifier']
    updateProduct['values'] = {}
    updateProduct['values']['garni'] = product['values']['accommodation_classification_garni']
    
    return updateProduct

def transform(products):
    print("Transform Products")
    productsUpdated = []
    for product in products:
        if "accommodation_classification_garni" in product['values']:
            updateProduct = removeProperties(product)
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