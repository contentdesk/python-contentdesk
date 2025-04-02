import entity.Family.Family as Family

def getSubClasses():
    subClasses = [
          "Event",
          "BusinessEvent",
          "ChildrensEvent",
          "ComedyEvent",
          "DanceEvent",
          "DeliveryEvent",
          "EducationEvent",
          "ExhibitionEvent",
          "Festival",
          "FoodEvent",
          "Hackathon",
          "LiteraryEvent",
          "MusicEvent",
          "PublicationEvent",
          "SaleEvent",
          "ScreeningEvent",
          "SocialEvent",
          "SportsEvent",
          "TheaterEvent",
          "VisualArtsEvent"
    ]
    return subClasses

def setBody(family, families):
    body = Family.setBody(family, families)
    
    body['attributes']['latitude'] = 'latitude'
    body['attributes']['longitude'] = 'longitude'
    
    body['attributes']['location'] = 'location'
    body['attributes']['streetAddress'] = 'streetAddress'
    body['attributes']['postalCode'] = 'postalCode'
    body['attributes']['addressLocality'] = 'addressLocality'
    body['attributes']['addressCountry'] = 'addressCountry'
    body['attributes']['addressRegion'] = 'addressRegion'
    
    body['attributes']['startTime'] = 'startTime'
    body['attributes']['endTime'] = 'endTime'
    
    body['attributes']['logo'] = 'logo'
    
    body['attributes']['metaTitle'] = 'metaTitle'
    body['attributes']['metaDescription'] = 'metaDescription'
    body['attributes']['canonicalUrl'] = 'canonicalUrl'
    
    body['attributes']['isAccessibleForFree'] = 'isAccessibleForFree'
    
    return body