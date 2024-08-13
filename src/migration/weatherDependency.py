import service.debug as debug
import logging

############################################################################################################
# https://tourismus.atlassian.net/browse/PIM-478
# 1. Export all Products with Attribute indoor_outdoor
# 2. Mapping indoor_outdoor options
# 3. Upload all Products with Attribute weatherDependency
############################################################################################################

def getProducts(target):
    #search = 'search={"openingHours_text":[{"operator":"NOT EMPTY","value":"","locale":"de_CH"}]}'
    search = '{"indoor_outdoor ":[{"operator":"NOT EMPTY","value":""}]}&attributes=indoor_outdoor'
    products = target.getProductBySearch(search)
    return products

def removeProperties(product):
    updateProduct = {}
    
    updateProduct['identifier'] = product['identifier']
    updateProduct['values'] = {}
    updateProduct['values']['weatherDependency'] = product['values']['indoor_outdoor']
    
    return updateProduct
    
def transform(products):
    print("Transform Products")
    productsUpdated = []
    for product in products:
        if "indoor_outdoor" in product['values']:
            weatherDependency_indoor = False
            weatherDependency_outoodor = False
            for value in product['values']["indoor_outdoor"][0]['data']:
                if "indoor" in value:
                    weatherDependency_indoor = True
                    product['values']["indoor_outdoor"][0]['data'] = ["weatherDependency_indoor"]
                    updateProduct = removeProperties(product)
                    productsUpdated.append(updateProduct)
                elif "outdoor" in value:
                    product['values']["indoor_outdoor"][0]['data'] = ["weatherDependency_outoodor"]
                    updateProduct = removeProperties(product)
                    productsUpdated.append(updateProduct)
                    weatherDependency_outoodor = True
                
            if weatherDependency_indoor and weatherDependency_outoodor:
                product['values']["indoor_outdoor"][0]['data'] = ["weatherDependency_indoor","weatherDependency_outoodor"]
                updateProduct = removeProperties(product)
                productsUpdated.append(updateProduct)
            elif not weatherDependency_indoor and weatherDependency_outoodor:
                product['values']["indoor_outdoor"][0]['data'] = ["weatherDependency_outoodor"]
                updateProduct = removeProperties(product)
                productsUpdated.append(updateProduct)
            elif weatherDependency_indoor and not weatherDependency_outoodor:
                product['values']["indoor_outdoor"][0]['data'] = ["weatherDependency_indoor"]
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