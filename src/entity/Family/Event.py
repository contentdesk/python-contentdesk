import entity.Family.Family as Family

def setBody(family, families):
    body = Family.setBody(family, families)
    
    body['attributes']['latitude'] = 'latitude'
    body['attributes']['longitude'] = 'longitude'
    
    body['attributes']['streetAddress'] = 'streetAddress'
    body['attributes']['postalCode'] = 'postalCode'
    body['attributes']['addressLocality'] = 'addressLocality'
    body['attributes']['addressCountry'] = 'addressCountry'
    body['attributes']['addressRegion'] = 'addressRegion'
    body['attributes']['tourismregion'] = 'tourismregion'
    
    body['attributes']['startTime'] = 'startTime'
    body['attributes']['endTime'] = 'endTime'
    
    body['attributes']['logo'] = 'logo'
    
    body['attributes']['metaTitle'] = 'metaTitle'
    body['attributes']['metaDescription'] = 'metaDescription'
    body['attributes']['canonicalUrl'] = 'canonicalUrl'
    
    
    return body