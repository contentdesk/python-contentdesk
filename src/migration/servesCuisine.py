import service.debug as debug
import logging

############################################################################################################
# https://tourismus.atlassian.net/browse/PIM-482
# 1. Export all Products with Attribute servesCuisine 
# 2. Mapping servesCuisine  options
# 3. Upload all Products with Attribute servesCuisine 
############################################################################################################

def getProducts(target):
    #search = 'search={"openingHours_text":[{"operator":"NOT EMPTY","value":"","locale":"de_CH"}]}'
    search = '{"servesCuisine  ":[{"operator":"NOT EMPTY","value":""}]}&attributes=servesCuisine'
    products = target.getProductBySearch(search)
    return products

def removeProperties(product):
    updateProduct = {}
    
    updateProduct['identifier'] = product['identifier']
    updateProduct['values'] = {}
    updateProduct['values']['servesCuisine'] = product['values']['servesCuisine']
    
    return updateProduct
    
def transform(products):
    print("Transform Products")
    attribute = 'servesCuisine'
    productsUpdated = []
    for product in products:
        if attribute in product['values']:
            i = 0
            for value in product['values'][attribute][0]['data']:
                if "simple_kitchen" in value:
                    product['values'][attribute][0]['data'][i] = "simpleKitchen"
                elif "gluten_free_cuisine" in value:
                    product['values'][attribute][0]['data'][i] = "glutenFreeCuisine"
                elif "market_fresh_dishes" in value:
                    product['values'][attribute][0]['data'][i] = "marketFreshDishes"
                elif "local_kitchen" in value:
                    product['values'][attribute][0]['data'][i] = "localKitchen"
                elif "swiss_specialties" in value:
                    product['values'][attribute][0]['data'][i] = "swissSpecialties"
                elif "sunday_brunch" in value:
                    product['values'][attribute][0]['data'][i] = "sundayBrunch"
                elif "traditional_kitchen" in value:
                    product['values'][attribute][0]['data'][i] = "traditionalKitchen"
                elif "vegan_friendly" in value:
                    product['values'][attribute][0]['data'][i] = "veganFriendly"
                elif "warm_kitchen" in value:
                    product['values'][attribute][0]['data'][i] ="warmKitchen"
                elif "dessert_menu" in value:
                    product['values'][attribute][0]['data'][i] = "dessertMenu"
                elif "home_delivery_service" in value:
                    product['values'][attribute][0]['data'][i] = "homeDeliveryService"
                i = i + 1
            
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