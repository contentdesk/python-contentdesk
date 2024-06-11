import entity.Family.Family as Family

def setBody(family, families):
    body = Family.setBody(family, families)

    if 'dayTime' in body['attributes']:
        print("DayTime: ", body['attributes']['dayTime'])
        body['attributes'].pop('dayTime')
    
    if 'duration' in body['attributes']:
        body['attributes'].pop('duration')

    print("LodgingBusiness Body: ", body)

    return body