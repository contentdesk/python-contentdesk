import service.debug as debug
import logging

####################################################################################################
# https://tourismus.atlassian.net/browse/PIM-472
# 1. Export all Products with Attribute action_button_url
# 2. Copy the value of action_button_url to target
# 3. Upload all Products with Attribute target
####################################################################################################

def getProducts(target):
    #search = 'search={"openingHours_text":[{"operator":"NOT EMPTY","value":"","locale":"de_CH"}]}'
    search = '{"action_button_url":[{"operator":"NOT EMPTY","value":""}]}&attributes=action_button_url'
    products = target.getProductBySearch(search)
    return products

def removeProperties(product):
    updateProduct = {}
    updateProduct['identifier'] = product['identifier']
    updateProduct['values'] = {}
    updateProduct['values']['target'] = product['values']['action_button_url']
    
    return updateProduct

def transform(products):
    print("Transform Products")
    productsUpdated = []
    for product in products:
        if "action_button_url" in product['values']:
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