import service.debug as debug

def setBody(family, families):
    code = family["label"]
    
    attribute_requirements = {"sku": "sku", "name": "name", "image": "image", "license": "license"}
    
    attributes = {}
    
    attributes['disambiguatingDescription'] = 'disambiguatingDescription'
    attributes['description'] = 'description'
    
    body = {}
    body["code"] = code
    body["attribute_as_image"] = "image"
    body["attribute_as_label"] = "name"
    body["attribute_requirements"] = {}
    body["attribute_requirements"]['ecommerce'] = attribute_requirements
    body["labels"] = {
        "en_US": family["label"],
        "de_CH": family["label"],
        "fr_FR": family["label"],
        "it_IT": family["label"]
    }
    body["attributes"] = attributes
    
    body["attributes"]['sku'] = 'sku'
    body["attributes"]['name'] = 'name'
    body["attributes"]['disambiguatingDescription'] = 'disambiguatingDescription'
    body["attributes"]['description'] = 'description'
    body["attributes"]['image'] = 'image'
    body["attributes"]['image_description'] = 'image_description'
    
    body['attributes']['license'] = 'license'
    body['attributes']['copyrightHolder'] = 'copyrightHolder'
    body['attributes']['author'] = 'author'
    
    body['attributes']['potentialAction'] = 'potentialAction'
    body['attributes']['target'] = 'target'
    
    body['attributes']['size'] = 'size'
    body['attributes']['color'] = 'color'
    body['attributes']['gender'] = 'gender'
    body['attributes']['weight'] = 'weight'
    #body['attributes']['duration'] = 'duration' # only ziggy
    
    return body