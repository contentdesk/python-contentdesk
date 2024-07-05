import entity.Family.Family as Family

def setBody(family, families):
    #body = Family.setBody(family, families)
    
    body = {}
    
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

    return body