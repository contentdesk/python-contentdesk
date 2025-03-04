import service.debug as debug

def getSubClasses():
    subClasses = [
        "Product",
        "Adventure",
        "ApartmentOffer",
        "Beverage",
        "CampingPitchOffer",
        "CityTour",
        "Course",
        "CrossCountryTicket",
        "Donation",
        "EventTicket",
        "Experience",
        "Fashion",
        "Accessoires",
        "Clothing",
        "Food",
        "GuestCard",
        "IndividualProduct",
        "Membership",
        "Merchandise",
        "NonFood",
        # "Offer",
        "Package",
        "ProductCollection",
        "ProductGroup",
        "Rental",
        "RoomOffer",
        "DormitoryOffer",
        "HotelRoomOffer",
        "DoubleRoomOffer",
        "FamilyRoomOffer",
        "SingleRoomOffer",
        "MeetingRoomOffer",
        "StayHelper",
        "Services",
        "SkiTicket",
        "SomeProducts",
        "Sportsgood",
        "SuiteOffer",
        "TableReservation",
        "Ticket",
        "Transport",
        "Vouchers",
        "Wellness"
    ]
    return subClasses

def setBody(family, families):
    code = family["label"]
    
    attribute_requirements = {
        "sku": "sku", 
        "name": "name", 
        "image": "image", 
        "license": "license"
        }
    
    attributes = {}
    
    attributes['disambiguatingDescription'] = 'disambiguatingDescription'
    attributes['description'] = 'description'
    
    body = {}
    body["code"] = code
    body["attribute_as_image"] = "image"
    body["attribute_as_label"] = "name"
    body["attribute_requirements"] = {}
    body["attribute_requirements"]['ecommerce'] = attribute_requirements
    body["labels"] = {
        "en_US": family["label.en_US"],
        "de_CH": family["label.de_CH"],
        "fr_FR": family["label.fr_FR"],
        "it_IT": family["label.it_IT"],
    }
    body["attributes"] = attributes
    
    body["attributes"]['sku'] = 'sku'
    body["attributes"]['name'] = 'name'
    body["attributes"]['disambiguatingDescription'] = 'disambiguatingDescription'
    body["attributes"]['description'] = 'description'
    body["attributes"]['image'] = 'image'
    body["attributes"]['image_description'] = 'image_description'
    
    body['attributes']['license'] = 'license'
    body['attributes']['copyrightHolder'] = 'copyrightHolder'
    body['attributes']['author'] = 'author'
    
    body['attributes']['potentialAction'] = 'potentialAction'
    body['attributes']['target'] = 'target'
    
    if code == "Product":
        body['attributes']['size'] = 'size'
        body['attributes']['color'] = 'color'
        body['attributes']['gender'] = 'gender'
        body['attributes']['weight'] = 'weight'
        body['attributes']['width'] = 'width'
        body['attributes']['height'] = 'height'
    
    #body['attributes']['availability'] = 'availability'
    
    body['attributes']['offers'] = 'offers'
    body['attributes']['price'] = 'price'
    body['attributes']['priceValidUntil '] = 'priceValidUntil'
    
    body['attributes']['validThrough'] = 'validThrough'
    body['attributes']['validFrom'] = 'validFrom'
    
    body['attributes']['leisure'] = 'leisure'
    
    # seo attributes
    attributes['metaTitle'] = 'metaTitle'
    attributes['metaDescription'] = 'metaDescription'
    attributes['canonicalUrl'] = 'canonicalUrl'

    
    # duration
    if (
        code == "Adventure" or 
        code == "CityTour" or
        code == "Course" or
        code == "Experience"
        ):
        body['attributes']['duration'] = 'duration'

        body['attributes']['longitude'] = 'longitude'
        body['attributes']['latitude'] = 'latitude'

        body['attributes']['streetAddress'] = 'streetAddress'
        body['attributes']['postalCode'] = 'postalCode'
        body['attributes']['addressLocality'] = 'addressLocality'
        body['attributes']['addressCountry'] = 'addressCountry'
        body['attributes']['addressRegion'] = 'addressRegion'
        # Contact
        body['attributes']['legalName'] = 'legalName'
        body['attributes']['department'] = 'department'
        body['attributes']['honorificPrefix'] = 'honorificPrefix'
        body['attributes']['givenName'] = 'givenName'
        body['attributes']['familyName'] = 'familyName'
        body['attributes']['email'] = 'email'
        body['attributes']['telephone'] = 'telephone'
        body['attributes']['url'] = 'url'
        
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
    
        debug.addToLogFileBody(str(family['label']), body)
    
    return body