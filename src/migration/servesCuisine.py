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
            for value in product['values'][attribute][0]['data']:
                if "simple_kitchen" in value:
                    product['values'][attribute][0]['data'] = value.replace("simple_kitchen", "simpleKitchen")
                elif "gluten_free_cuisine" in value:
                    product['values'][attribute][0]['data'] = value.replace("gluten_free_cuisine", "glutenFreeCuisine")
                elif "market_fresh_dishes" in value:
                    product['values'][attribute][0]['data'] = value.replace("market_fresh_dishes", "marketFreshDishes")
                elif "local_kitchen" in value:
                    product['values'][attribute][0]['data'] = value.replace("local_kitchen", "localKitchen")
                elif "swiss_specialties" in value:
                    product['values'][attribute][0]['data'] = value.replace("swiss_specialties", "swissSpecialties")
                elif "sunday_brunch" in value:
                    product['values'][attribute][0]['data'] = value.replace("sunday_brunch", "sundayBrunch")
                elif "traditional_kitchen" in value:
                    product['values'][attribute][0]['data'] = value.replace("traditional_kitchen", "traditionalKitchen")
                elif "vegan_friendly" in value:
                    product['values'][attribute][0]['data'] = value.replace("vegan_friendly", "veganFriendly")
                elif "warm_kitchen" in value:
                    product['values'][attribute][0]['data'] = value.replace("warm_kitchen", "warmKitchen")
                elif "dessert_menu" in value:
                    product['values'][attribute][0]['data'] = value.replace("dessert_menu", "dessertMenu")
                elif "home_delivery_service" in value:
                    product['values'][attribute][0]['data'] = value.replace("home_delivery_service", "homeDeliveryService")
            
            updateProduct = removeProperties(product)
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