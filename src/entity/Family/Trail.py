import service.debug as debug

def setBody(family, families):
    code = family["label"]

    if family["attribute_requirements.ecommerce"] != None:
        attribute_requirements = {attrRequ: attrRequ for attrRequ in family["attribute_requirements.ecommerce"].split(",")}
    else:
        attribute_requirements = {"sku": "sku", "name": "name", "image": "image", "license": "license"}
        
    attributes = {}
    attributes['sku'] = 'sku'
    attributes['name'] = 'name'
    attributes['image'] = 'image'
    
    attributes['disambiguatingDescription'] = 'disambiguatingDescription'
    attributes['description'] = 'description'

    attributes['openstreetmap_id'] = 'openstreetmap_id'
    attributes['license'] = 'license'
    attributes['copyrightHolder'] = 'copyrightHolder'
    attributes['author'] = 'author'
    
    attributes['leisure'] = 'leisure'
    
    attributes['potentialAction'] = 'potentialAction'
    attributes['target'] = 'target'

    if 'image' in attributes:
        attributes['image_description'] = 'image_description'
    
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

    body["attributes"] = attributes

    return body