# TODO:
# Not Used!!

def getSettings():
    label = "QuestionAnswer"

def getProperties():
    properties = {}
    
    properties['sku'] = 'sku'
    properties['name'] = 'name'
    properties['text'] = 'text'
    
    properties['potentialAction'] = 'potentialAction'
    properties['target'] = 'target'
    
    return properties

def setBody(family, families):
    code = family["label"]

    if family["attribute_requirements.ecommerce"] != None:
        attribute_requirements = {"sku": "sku", "name": "name"}
    else:
        attribute_requirements = {"sku": "sku", "name": "name"}
    
    # Create body
    body = {
        "code": code,
        "attribute_as_label": family["attribute_as_label"],
        "attribute_as_image": None,
        "attribute_requirements": {
            "ecommerce": attribute_requirements,
            "mice": attribute_requirements,
        },
        "labels": {
            "en_US": family["label.en_US"],
            "de_CH": family["label.de_CH"],
            "fr_FR": family["label.fr_FR"],
            "it_IT": family["label.it_IT"],
        }
    }
    
    body['attributes'] = getProperties()
    
    return body