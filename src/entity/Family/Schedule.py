import entity.Family.Family as Family

def setBody(family, families):
    
    attribute_requirements = {
                                "sku": "sku", 
                                "name": "name", 
                                "license": "license"
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
    
    body['attributes']['license'] = 'license'
    body['attributes']['copyrightHolder'] = 'copyrightHolder'
    body['attributes']['author'] = 'author'
    
    # Specific Schedule Attributes
    body['attributes']['byDay'] = 'byDay'
    body['attributes']['byMonth'] = 'byMonth'
    #body['attributes']['byMonthDay'] = 'byMonthDay'
    #body['attributes']['byMonthDay'] = 'byMonthDay'
    
    body['attributes']['duration'] = 'duration'
    body['attributes']['endDate'] = 'endDate'
    body['attributes']['endTime'] = 'endTime'
    body['attributes']['startDate'] = 'startDate'
    body['attributes']['startTime'] = 'startTime'
    
    body['attributes']['url'] = 'url'
    
    return body