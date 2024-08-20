import service.debug as debug

def setBody(family, families):
    code = family["label"]
    
    attributes = {}
    attributes['sku'] = 'sku'
    attributes['name'] = 'name'
    attributes['description'] = 'description'
    attributes['disambiguatingDescription'] = 'disambiguatingDescription'
    attributes['image'] = 'image'
    attributes['image_description'] = 'image_description'
    attributes['license'] = 'license'
    attributes['author'] = 'author'
    attributes['copyrightHolder'] = 'copyrightHolder'
    
    attributes['isAccessibleForFree'] = 'isAccessibleForFree'
    attributes['inLanguage'] = 'inLanguage'
    attributes['url'] = 'url'
    attributes['potentialAction'] = 'potentialAction'
    attributes['target'] = 'target'
    attributes['leisure'] = 'leisure'
    attributes['channel'] = 'channel'
    
    attribute_requirements = {"sku": "sku", "name": "name", "image": "image", "license": "license"}
    
    body = {
        "code": code,
        "attribute_as_label": 'name',
        "attribute_as_image": 'image',
        "attribute_requirements": {
            "ecommerce": attribute_requirements,
        },
        "labels": {
            "en_US": family["label.en_US"],
            "de_CH": family["label.de_CH"],
            "fr_FR": family["label.fr_FR"],
            "it_IT": family["label.it_IT"],
        }
    }

    # Remove Properties
    #print("Remove Attributes: ")
    ##print(code)
    #attributes = removeProperties(code, attributes)

    body["attributes"] = attributes
    
    return body