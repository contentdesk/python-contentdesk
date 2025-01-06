import service.debug as debug
import logging

############################################################################################################
# 1. Export all Products with Attribute with Options
# 1.1 Backup all Products with Attribute
# 2. Change Attribute Options to new Options
# 3. Upload all Products with Attribute   
############################################################################################################

def getProducts(target, attribute, oldOption):
    #search = 'search={"openingHours_text":[{"operator":"NOT EMPTY","value":"","locale":"de_CH"}]}'
    search = '{"'+attribute+'":[{"operator":"IN,"value":["'+oldOption+'"]}]}&attributes=award'
    products = target.getProductBySearch(search)
    return products

def changeAttributeOptions(product, attribute, oldOption, newOptions):
    updateProduct = {}
    
    updateProduct['identifier'] = product['identifier']
    updateProduct['values'] = {}
    updateProduct['values'][attribute] = product['values'][attribute]
    options = product['values'][attribute]['data']
    
    # replace oldOption with newOptions in array options
    options = [newOptions if x == oldOption else x for x in options]
    
    updateProduct['values'][attribute][0]['data'] = options
    
    return updateProduct

def removeProperties(product):
    updateProduct = {}
    
    updateProduct['identifier'] = product['identifier']
    updateProduct['values'] = {}
    updateProduct['values']['award'] = product['values']['labels']
    
    return updateProduct

def transform(products, attribute, oldOption, newOptions):
    print("Transform Products")
    productsUpdated = []
    for product in products:
        print("Product: ", product['identifier'])
        updateProduct = changeAttributeOptions(product, attribute, oldOption, newOptions)
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