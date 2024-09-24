import service.debug as debug

def setBody(family, families):
    code = family["label"]
    
    attribute_requirements = {"sku": "sku", "name": "name", "image": "image", "license": "license"}
    
    attributes = {}
    
    attributes['disambiguatingDescription'] = 'disambiguatingDescription'
    attributes['description'] = 'description'
    attributes['channel'] = 'channel'
    
    body = {}
    body["code"] = code
    body["attribute_as_image"] = "image"
    body["attribute_as_label"] = "name"
    body["attribute_requirements"] = {}
    body["attribute_requirements"]['ecommerce'] = attribute_requirements
    body["labels"] = {
        "en_US": family["label.en_US"],
        "de_CH": family["label.de_CH"],
        "fr_FR": family["label.fr_FR"],
        "it_IT": family["label.it_IT"],
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
    
    body['attributes']['availability'] = 'availability'
    
    body['attributes']['price'] = 'price'
    body['attributes']['priceValidUntil '] = 'priceValidUntil'
    
    body['attributes']['validThrough'] = 'validThrough'
    body['attributes']['validFrom'] = 'validFrom'
    body['attributes']['channel'] = 'channel'
    
    # Remove after Release Contentdesk 3.5.0
    #body['attributes']['avs_id'] = 'avs_id' # only now demo and vgl
    
    return body