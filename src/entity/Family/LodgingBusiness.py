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

def getProperties():
    properties = {}
    
    # https://schema.org/LodgingBusiness
    properties['amenityFeature'] = 'amenityFeature'
    # body['attributes']['audience'] = 'audience' ?
    properties['availableLanguage'] = 'availableLanguage'
    properties['checkinTime'] = 'checkinTime'
    properties['checkoutTime'] = 'checkoutTime'
    properties['numberOfRooms'] = 'numberOfRooms'
    properties['petsAllowed'] = 'petsAllowed'
    properties['starRating'] = 'starRating'
    
    properties['license'] = 'license'
    properties['copyrightHolder'] = 'copyrightHolder'
    properties['author'] = 'author'
    
    ## Contentdesk.io Settings
    properties['superior'] = 'superior'
    properties['garni'] = 'garni'
    properties['trustyou_id'] = 'trustyou_id'
    properties['tripadvisor_id'] = 'tripadvisor_id'

    properties['award'] = 'award'

    properties['typicalAgeRange'] = 'typicalAgeRange'
    properties['gender'] = 'gender'

    properties['metaTitle'] = 'metaTitle'
    properties['metaDescription'] = 'metaDescription'
    properties['canonicalUrl'] = 'canonicalUrl'
    
    properties['openstreetmap_id'] = 'openstreetmap_id'

    properties['image_summer'] = 'image_summer'
    properties['image_winter'] = 'image_winter'

    properties['image_01_scope'] = 'image_01_scope'
    properties['image_02_scope'] = 'image_02_scope'
    properties['image_03_scope'] = 'image_03_scope'
    properties['image_04_scope'] = 'image_04_scope'
    properties['image_05_scope'] = 'image_05_scope'
    properties['image_06_scope'] = 'image_06_scope'
    properties['image_07_scope'] = 'image_07_scope'
    properties['image_08_scope'] = 'image_08_scope'
    properties['image_09_scope'] = 'image_09_scope'
    properties['image_10_scope'] = 'image_10_scope'

    properties['image_01_scope_description'] = 'image_01_scope_description'
    properties['image_02_scope_description'] = 'image_02_scope_description'
    properties['image_03_scope_description'] = 'image_03_scope_description'
    properties['image_04_scope_description'] = 'image_04_scope_description'
    properties['image_05_scope_description'] = 'image_05_scope_description'
    properties['image_06_scope_description'] = 'image_06_scope_description'
    properties['image_07_scope_description'] = 'image_07_scope_description'
    properties['image_08_scope_description'] = 'image_08_scope_description'
    properties['image_09_scope_description'] = 'image_09_scope_description'
    properties['image_10_scope_description'] = 'image_10_scope_description'
    
    # marker Icon
    properties['markerIcon'] = 'markerIcon'
    
    # discover.swiss Testing
    properties['parking'] = 'parking'
    properties['publicTransport'] = 'publicTransport'
    
    localBusinessProperties = LocalBusiness.getProperties()
    
    for key, value in localBusinessProperties.items():
        properties[key] = value
    
    return properties
    

def setBody(family, families):
    body = Family.setBody(family, families)
    
    attribute_requirements = {"sku": "sku", "name": "name", "image": "image", "license": "license", "openstreetmap_id": "openstreetmap_id"}
    attribute_requirementsMice = {"sku": "sku", "name": "name", "image": "image", "license": "license", "openstreetmap_id": "openstreetmap_id"}
    
    body['attribute_requirements'] = {}
    body["attribute_requirements"]['ecommerce'] = attribute_requirements
    body["attribute_requirements"]['mice'] = attribute_requirements
    
    body['attributes'] = {}
     
    # Add and merge properties from getProperties    
    body["attributes"] = getProperties()
    
    return body