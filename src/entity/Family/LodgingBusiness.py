import entity.Family.Family as Family

def setBody(family, families):
    body = Family.setBody(family, families)
    print("Family Body: ", body)

    attributes = body['attributes']

    if 'daytime' in attributes:
        print("Remove DayTime: ")
        attributes.pop('daytime', None)
        if 'daytime' in attributes:
            del attributes['daytime']
    
    if 'duration' in attributes:
        attributes.pop('duration', None)
        if 'duration' in attributes:
            del attributes['duration']

    body['attributes'] = attributes
    
    print("LodgingBusiness Body: ", body)

    return body