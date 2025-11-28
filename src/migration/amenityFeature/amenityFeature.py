import service.debug as debug
import logging

############################################################################################################
# https://tourismus.atlassian.net/browse/CDESK-40
# 1. Export all Products with Attribute amenityFeature
# 2. Delete amenityFeature and Remove amenityFeature options
# 3. Create amenityFeature options
# 4. Products remove old amenityFeature options
# 5. Upload all Products with Attribute amenityFeature  
############################################################################################################

# Problem
# Produktfamilies lost amenityFeature Attribut

def getProducts(target):
    #search = 'search={"openingHours_text":[{"operator":"NOT EMPTY","value":None,"locale":"de_CH"}]}'
    search = '{"amenityFeature":[{"operator":"NOT EMPTY","value":""}]}&attributes=amenityFeature'
    products = target.getProductBySearch(search)
    return products