import service.debug as debug
import entity.Family.Family as Family

def importFamilyEnitity(code):
    if (code == "MeetingRoom"):
        import entity.Family.MeetingRoom as Family
    elif (
        code == "LodgingBusiness" or
        code == "BedAndBreakfast" or
        code == "Campground" or 
        code == "Hostel" or
        code == "Hotel" or
        code == "Motel" or
        code == "Resort" or
        code == "HolidayHouse" or
        code == "HolidayApartment" or
        code == "Agrotourism" or
        code == "CountryInn" or
        code == "FarmLodging" or
        code == "Garni" or
        code == "GroupAccommodation" or
        code == "Guesthouse" or
        code == "IglooVillage" or
        code == "Mountainhut" or
        code == "RescueHut" or
        code == "SelfCateredHut" or
        code == "ManagedHut" or
        code == "Pension" or
        code == "PrivateRoom"
        ):
        import entity.Family.LodgingBusiness as Family
    elif (
        code == "FoodEstablishment" or
        code == "Bakery" or
        code == "BarOrPub" or
        code == "Brewery" or
        code == "CafeOrCoffeeShop" or 
        code == "Distillery" or
        code == "FastFoodRestaurant" or
        code == "IceCreamShop" or 
        code == "Restaurant" or
        code == "Winery"):
        import entity.Family.FoodEstablishment as Family
    elif (code == "TouristAttraction"):
        import entity.Family.TouristAttraction as Family
    elif (code == "CivicStructure"):
        import entity.Family.CivicStructure as Family
    elif (code == "Webcam" or
          code == "LiveVideo" or
          code == "StaticWebcam" or
          code == "WebLink"):
        import entity.Family.Webcam as Family
    elif (code == "Event" or
          code == "BusinessEvent" or
          code == "ChildrensEvent" or
          code == "ComedyEvent" or
          code == "DanceEvent" or
          code == "DeliveryEvent" or
          code == "EducationEvent" or
          code == "ExhibitionEvent" or
          code == "Festival" or
          code == "FoodEvent" or
          code == "Hackathon" or
          code == "LiteraryEvent" or
          code == "MusicEvent" or
          code == "PublicationEvent" or
          code == "SaleEvent" or
          code == "ScreeningEvent" or
          code == "SocialEvent" or
          code == "SportsEvent" or
          code == "TheaterEvent" or
          code == "VisualArtsEvent"):
        import entity.Family.Event as Family
    elif (code == "MediaObejct" or
          code == "AudioObject" or
          code == "VideoObject" or
          code == "ImageObject"):
        print("MediaObject")
        import entity.Family.MediaObject as Family
    elif (code == "Landform" or
          code == "BodyOfWater" or
          code == "LakeBodyOfWater" or
          code == "Reservoir" or
          code == "RiverBodyOfWater" or
          code == "Pond" or
          code == "Continent" or
          code == "Mountain" or
          code == "Volcano" or
          code == "Waterfall"):
        import entity.Family.Landform as Family
    elif (code == "Event" or
          code == "BusinessEvent" or
          code == "ChildrensEvent" or
          code == "ComedyEvent" or
          code == "DanceEvent" or
          code == "DeliveryEvent" or
          code == "EducationEvent" or
          code == "ExhibitionEvent" or
          code == "Festival" or
          code == "FoodEvent" or
          code == "Hackathon" or
          code == "LiteraryEvent" or
          code == "MusicEvent" or
          code == "PublicationEvent" or
          code == "SaleEvent" or
          code == "ScreeningEvent" or
          code == "SocialEvent" or
          code == "SportsEvent" or
          code == "TheaterEvent" or
          code == "VisualArtsEvent"):
        import entity.Family.Schedule as Family
    elif (code == "Schedule"):
        import entity.Family.Schedule as Family
    elif (code == "Product"):
        import entity.Family.Product as Family
    elif (code == "Webcam" or
          code == "LiveVideo" or
          code == "StaticWebcam" or
          code == "WebLink"):
        import entity.Family.Webcam as Family
    elif (code == "Trail"):
        import entity.Family.Trail as Family
    elif (code == "Recommendation"):
        import entity.Family.Recommendation as Family
    elif (code == "Organization"):
        import entity.Family.Organization as Family
    elif (code == "Place"):
        import entity.Family.Place as Family
    else:
        # Default all 
        import entity.Family.Family as Family
    return Family

def patchAkeneoFamily(family, families, target):
    Family = importFamilyEnitity(family["label"])
    print("PATCH Family: ", family["label"])
    body = Family.setBody(family, families)
    response = patchFamily(family["label"], body, target)
    print("FINISH - patch Family: ", family["label"])

def patchFamily(code, body, akeneo):
    clearBody = {
        "code": code,
        "attribute_as_label": body["attribute_as_label"],
        "attribute_as_image": body["attribute_as_image"],
        "attribute_requirements": {
            "ecommerce": [
                "sku",
                "name",
                "image",
            ],
            "mice": [],
            "print": [],
            "intern": []
        },
        "labels": {
            "en_US": body["labels"]["en_US"],
            "de_CH": body["labels"]["de_CH"],
            "fr_FR": body["labels"]["fr_FR"],
            "it_IT": body["labels"]["it_IT"],
        },
        "attributes": [
            "sku",
            "name",
            "image"
        ]
    }
    try:
        # Clear Attributes
        #print("Clear Attributes")
        #response = akeneo.patchFamily(code, clearBody)
        # DEBUG - Write to file
        debug.addToFile(code, body)
        # To Akeneo
        print("Patch family")
        response = akeneo.patchFamily(code, body)
        print("Response: ", response)
        print("Status Code: ", response.status_code)
        debug.addToLogFile(code, response.text)
           
    except Exception as e:
        print("Error: ", e)
        print("patch Family: ", code)
        print("Response: ", response)
        debug.addToLogFile(code, response)
    return response