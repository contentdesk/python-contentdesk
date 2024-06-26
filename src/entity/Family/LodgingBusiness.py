import entity.Family.Family as Family

def setBody(family, families):
    body = Family.setBody(family, families)

    if 'daytime' in body['attributes']:
        body['attributes'].pop('daytime', None)
        if 'daytime' in body['attributes']:
            del body['attributes']['daytime']
    
    if 'duration' in body['attributes']:
        body['attributes'].pop('duration', None)
        if 'duration' in body['attributes']:
            del body['attributes']['duration']

    attributes = body["attributes"]

    #attributes['license']
    #attributes['copyrightHolder']
    #attributes['author']

    body["attributes"] = attributes

    return body