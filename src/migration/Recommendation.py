import service.debug as debug
import logging

####################################################################################################
# https://tourismus.atlassian.net/browse/PIM-491
# 1. Export all Products
# 2. Copy association-type RECOMMEND to Recommendation
# 3. Upload all changed Products
####################################################################################################

def getProducts(target):
    #search = 'search={"openingHours_text":[{"operator":"NOT EMPTY","value":"","locale":"de_CH"}]}'
    search = '{"accommodation_classification_garni":[{"operator":"=","value":true}]}&attributes=accommodation_classification_garni'
    #products = target.getProductBySearch(search)
    products = target.getProducts()
    return products

def removeProperties(product):
    updateProduct = {}
    updateProduct['identifier'] = product['identifier']
    updateProduct['associations'] = {}
    updateProduct['associations']['Recommendation'] = product['associations']['RECOMMEND']
    
    return updateProduct

def transform(products):
    print("Transform Products")
    productsUpdated = []
    for product in products:
        if "RECOMMEND" in product['associations']:
            if "products" in product['associations']['RECOMMEND']:
                # if not empty products
                if product['associations']['RECOMMEND']['products']:
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