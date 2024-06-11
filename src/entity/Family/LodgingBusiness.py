import entity.Family.Family as Family

def setBody(family, families):
    body = Family.setBody(family, families)

    if 'dayTime' in body['attributes']:
        print("Remove DayTime: ")
        body['attributes'].pop('dayTime')
        body['attributes'].remove('dayTime')
    
    if 'duration' in body['attributes']:
        body['attributes'].pop('duration')

    
    print("LodgingBusiness Body: ", body)

    return body