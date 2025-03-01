import entity.Family.Family as Family
import entity.Family.Place as Place
import entity.Family.LocalBusiness as LocalBusiness

def getSubClasses():
    subClasses = [
        "LodgingBusiness",
        "Agrotourism",
        "BedAndBreakfast",
        "Campground",
        "FarmLodging",
        "GroupAccommodation",
        "GuestHouse",
        "HolidayApartment",
        "HolidayHouse",
        "Hostel",
        "Hotel",
        "IglooVillage",
        "Motel",
        "Mountainhut",
        "ManagedHut",
        "RescueHut",
        "SelfCateredHut",
        "Pension",
        "Pitch",
        "PrivateRoom",
        "Resort"
    ]
    return subClasses

def setBody(family, families):
    body = Family.setBody(family, families)
    
    attribute_requirements = {"sku": "sku", "name": "name", "image": "image", "license": "license", "openstreetmap_id": "openstreetmap_id"}
    attribute_requirementsMice = {"sku": "sku", "name": "name", "image": "image", "license": "license", "openstreetmap_id": "openstreetmap_id"}
    
    # https://schema.org/LodgingBusiness
    body['attributes']['amenityFeature'] = 'amenityFeature'
    # body['attributes']['audience'] = 'audience' ?
    body['attributes']['availableLanguage'] = 'availableLanguage'
    body['attributes']['checkinTime'] = 'checkinTime'
    body['attributes']['checkoutTime'] = 'checkoutTime'
    body['attributes']['numberOfRooms'] = 'numberOfRooms'
    body['attributes']['petsAllowed'] = 'petsAllowed'
    body['attributes']['starRating'] = 'starRating'
    
    ## Contentdesk.io Settings
    body['attributes']['superior'] = 'superior'
    body['attributes']['garni'] = 'garni'

    if 'daytime' in body['attributes']:
        body['attributes'].pop('daytime', None)
        if 'daytime' in body['attributes']:
            del body['attributes']['daytime']
    
    if 'duration' in body['attributes']:
        body['attributes'].pop('duration', None)
        if 'duration' in body['attributes']:
            del body['attributes']['duration']

    body['attributes']['license'] = 'license'
    body['attributes']['copyrightHolder'] = 'copyrightHolder'
    body['attributes']['author'] = 'author'
    
    body['attributes']['award'] = 'award'

    body['attributes']['typicalAgeRange'] = 'typicalAgeRange'
    body['attributes']['gender'] = 'gender'

    body['attributes']['metaTitle'] = 'metaTitle'
    body['attributes']['metaDescription'] = 'metaDescription'
    body['attributes']['canonicalUrl'] = 'canonicalUrl'
    
    body['attributes']['openstreetmap_id'] = 'openstreetmap_id'

    body['attributes']['image_summer'] = 'image_summer'
    body['attributes']['image_winter'] = 'image_winter'

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
    
    # discover.swiss Testing
    body['attributes']['parking'] = 'parking'
    body['attributes']['publicTransport'] = 'publicTransport'
    
    body['attribute_requirements'] = {}
    body["attribute_requirements"]['ecommerce'] = attribute_requirements
    body["attribute_requirements"]['mice'] = attribute_requirements
    
    ## plus Properties from LocalBusiness + Place!
    # Add and merge properties from Place    
    localBusinessProperties = LocalBusiness.getProperties()
    
    for key, value in localBusinessProperties.items():
        print(key, value)
        body["attributes"][key] = value
    
    # Add and merge properties from Place    
    placeProperties = Place.getProperties()
    
    for key, value in placeProperties.items():
        print(key, value)
        body["attributes"][key] = value
    
    return body