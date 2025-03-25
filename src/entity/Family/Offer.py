import service.debug as debug

def setBody(family, families):
    code = family["label"]
    
    attribute_requirements = {
        "sku": "sku", 
        "name": "name", 
        "image": "image", 
        "license": "license",
        "validThrough": "validThrough",
        "validFrom": "validFrom",
        }
    
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
    body['attributes']['priceValidFrom '] = 'priceValidFrom'
    
    body['attributes']['validThrough'] = 'validThrough'
    body['attributes']['validFrom'] = 'validFrom'
    
    body['attributes']['leisure'] = 'leisure'
    
    body['attributes']['offers'] = 'offers'
    
    # Befor Release 3.5.0
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
    
    body['attributes']['metaTitle'] = 'metaTitle'
    body['attributes']['metaDescription'] = 'metaDescription'
    body['attributes']['canonicalUrl'] = 'canonicalUrl'
    
    # only now demo and vgl
    #body['attributes']['avs_id'] = 'avs_id'
    
    return body