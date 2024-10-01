import service.debug as debug
import logging

####################################################################################################
# xy
# 1. Export all Products
# 2. Copy association-type x to y
# 3. Upload all changed Products
####################################################################################################

def getProducts(target):
    #search = 'search={"openingHours_text":[{"operator":"NOT EMPTY","value":"","locale":"de_CH"}]}'
    #search = '{"accommodation_classification_garni":[{"operator":"=","value":true}]}&attributes=accommodation_classification_garni'
    #products = target.getProductBySearch(search)
    products = target.getProducts()
    return products

def removeProperties(product, oldAssociation, newAssociation):
    updateProduct = {}
    updateProduct['identifier'] = product['identifier']
    updateProduct['associations'] = {}
    updateProduct['associations'][newAssociation] = product['associations'][oldAssociation]
    
    return updateProduct

def transform(products, oldAssociation, newAssociation):
    print("Transform Products")
    productsUpdated = []
    for product in products:
        if "MICE_ROOM" in product['associations']:
            if "products" in product['associations'][oldAssociation]:
                # if not empty products
                if product['associations'][oldAssociation]['products']:
                    updateProduct = removeProperties(product, oldAssociation, newAssociation)
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