import service.debug as debug
import entity.Family.Family as Family

def setBody(family, families):
    body = Family.setBody(family, families)

    if 'starRating' in body['attributes']:
        body['attributes'].pop('starRating')
        if 'starRating' in body['attributes']:
            del body['attributes']['starRating']
    
    return body


