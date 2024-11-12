import service.debug as debug
import logging
from datetime import datetime, timedelta

####################################################################################################
# https://tourismus.atlassian.net/browse/PIM-521
# 1. Export all Products with Attribute openingHoursSpecification
# 2. Manuell Fix openingHoursSpecification
# 3. Upload all Products with Attribute openingHoursSpecification 
####################################################################################################

def getProducts(target):
    #search = 'search={"openingHours_text":[{"operator":"NOT EMPTY","value":"","locale":"de_CH"}]}'
    #search = '{"starRating ":[{"operator":"NOT EMPTY","value":""}]}&attributes=starRating'
    products = target.getProducts()
    return products

def transform(products):
    attribute = "openingHoursSpecification"
    productsUpdated = []
    for product in products:
        productUpdate = {}
        productUpdate["identifier"] = product["identifier"]
        productUpdate["values"] = {}
        productUpdate["values"][attribute] = []
        productUpdate["values"][attribute].append({})
        if attribute in product["values"]:
            #productsUpdated.append(product)
            for openingHours in product["values"][attribute]:
                newOpeningHours = []
                for hours in openingHours['data']:
                    print(hours)
                    for key, value in hours.items():
                        if key == "opens" or key == "closes":
                            if value is not None:
                                if "Z" in value:
                                    openingHours[key] = (datetime.strptime(value.replace("Z", ""), "%H:%M") + timedelta(hours=2)).strftime("%H:%M")
                                    print(openingHours[key])
                                    # replace value in product
                                    hours[key] = openingHours[key]
                    print (hours)
                    # add to array
                    newOpeningHours.append(hours)
                # replace value in product
                openingHours['data'] = newOpeningHours
                print (openingHours)
            # add to product
            productUpdate["values"][attribute][0]['locale'] = None
            productUpdate["values"][attribute][0]['scope'] = None
            productUpdate["values"][attribute][0]['data'] = newOpeningHours
            print(productUpdate["values"][attribute])
            productsUpdated.append(productUpdate)
            #print(product["values"][attribute])
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