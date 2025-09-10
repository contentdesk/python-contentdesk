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
    # https://docs.discover.swiss/dev/reference/dataschema/definition/infocenter-classes/Event/
    
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
    
    body['attributes']['duration'] = 'duration'
    body['attributes']['price'] = 'price'
    #body['attributes']['offer'] = 'offer'
    
    body['attributes']['guidle_event_id'] = 'guidle_event_id'
    body['attributes']['eventfrog_id'] = 'eventfrog_id'
    
    return body