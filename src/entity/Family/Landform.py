import entity.Family.Family as Family
import entity.Family.Place as Place

def getSubClasses():
    subClasses = [
          "Landform",
          "BodyOfWater",
          "LakeBodyOfWater",
          "Reservoir",
          "RiverBodyOfWater",
          "Pond",
          "Continent",
          "Mountain",
          "Volcano",
          "Waterfall"
    ]
    return subClasses

def getProperties():
    properties = {}
    
    properties['typicalAgeRange'] = 'typicalAgeRange'
    properties['gender'] = 'gender'
    
    # Add and merge properties from Place    
    placeProperties = Place.getProperties()
    
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