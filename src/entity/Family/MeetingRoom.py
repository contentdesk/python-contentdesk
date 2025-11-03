import service.debug as debug

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

    # MeetingRoom specific properties
    properties['seating_banquet'] = 'seating_banquet'
    properties['seating_bar_table'] = 'seating_bar_table'
    properties['seating_block'] = 'seating_block'
    properties['seating_boardroom'] = 'seating_boardroom'
    properties['seating_concert'] = 'seating_concert'
    properties['seating_seminar'] = 'seating_seminar'
    properties['seating_ushape'] = 'seating_ushape'

    properties['openstreetmap_id'] = 'openstreetmap_id'
    properties['license'] = 'license'
    properties['copyrightHolder'] = 'copyrightHolder'
    properties['author'] = 'author'

    properties['amenityFeature'] = 'amenityFeature'
    properties['occupancy'] = 'occupancy'
    properties['floorLevel'] = 'floorLevel'
    properties['floorSize'] = 'floorSize'
    properties['maximumAttendeeCapacity'] = 'maximumAttendeeCapacity'
    properties['yearBuilt'] = 'yearBuilt'
    properties['offers'] = 'offers'
    properties['priceRange'] = 'priceRange'

    properties['latitude'] = 'latitude'
    properties['longitude'] = 'longitude'

    properties['leisure'] = 'leisure'

    if 'image' in properties:
        properties['image_description'] = 'image_description'
        
    properties['image_01_scope'] = 'image_01_scope'
    properties['image_02_scope'] = 'image_02_scope'
    properties['image_03_scope'] = 'image_03_scope'
    properties['image_04_scope'] = 'image_04_scope'
    properties['image_05_scope'] = 'image_05_scope'
    properties['image_06_scope'] = 'image_06_scope'
    properties['image_07_scope'] = 'image_07_scope'
    properties['image_08_scope'] = 'image_08_scope'
    properties['image_09_scope'] = 'image_09_scope'
    properties['image_10_scope'] = 'image_10_scope'

    properties['image_01_scope_description'] = 'image_01_scope_description'
    properties['image_02_scope_description'] = 'image_02_scope_description'
    properties['image_03_scope_description'] = 'image_03_scope_description'
    properties['image_04_scope_description'] = 'image_04_scope_description'
    properties['image_05_scope_description'] = 'image_05_scope_description'
    properties['image_06_scope_description'] = 'image_06_scope_description'
    properties['image_07_scope_description'] = 'image_07_scope_description'
    properties['image_08_scope_description'] = 'image_08_scope_description'
    properties['image_09_scope_description'] = 'image_09_scope_description'
    properties['image_10_scope_description'] = 'image_10_scope_description'
    
    return properties

def setBody(family, families):
    code = family["label"]

    if family["attribute_requirements.ecommerce"] != None:
        attribute_requirements = {"sku": "sku", "name": "name", "license": "license"}
    else:
        attribute_requirements = {"sku": "sku", "name": "name", "license": "license"}

    #attribute_requirements = getParentAttributesRequirements(family, families, attribute_requirements)

    #if family["attributes"] != None:
    #    attributes = {attr: attr for attr in family["attributes"].split(",")}
    #else:
    #    attributes = {"sku": "sku", "name": "name", "image": "image"}

    attributes = getProperties()
    
    body = {
        "code": code,
        "attribute_as_label": 'name',
        "attribute_as_image": 'image',
        "attribute_requirements": {
            "ecommerce": attribute_requirements,
            "mice": attribute_requirements
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
            "mice": [
                "sku",
                "name",
                "image"
            ]
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