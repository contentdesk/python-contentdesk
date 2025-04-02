import service.debug as debug
import entity.Family.Family as Family
import entity.Family.Place as Place
import entity.Family.LocalBusiness as LocalBusiness

def getSubClasses():
    subClasses = [
        "FoodEstablishment",
        "Bakery",
        "BarOrPub",
        "BeerGarden",
        "Bistro",
        "Brewery",
        "CafeOrCoffeeShop",
        "Confectionery",
        "Dairy",
        "Distillery",
        "FastFoodRestaurant",
        "Grotto",
        "IceCreamShop",
        "Imbiss",
        "MountainRestaurant",
        "Pizzeria",
        "Restaurant",
        "TakeAway",
        "Vinotheque",
        "Winery"
    ]
    return subClasses

def getProperties():
    
    properties = {}
    
    properties['acceptsReservations'] = 'acceptsReservations'
    properties['servesCuisine'] = 'servesCuisine'
    properties['starRating'] = 'starRating'
    
    # Add and merge properties from Place    
    placeProperties = LocalBusiness.getProperties()
    
    for key, value in placeProperties.items():
        print(key, value)
        properties[key] = value
        
    return properties

def setBody(family, families):
    body = Family.setBody(family, families)
    
    attribute_requirements = {"sku": "sku", "name": "name", "image": "image", "license": "license", "openstreetmap_id": "openstreetmap_id"}
    
    # https://schema.org/FoodEstablishment
    body['attributes']['acceptsReservations'] = 'acceptsReservations'
    #body['attributes']['hasMenu'] = 'hasMenu'
    body['attributes']['servesCuisine'] = 'servesCuisine'
    if 'starRating' in body['attributes']:
        body['attributes'].pop('starRating')
        if 'starRating' in body['attributes']:
            del body['attributes']['starRating']

    ## Contentdesk.io Settings
    body['attributes']['license'] = 'license'
    body['attributes']['copyrightHolder'] = 'copyrightHolder'
    body['attributes']['author'] = 'author'

    body['attributes']['typicalAgeRange'] = 'typicalAgeRange'
    body['attributes']['gender'] = 'gender'
    
    body['attributes']['award'] = 'award'
    
    body['attributes']['metaTitle'] = 'metaTitle'
    body['attributes']['metaDescription'] = 'metaDescription'
    body['attributes']['canonicalUrl'] = 'canonicalUrl'
    
    body['attributes']['openstreetmap_id'] = 'openstreetmap_id'

    body['attributes']['image_01_scope'] = 'image_01_scope'
    body['attributes']['image_02_scope'] = 'image_02_scope'
    body['attributes']['image_03_scope'] = 'image_03_scope'
    body['attributes']['image_04_scope'] = 'image_04_scope'
    body['attributes']['image_05_scope'] = 'image_05_scope'
    body['attributes']['image_06_scope'] = 'image_06_scope'
    body['attributes']['image_07_scope'] = 'image_07_scope'
    body['attributes']['image_08_scope'] = 'image_08_scope'
    body['attributes']['image_09_scope'] = 'image_09_scope'
    body['attributes']['image_10_scope'] = 'image_10_scope'

    body['attributes']['image_01_scope_description'] = 'image_01_scope_description'
    body['attributes']['image_02_scope_description'] = 'image_02_scope_description'
    body['attributes']['image_03_scope_description'] = 'image_03_scope_description'
    body['attributes']['image_04_scope_description'] = 'image_04_scope_description'
    body['attributes']['image_05_scope_description'] = 'image_05_scope_description'
    body['attributes']['image_06_scope_description'] = 'image_06_scope_description'
    body['attributes']['image_07_scope_description'] = 'image_07_scope_description'
    body['attributes']['image_08_scope_description'] = 'image_08_scope_description'
    body['attributes']['image_09_scope_description'] = 'image_09_scope_description'
    body['attributes']['image_10_scope_description'] = 'image_10_scope_description'
    
    # marker Icon
    body['attributes']['markerIcon'] = 'markerIcon'
    
    body['attribute_requirements'] = {}
    body["attribute_requirements"]['ecommerce'] = attribute_requirements
    body["attribute_requirements"]['mice'] = attribute_requirements
    
    # Add and merge properties from Place    
    placeProperties = Place.getProperties()
    
    for key, value in placeProperties.items():
        print(key, value)
        body["attributes"][key] = value
    
    return body


