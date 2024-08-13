import service.debug as debug
import logging

####################################################################################################
# https://tourismus.atlassian.net/browse/PIM-472
# 1. Export all Products with Attribute action_button_text
# 2. Copy the value of action_button_text to potentialAction
# 3. Upload all Products with Attribute potentialAction
####################################################################################################

def getProducts(target):
    #locales = ['de_CH', 'en_US', 'fr_FR', 'it_IT']
    #locales = target.getLocales(search='{"enabled":[{"operator":"=","value":true}]}')
    #print("locales: ", locales)
    scopes = target.getChannels()
    print("scopes: ", scopes)
    #search = 'search={"openingHours_text":[{"operator":"NOT EMPTY","value":"","locale":"de_CH"}]}'
    getProducts = {}
    for scope in scopes:
        print("Scope: ", scope['code'])
        for locale in scope['locales']:
            print("Locale: ", locale)
            search = '{"action_button_text":[{"operator":"NOT EMPTY","value":"","locale":"' + locale+'","scope":"'+scope['code']+'"}]}&attributes=action_button_text'
            products = target.getProductBySearch(search)
            for product in products:
                print("Product: ", product['identifier'])
                getProducts[product['identifier']] = product
        
    #search = '{"action_button_url":[{"operator":"NOT EMPTY","value":"","locale":"en_US","scope":"mobile"}]}&attributes=action_button_url&search_locale=en_US'
    #products = target.getProductBySearch(search)
    return getProducts

def removeProperties(product):
    updateProduct = {}
    updateProduct['identifier'] = product['identifier']
    updateProduct['values'] = {}
    updateProduct['values']['potentialAction'] = product['values']['action_button_text']
    
    return updateProduct

def transform(getProducts):
    print("Transform Products")
    attribute = 'action_button_text'
    productsUpdated = []
    for products in getProducts:
        print("Product: ", products)
        if attribute in getProducts[products]['values']:
            i = 0
            for value in getProducts[products]['values'][attribute]:
                if value['data'] == "ticketing":
                    getProducts[products]['values'][attribute][i]['data'] = "ReserveAction"
                elif value['data']  == "booking":
                    getProducts[products]['values'][attribute][i]['data'] = "ReserveAction"
                elif value['data']  == "offer":
                    getProducts[products]['values'][attribute][i]['data'] = "ViewAction"
                elif value['data']  == "onlineshop":
                    getProducts[products]['values'][attribute][i]['data'] = "BuyAction"
                elif value['data']  == "website":
                    getProducts[products]['values'][attribute][i]['data'] = "ViewAction"
                i = i + 1
            updateProduct = removeProperties(getProducts[products])
            productsUpdated.append(updateProduct)
    
    return productsUpdated

def uploadProducts(target, products):

    for product in products:
        print("Upload Product: ", product['identifier'])
        print("Product: ", product)
        try:
            print("Start Upload")
            #response = target.patchProductByCode(product['identifier'], product)
            #print("Response: ", response)
        except Exception as e:
            print("Error: ", e)
            # Add To Error Log File
            debug.loggingToFile("error", e)   
             
    print("Upload Products")