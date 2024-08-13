import service.debug as debug
import logging

####################################################################################################
# https://tourismus.atlassian.net/browse/PIM-481
# 1. Export all Products with Attribute accommodation_classification_superior
# 2. Copy the value of accommodation_classification_superior to superior
# 3. Upload all Products with Attribute garni
####################################################################################################

def getProducts(target):
    #search = 'search={"openingHours_text":[{"operator":"NOT EMPTY","value":"","locale":"de_CH"}]}'
    search = '{"accommodation_classification_superior":[{"operator":"=","value":true}]}&attributes=accommodation_classification_superior'
    products = target.getProductBySearch(search)
    return products

def removeProperties(product):
    updateProduct = {}
    updateProduct['identifier'] = product['identifier']
    updateProduct['values'] = {}
    updateProduct['values']['superior'] = product['values']['accommodation_classification_superior']
    
    return updateProduct

def transform(products):
    print("Transform Products")
    productsUpdated = []
    for product in products:
        if "accommodation_classification_superior" in product['values']:
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