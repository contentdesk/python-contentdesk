import entity.Family as Family

def setBody(family, families):
    body = Family.setBody(family, families)

    if 'dayTime' in body['attributes']:
        body['attributes'].pop('dayTime')
    
    if 'duration' in body['attributes']:
        body['attributes'].pop('duration')

    return body