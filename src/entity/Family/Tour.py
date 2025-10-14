import entity.Family.Family as Family
import entity.Family.Place as Place

def getSubClasses():
    subClasses = [
        "Longdistance",
        "Route",
        "GlacierTour",
        "HighTour",
        "MotorisedTours",
        "BusTour",
        "CarTour",
        "MotorTour",
        "QuadTour",
        "SegwayTour",
        "ShipTour",
        "TrainTour",
        "ThemeTrail",
        "ViaFerrata",
        "Way",
        "AlpineHikingtrail",
        "BikeTrail",
        "CrossCountry",
        "HikingTrail",
        "MountainHikingtrail",
        "NatureTrail",
        "SkiRoute",
        "SkiSlope",
        "SnowshoeTrail",
        "TobogganRun",
        "WinterHiking",
    ]
    return subClasses

def getProperties():
    properties = {}
    
    # https://docs.discover.swiss/dev/reference/dataschema/definition/infocenter-classes/Tour/
    
    print(" - SET GEO")
    properties['geo'] = 'geo'
    
    # Tour specific
    properties['seasonOfYear'] = 'seasonOfYear'
    properties['length'] = 'length'
    properties['difficulty'] = 'difficulty'
    properties['estimatedDuration'] = 'estimatedDuration'
    properties['uphillElevation'] = 'uphillElevation'
    properties['downhillElevation'] = 'downhillElevation'
    properties['highestPoint'] = 'highestPoint'
    properties['lowestPoint'] = 'lowestPoint'
    properties['recommendedEquipment'] = 'recommendedEquipment'
    properties['circularTrail'] = 'circularTrail'
    properties['directions'] = 'directions'
    properties['startingPointDescription'] = 'startingPointDescription'
    properties['destination'] = 'destination'
    properties['condition'] = 'condition'
    properties['technique'] = 'technique'
    properties['qualityOfExperience'] = 'qualityOfExperience'
    properties['landscape'] = 'landscape'


    placeProperties = Place.getProperties()
    
    for key, value in placeProperties.items():
        properties[key] = value
        
    # remove properties not used in Tour
    if 'latitude' in properties:
        del properties['latitude']
    if 'longitude' in properties:
        del properties['longitude']

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

def setBodyOld(family, families):
    body = Place.setBody(family, families)

    attribute_requirements = {"sku": "sku", "name": "name", "image": "image", "license": "license"}
    
    body['attributes']['name'] = 'name'
    body['attributes']['disambiguatingDescription'] = 'disambiguatingDescription'
    body['attributes']['description'] = 'description'
    body['attributes']['image'] = 'image'
    body['attributes']['image_description'] = 'image_description'

    body['attributes']['license'] = 'license'
    body['attributes']['copyrightHolder'] = 'copyrightHolder'
    body['attributes']['author'] = 'author'
    
    print(" - SET GEO")
    body['attributes']['geo'] = 'geo'

    # https://docs.discover.swiss/dev/reference/dataschema/definition/infocenter-classes/Tour/
    body['attributes']['duration'] = 'duration'
    body['attributes']['isAccessibleForFree'] = 'isAccessibleForFree'
    body['attributes']['maximumAttendeeCapacity'] = 'maximumAttendeeCapacity'
    body['attributes']['openingHoursSpecification'] = 'openingHoursSpecification'
    body['attributes']['openingHours'] = 'openingHours'
    body['attributes']['publicAccess'] = 'publicAccess'

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

    return body