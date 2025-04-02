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
    
    ## Contentdesk.io Settings
    properties['typicalAgeRange'] = 'typicalAgeRange'
    properties['gender'] = 'gender'
    
    # Add and merge properties from Place    
    placeProperties = LocalBusiness.getProperties()
    
    for key, value in placeProperties.items():
        properties[key] = value
        
    return properties

def setBody(family, families):
    body = Family.setBody(family, families)
    
    attribute_requirements = {"sku": "sku", "name": "name", "image": "image", "license": "license", "openstreetmap_id": "openstreetmap_id"}

    body['attribute_requirements'] = {}
    body["attribute_requirements"]['ecommerce'] = attribute_requirements
    body["attribute_requirements"]['mice'] = attribute_requirements
    
    body['attributes'] = {}
    body['attributes'] = getProperties()
    
    return body


