import service.debug as debug
import logging

############################################################################################################
# https://tourismus.atlassian.net/browse/PIM-468
# 1. Export all Products with Attribute features 
# 2. Mapping amenityFeature   options
# 3. Upload all Products with Attribute amenityFeature  
############################################################################################################

def getProducts(target):
    #search = 'search={"openingHours_text":[{"operator":"NOT EMPTY","value":"","locale":"de_CH"}]}'
    search = '{"features":[{"operator":"NOT EMPTY","value":""}]}&attributes=features'
    products = target.getProductBySearch(search)
    return products

def removeProperties(product):
    updateProduct = {}
    
    updateProduct['identifier'] = product['identifier']
    updateProduct['values'] = {}
    updateProduct['values']['amenityFeature'] = product['values']['features']
    
    return updateProduct

def mappingList():
    mappingList = {
        "half_board_supplement": "food_halfboard",
        "full_board_supplement": "food_fullboard",
        "balcony": "view_balcony",
        "bar": "food_bar",
        "bar_bistro": "food_bar"
    }
    
    return mappingList
    
def transform(products):
    print("Transform Products")
    attribute = 'features'
    productsUpdated = []
    for product in products:
        if attribute in product['values']:
            i = 0
            for value in product['values'][attribute][0]['data']:
                if "half_board_supplement" in value:
                    product['values'][attribute][0]['data'][i] = "food_halfboard"
                elif "full_board_supplement" in value:
                    product['values'][attribute][0]['data'][i] = "food_fullboard"
                elif "balcony" in value:
                    product['values'][attribute][0]['data'][i] = "marketFreshDishes"
                elif "bar" in value:
                    product['values'][attribute][0]['data'][i] = "localKitchen"
                elif "bar_bistro" in value:
                    product['values'][attribute][0]['data'][i] = "swissSpecialties"
                elif "family_friendly" in value:
                    product['values'][attribute][0]['data'][i] = "sundayBrunch"
                elif "fumoir" in value:
                    product['values'][attribute][0]['data'][i] = "traditionalKitchen"
                elif "hotel_garden_or_park" in value:
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
            #response = target.patchProductByCode(product['identifier'], product)
            #print("Response: ", response)
        except Exception as e:
            print("Error: ", e)
            # Add To Error Log File
            debug.loggingToFile("error", e)   
             
    print("Upload Products")