import service.debug as debug
import logging

############################################################################################################
# https://tourismus.atlassian.net/browse/PIM-468
# 1. Export all Products with Attribute features 
# 2. Mapping amenityFeature   options
# 3. Upload all Products with Attribute amenityFeature  
############################################################################################################

def getProducts(target):
    #search = 'search={"openingHours_text":[{"operator":"NOT EMPTY","value":None,"locale":"de_CH"}]}'
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
        "apartments_with_hotel_service":None,
        "half_board_supplement":"food_halfboard",
        "full_board_supplement":"food_fullboard",
        "viewpoint":None,
        "balcony":"view_balcony",
        "bar":"food_bar",
        "bar_bistro":"food_bar",
        "particularly_quiet_location":"location_quietlocation",
        "particularly_quiet_rooms":None,
        "catering":None,
        "family_friendly":"characteristics_familyfriendly",
        "fumoir":"furnishing_smokingrooms",
        "hotel_garden_or_park":"outdoor_garden",
        "grill_restaurant":None,
        "free_wifi":"furnishing_wifi",
        "exercise_gym":"sport_fitnessRoom",
        "indoor_pool":"sport_indoorswimmingpool",
        "home_delivery_service":None,
        "pets_welcome":"characteristics_petfriendly",
        "pets_not_allowed":"characteristics_nopetsallowed",
        "historical_building":None,
        "internet_access":"furnishing_internetaccess",
        "coffee_machine":"food_coffeemachine",
        "kids_beds":"family_children_cribs",
        "air_conditioning":"furnishing_airconditioning",
        "kitchenette":"food_kitchenette",
        "credit_cards_accepted":None,
        "electric_car_charging_station":"general_chargingstationElectricvehicles",
        "elevators":"general_lift",
        "microwave_oven":"food_microwave",
        "minibar":"food_minibar",
        "non_smoking":"characteristics_nonsmoking",
        "public_parking":"general_carpark",
        "public_restaurant":"food_restaurant",
        "outdoor_parking":None,
        "aII_rooms_with_radio":"media_radio",
        "radio_tv":"media_tv",
        "reservation_also_through_travel_agencies":None,
        "restaurant":"food_restaurant",
        "wheelchair_accessible_toilet":None,
        "wheelchair_access":None,
        "meeting_room":None,
        "sauna":"wellness_sauna",
        "diet_meals":None,
        "pool":None,
        "snack_restaurant":"food_snackbar",
        "conference_and_banqueting_rooms":None,
        "all_rooms_with_telephone":"media_telephone",
        "garden_terrace":"view_terrace",
        "textile_cleaning_service":None,
        "indoor_parking":None,
        "aII_rooms_with_tv":"media_tv",
        "washing_machine":"general_washingmachine",
        "health_club":None,
        "rooms_with_private_bathroom":None,
        "rooms_without_private_bathroom":None,
        "room_with_wc":None,
        "bike_friendly":None,
        "ebike_friendly":"sport_chargingstationEbikes",
        "disabled_parking":None,
        "playground":"entertainment_playground",
        "bus_parking_available":"general_busparking",
        "public_transportation":None,
        "storage_room":"ski_skiequipmentstorage",
        "family_friendly_playground":"entertainment_playroom",
        "family_friendly_toys":None,
        "family_friendly_books":None,
        "family_friendly_kidschair":"general_highchairForChildren",
        "family_friendly_diaper":None,
        "family_friendly_childrenmenu":None,
        "family_friendly_childcare":"entertainment_childcareservice",
        "veloabstellraum":"general_bicyclestoragearea",
        "Bikeshop":"sport_bikerental",
        "Trockenraum":"furnishing_tumbledryer",
        "Waescheservice":"general_laundryservice",
    }
    
    return mappingList

def removeList():
    removeList = {
        "apartments_with_hotel_service",
        "viewpoint",
        "particularly_quiet_rooms",
        "catering",
        "grill_restaurant",
        "home_delivery_service",
        "historical_building",
        "credit_cards_accepted",
        "outdoor_parking",
        "reservation_also_through_travel_agencies",
        "wheelchair_accessible_toilet",
        "wheelchair_access",
        "meeting_room",
        "diet_meals",
        "pool",
        "conference_and_banqueting_rooms",
        "textile_cleaning_service",
        "indoor_parking",
        "health_club",
        "rooms_with_private_bathroom",
        "rooms_without_private_bathroom",
        "room_with_wc",
        "bike_friendly",
        "disabled_parking",
        "public_transportation",
        "family_friendly_toys",
        "family_friendly_books",
        "family_friendly_diaper",
        "family_friendly_childrenmenu"
        }
    return removeList
        
    
def transform(products):
    print("Transform Products")
    attribute = 'features'
    productsUpdated = []
    mappingValues = mappingList()
    removeValues = removeList()
    for product in products:
        print("Product: ", product['identifier'])
        i = 0
        
        # replace Values in List product['values'][attribute][0]['data']
        product['values'][attribute][0]['data'] = [mappingValues.get(value, value) for value in product['values'][attribute][0]['data']]
        
        
        # remove Values from List product['values'][attribute][0]['data']
        product['values'][attribute][0]['data'] = [value for value in product['values'][attribute][0]['data'] if value not in removeValues]
        
        
        for value in product['values'][attribute][0]['data']:
            print ("Value: ", value)
            if value in mappingValues:
                print ("Value in mappingList")
            else: 
                print ("Value not in mappingList")
            for key in mappingValues:
                if value == key:
                    print ("Key: ", key)
                    print ("Value: ", value)
                    print ("Mapping Value: ", mappingValues[key])
                    if mappingValues[key] != None:
                        print ("Replace Value: ", mappingValues[key] )
                        product['values'][attribute][0]['data'][i] = mappingValues[key]
                    if mappingValues[key] == None:
                        # Remove Value from List
                        print ("Remove Value: ", value)
                        product['values'][attribute][0]['data'][i].remove()
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
            response = target.patchProductByCode(product['identifier'], product)
            print("Response: ", response)
        except Exception as e:
            print("Error: ", e)
            # Add To Error Log File
            debug.loggingToFile("error", e)   
             
    print("Upload Products")