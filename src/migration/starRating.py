import service.debug as debug
import logging

####################################################################################################
# https://tourismus.atlassian.net/browse/PIM-471
# 1. Export all Products with Attribute starRating
# 2. Mapping starRating options
# 3. Upload all Products with Attribute starRating 
####################################################################################################

def getProducts(target):
    #search = 'search={"openingHours_text":[{"operator":"NOT EMPTY","value":"","locale":"de_CH"}]}'
    search = '{"starRating ":[{"operator":"NOT EMPTY","value":""}]}&attributes=starRating'
    products = target.getProductBySearch(search)
    return products

def removeProperties(product):
    updateProduct = {}
    
    updateProduct['identifier'] = product['identifier']
    updateProduct['values'] = product['values']
    
    return updateProduct
    
def transform(products):
    print("Transform Products")
    attribute = "starRating"
    productsUpdated = []
    for product in products:
        print("Transform Product: ", product['identifier'])
        if attribute in product['values']:
            if product['values'][attribute][0]['data'] == "starRating_1":
                product['values'][attribute][0]['data'] = "1"
                updateProduct = removeProperties(product)
                productsUpdated.append(updateProduct)
            elif(product['values'][attribute][0]['data'] == "starRating_2"):
                product['values'][attribute][0]['data'] = "2"
                updateProduct = removeProperties(product)
                productsUpdated.append(updateProduct)
            elif(product['values'][attribute][0]['data'] == "starRating_3"):
                product['values'][attribute][0]['data'] = "3"
                updateProduct = removeProperties(product)
                productsUpdated.append(updateProduct)
            elif(product['values'][attribute][0]['data'] == "starRating_4"):
                product['values'][attribute][0]['data'] = "4"
                updateProduct = removeProperties(product)
                productsUpdated.append(updateProduct)
            elif(product['values'][attribute][0]['data'] == "starRating_5"):
                product['values'][attribute][0]['data'] = "5"
                updateProduct = removeProperties(product)
                productsUpdated.append(updateProduct)
    
    return productsUpdated
    
def uploadProducts(target, products):
    for product in products:
        print("Upload Product: ", product['identifier'])
        print("Product: ", product)
        try:
            response = target.patchProductByCode(product['identifier'], product)
            print("Response: ", response)
        except Exception as e:
            print("Error: ", e)
            # Add To Error Log File
            debug.loggingToFile("error", e)   
             
    print("Upload Products")