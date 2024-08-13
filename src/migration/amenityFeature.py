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
        "apartments_with_hotel_service":"",
        "half_board_supplement":"food_halfboard",
        "full_board_supplement":"food_fullboard",
        "viewpoint":"",
        "balcony":"view_balcony",
        "bar":"food_bar",
        "bar_bistro":"food_bar",
        "particularly_quiet_location":"location_quietlocation",
        "particularly_quiet_rooms":"",
        "catering":"",
        "family_friendly":"characteristics_familyfriendly",
        "fumoir":"furnishing_smokingrooms",
        "hotel_garden_or_park":"outdoor_garden",
        "grill_restaurant":"",
        "free_wifi":"furnishing_wifi",
        "exercise_gym":"sport_fitnessRoom",
        "indoor_pool":"sport_indoorswimmingpool",
        "home_delivery_service":"",
        "pets_welcome":"characteristics_petfriendly",
        "pets_not_allowed":"characteristics_nopetsallowed",
        "historical_building":"",
        "internet_access":"furnishing_internetaccess",
        "coffee_machine":"food_coffeemachine",
        "kids_beds":"family_children_cribs",
        "air_conditioning":"furnishing_airconditioning",
        "kitchenette":"food_kitchenette",
        "credit_cards_accepted":"",
        "electric_car_charging_station":"general_chargingstationElectricvehicles",
        "elevators":"general_lift",
        "microwave_oven":"food_microwave",
        "minibar":"food_minibar",
        "non_smoking":"characteristics_nonsmoking",
        "public_parking":"general_carpark",
        "public_restaurant":"food_restaurant",
        "outdoor_parking":"",
        "aII_rooms_with_radio":"media_radio",
        "radio_tv":"media_tv",
        "reservation_also_through_travel_agencies":"",
        "restaurant":"food_restaurant",
        "wheelchair_accessible_toilet":"",
        "wheelchair_access":"",
        "meeting_room":"",
        "sauna":"wellness_sauna",
        "diet_meals":"",
        "pool":"",
        "snack_restaurant":"food_snackbar",
        "conference_and_banqueting_rooms":"",
        "all_rooms_with_telephone":"media_telephone",
        "garden_terrace":"view_terrace",
        "textile_cleaning_service":"",
        "indoor_parking":"",
        "aII_rooms_with_tv":"media_tv",
        "washing_machine":"general_washingmachine",
        "health_club":"",
        "rooms_with_private_bathroom":"",
        "rooms_without_private_bathroom":"",
        "room_with_wc":"",
        "bike_friendly":"",
        "ebike_friendly":"sport_chargingstationEbikes",
        "disabled_parking":"",
        "playground":"entertainment_playground",
        "bus_parking_available":"general_busparking",
        "public_transportation":"",
        "storage_room":"ski_skiequipmentstorage",
        "family_friendly_playground":"entertainment_playroom",
        "family_friendly_toys":"",
        "family_friendly_books":"",
        "family_friendly_kidschair":"general_highchairForChildren",
        "family_friendly_diaper":"",
        "family_friendly_childrenmenu":"",
        "family_friendly_childcare":"entertainment_childcareservice",
        "veloabstellraum":"general_bicyclestoragearea",
        "Bikeshop":"",
        "Trockenraum":"",
        "Waescheservice":"general_laundryservice",
    }
    
    return mappingList
    
def transform(products):
    print("Transform Products")
    attribute = 'features'
    productsUpdated = []
    mappingValues = mappingList()
    for product in products:
        print("Product: ", product['identifier'])
        i = 0
        for value in product['values'][attribute][0]['data']:
            for key in mappingValues:
                if value == key:
                    print ("Key: ", key)
                    print ("Value: ", value)
                    print ("Mapping Value: ", mappingValues[key])
                    if mappingValues[key] != "":
                        print ("Replace Value: ", mappingValues[key] )
                        product['values'][attribute][0]['data'][i] = mappingValues[key]
                    if mappingValues[key] == "":
                        # Remove Value from List
                        print ("Remove Value: ", value)
                        product['values'][attribute][0]['data'].remove(key)
                if value == "Trockenraum":
                    print ("Achtung Trockenraum")
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