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
    
    body['attributes']['image_01_scope'] = 'image_01_scope'
    body['attributes']['image_02_scope'] = 'image_02_scope'
    body['attributes']['image_03_scope'] = 'image_03_scope'
    body['attributes']['image_04_scope'] = 'image_04_scope'
    body['attributes']['image_05_scope'] = 'image_05_scope'
    body['attributes']['image_06_scope'] = 'image_06_scope'
    body['attributes']['image_07_scope'] = 'image_07_scope'
    body['attributes']['image_08_scope'] = 'image_08_scope'
    body['attributes']['image_09_scope'] = 'image_09_scope'
    body['attributes']['image_10_scope'] = 'image_10_scope'
    
    body['attributes']['image_01_scope_description'] = 'image_01_scope_description'
    body['attributes']['image_02_scope_description'] = 'image_02_scope_description'
    body['attributes']['image_03_scope_description'] = 'image_03_scope_description'
    body['attributes']['image_04_scope_description'] = 'image_04_scope_description'
    body['attributes']['image_05_scope_description'] = 'image_05_scope_description'
    body['attributes']['image_06_scope_description'] = 'image_06_scope_description'
    body['attributes']['image_07_scope_description'] = 'image_07_scope_description'
    body['attributes']['image_08_scope_description'] = 'image_08_scope_description'
    body['attributes']['image_09_scope_description'] = 'image_09_scope_description'
    body['attributes']['image_10_scope_description'] = 'image_10_scope_description'
    
    body['attributes']['metaTitle'] = 'metaTitle'
    body['attributes']['metaDescription'] = 'metaDescription'
    body['attributes']['canonicalUrl'] = 'canonicalUrl'
    
    body['attributes']['isAccessibleForFree'] = 'isAccessibleForFree'
    
    body['attributes']['duration'] = 'duration'
    body['attributes']['price'] = 'price'
    #body['attributes']['offer'] = 'offer'
    
    body['attributes']['guidle_event_id'] = 'guidle_event_id'
    body['attributes']['guidle_webcode'] = 'guidle_webcode'
    body['attributes']['eventfrog_id'] = 'eventfrog_id'
    
    return body