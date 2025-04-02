import entity.Family.Family as Family

def getProperties():
    properties = {}
    
    properties['sku'] = 'sku'
    properties['name'] = 'name'
    properties['disambiguatingDescription'] = 'disambiguatingDescription'
    properties['description'] = 'description'
    properties['image'] = 'image'
    properties['image_description'] = 'image_description'

    properties['latitude'] = 'latitude'
    properties['longitude'] = 'longitude'
    
    properties['contentUrl'] = 'contentUrl'
    properties['embedUrl'] = 'embedUrl'
    properties['thumbnailUrl'] = 'thumbnailUrl'
    
    properties['openstreetmap_id'] = 'openstreetmap_id'
    properties['license'] = 'license'
    properties['copyrightHolder'] = 'copyrightHolder'
    properties['author'] = 'author'
    
    properties['leisure'] = 'leisure'
    
    properties['potentialAction'] = 'potentialAction'
    properties['target'] = 'target'
    properties['search_text_pro_channel'] = 'search_text_pro_channel'
    properties['promo_sort_order_scope'] = 'promo_sort_order_scope'
    
    properties['markerIcon'] = 'markerIcon'
    
    return properties

def setBody(family, families, target):
    #body = Family.setBody(family, families)
    
    attribute_requirements = {
                                "sku": "sku", 
                                "name": "name",
                                "image": "image",
                                "license": "license", 
                                "embedUrl": "embedUrl",
                                "latitude": "latitude",
                                "longitude": "longitude",
                                "openstreetmap_id": "openstreetmap_id",
                              }
    
    body = {}
    body['code'] = family['label']
    body['attribute_as_label'] = 'name'
    body['attribute_as_image'] = 'image'
    body["attribute_requirements"] = {}
    body["attribute_requirements"]['ecommerce'] = attribute_requirements
    body["labels"] = {
        "en_US": family["label"],
        "de_CH": family["label"],
        "fr_FR": family["label"],
        "it_IT": family["label"]
    }
    
    body['attributes'] = {}
     
    # Add and merge properties from getProperties    
    body["attributes"] = getProperties()

    return body