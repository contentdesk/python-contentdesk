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
        if attribute in product["values"]:
            #productsUpdated.append(product)
            for openingHours in product["values"][attribute]:
                newOpeningHours = []
                for hours in openingHours['data']:
                    print(hours)
                    for key, value in hours.items():
                        if key == "opens" or key == "closes":
                            if value is not None:
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
            productsUpdated.append(product)
            print(product["values"][attribute])
    return productsUpdated

def uploadProducts(target, products):
    # save on file for manual fix
    # stop here
    debug.addToFileMigration("test", "openingHoursSpecification", 'upload', products)