import entity.Family.Family as Family

def setBody(family, families):
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
    body['attributes']['sku'] = 'sku'
    body['attributes']['name'] = 'name'
    body['attributes']['disambiguatingDescription'] = 'disambiguatingDescription'
    body['attributes']['description'] = 'description'
    body['attributes']['image'] = 'image'
    body['attributes']['image_description'] = 'image_description'

    body['attributes']['latitude'] = 'latitude'
    body['attributes']['longitude'] = 'longitude'
    
    body['attributes']['contentUrl'] = 'contentUrl'
    body['attributes']['embedUrl'] = 'embedUrl'
    body['attributes']['thumbnailUrl'] = 'thumbnailUrl'
    
    body['attributes']['openstreetmap_id'] = 'openstreetmap_id'
    body['attributes']['license'] = 'license'
    body['attributes']['copyrightHolder'] = 'copyrightHolder'
    body['attributes']['author'] = 'author'
    
    body['attributes']['leisure'] = 'leisure'
    
    body['attributes']['potentialAction'] = 'potentialAction'
    body['attributes']['target'] = 'target'
    
    body['attributes']['markerIcon'] = 'markerIcon'

    return body