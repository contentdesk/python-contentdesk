import service.debug as debug
import logging

############################################################################################################
# https://tourismus.atlassian.net/browse/PIM-470
# 1. Export all Products with Attribute labels 
# 2. Mapping award    options
# 3. Upload all Products with Attribute award   
############################################################################################################

def getProducts(target):
    #search = 'search={"openingHours_text":[{"operator":"NOT EMPTY","value":"","locale":"de_CH"}]}'
    search = '{"labels":[{"operator":"NOT EMPTY","value":""}]}&attributes=labels'
    products = target.getProductBySearch(search)
    return products

def removeProperties(product):
    updateProduct = {}
    
    updateProduct['identifier'] = product['identifier']
    updateProduct['values'] = {}
    updateProduct['values']['award'] = product['values']['labels']
    
    return updateProduct

def mappingList():
    mappingList = {
        "hotellerie_suisse_1": "hotellerieSuisse1",
        "hotellerie_suisse_1s": "hotellerieSuisse1s",
        "hotellerie_suisse_2": "hotellerieSuisse2",
        "hotellerie_suisse_2s": "hotellerieSuisse2s",
        "hotellerie_suisse_3": "hotellerieSuisse3",
        "hotellerie_suisse_3s": "hotellerieSuisse3s",
        "hotellerie_suisse_4": "hotellerieSuisse4",
        "hotellerie_suisse_4s": "hotellerieSuisse4s",
        "hotellerie_suisse_5": "hotellerieSuisse5",
        "hotellerie_suisse_5s": "hotellerieSuisse5s",
        "gastro_suisse_1": "gastroSuisse1",
        "gastro_suisse_2": "gastroSuisse2",
        "gastro_suisse_3": "gastroSuisse3",
        "gastro_suisse_4": "gastroSuisse4",
        "gastro_suisse_5": "gastroSuisse5",
        "apartment_1": "holidayApartment1",
        "apartment_1s": "holidayApartment1s",
        "apartment_2": "holidayApartment2",
        "apartment_2s": "holidayApartment2s",
        "apartment_3": "holidayApartment3",
        "apartment_3s": "holidayApartment3s",
        "apartment_4": "holidayApartment4",
        "apartment_4s": "holidayApartment4s",
        "apartment_5": "holidayApartment5",
        "apartment_5s": "holidayApartment5s",
        "bio_knospe": "bioKnospe",
        "bio_gourmet_knospe": "bioGourmetKnospe",
        "bio_suisse_knospe": "bioSuisseKnospe",
        "bnb_1": "bedAndBreakfast1",
        "bnb_2": "bedAndBreakfast2",
        "bnb_3": "bedAndBreakfast3",
        "bnb_4": "bedAndBreakfast4",
        "bnb_5": "bedAndBreakfast5",
        "culinarium": "culinarium",
        "gilde": "gilde",
        "guide_bleu": "guideBleu",
        "jeunes_restaurateurs": "jeunesRestaurateurs",
        "q1": None,
        "q2": None,
        "q3": None,
        "schweiz_mobil": None,
        "fisch": None,
        "family_destination": None,
        "wellness_destination": None,
        "gault_millau_12": None,
        "gault_millau_13": None,
        "gault_millau_14": None,
        "gault_millau_15": None,
        "gault_millau_16": None,
        "gault_millau_17": None,
        "gault_millau_18": None,
        "gault_millau_19": None,
        "guide_michelin_1": None,
        "guide_michelin_2": None,
        "guide_michelin_3": None,
        "swisstainable_1": None,
        "swisstainable_2": None,
        "swisstainable_3": None,
        "ok_go": None,
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
            response = target.patchProductByCode(product['identifier'], product)
            print("Response: ", response)
        except Exception as e:
            print("Error: ", e)
            # Add To Error Log File
            debug.loggingToFile("error", e)   
             
    print("Upload Products")