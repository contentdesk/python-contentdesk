import service.debug as debug

def setBody(family, families):
    code = family["label"]

    if family["attribute_requirements.ecommerce"] != None:
        attribute_requirements = {attrRequ: attrRequ for attrRequ in family["attribute_requirements.ecommerce"].split(",")}
    else:
        attribute_requirements = {"sku": "sku", "name": "name", "image": "image", "license": "license"}

    #attribute_requirements = getParentAttributesRequirements(family, families, attribute_requirements)

    #if family["attributes"] != None:
    #    attributes = {attr: attr for attr in family["attributes"].split(",")}
    #else:
    #    attributes = {"sku": "sku", "name": "name", "image": "image"}

    attributes = {}
    attributes['sku'] = 'sku'
    attributes['name'] = 'name'
    attributes['image'] = 'image'

    attributes['seating_banquet'] = 'seating_banquet'
    attributes['seating_bar_table'] = 'seating_bar_table'
    attributes['seating_block'] = 'seating_block'
    attributes['seating_boardroom'] = 'seating_boardroom'
    attributes['seating_concert'] = 'seating_concert'
    attributes['seating_seminar'] = 'seating_seminar'
    attributes['seating_ushape'] = 'seating_ushape'

    attributes['openstreetmap_id'] = 'openstreetmap_id'
    attributes['license'] = 'license'
    attributes['copyrightHolder'] = 'copyrightHolder'
    attributes['author'] = 'author'

    attributes['amenityFeature'] = 'amenityFeature'
    attributes['occupancy'] = 'occupancy'
    attributes['floorLevel'] = 'floorLevel'
    attributes['floorSize'] = 'floorSize'
    attributes['maximumAttendeeCapacity'] = 'maximumAttendeeCapacity'
    attributes['yearBuilt'] = 'yearBuilt'
    attributes['offers'] = 'offers'
    attributes['priceRange'] = 'priceRange'

    attributes['latitude'] = 'latitude'
    attributes['longitude'] = 'longitude'

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

    # Remove Properties
    #print("Remove Attributes: ")
    ##print(code)
    #attributes = removeProperties(code, attributes)

    body["attributes"] = attributes

    clearBody = {
        "code": code,
        "attribute_as_label": family["attribute_as_label"],
        "attribute_as_image": family["attribute_as_image"],
        "attribute_requirements": {
            "ecommerce": [
                "sku",
                "name",
                "image"
            ],
        },
        "labels": {
            "en_US": family["label.en_US"],
            "de_CH": family["label.de_CH"],
            "fr_FR": family["label.fr_FR"],
            "it_IT": family["label.it_IT"],
        },
        "attributes": [
            "sku",
            "name",
            "image"
        ]
    }

    return body