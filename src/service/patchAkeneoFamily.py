import service.debug as debug
import entity.Family.Family as Family

def importFamilyEnitity(code):
    if (code == "MeetingRoom"):
        print("Load MeetingRoom")
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
        code == "PrivateRoom" or
        code == "Pitch"
        ):
        print("Load LodgingBusiness")
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
        print("Load FoodEstablishment")
        import entity.Family.FoodEstablishment as Family
    elif (code == "TouristAttraction"):
        print("Load TouristAttraction")
        import entity.Family.TouristAttraction as Family
    elif (code == "CivicStructure"):
        print("Load CivicStructure")
        import entity.Family.CivicStructure as Family
    elif (code == "Webcam" or
          code == "LiveVideo" or
          code == "StaticWebcam" or
          code == "WebLink"):
        print("Load Webcam")
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
        print("Load Event")
        import entity.Family.Event as Family
    elif (code == "MediaObejct" or
          code == "AudioObject" or
          code == "VideoObject" or
          code == "ImageObject"):
        print("Load MediaObject")
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
        print("Load Landform")
        import entity.Family.Landform as Family
    elif (code == "Schedule"):
        print("Load Schedule")
        import entity.Family.Schedule as Family
    elif (
            code == "Product" or
            code == "Adventure" or
            code == "ApartmentOffer" or
            code == "Beverage" or
            code == "CampingPitchOffer" or
            code == "CityTour" or
            code == "Course" or
            code == "CrossCountryTicket" or
            code == "Donation" or
            code == "EventTicket" or
            code == "Experience" or
            code == "Fashion" or
            code == "Accessoires" or
            code == "Clothing" or
            code == "Food" or
            code == "GuestCard" or
            code == "IndividualProduct" or
            code == "Membership" or
            code == "Merchandise" or
            code == "NonFood" or
            code == "Offer" or
            code == "Package" or
            code == "ProductCollection" or
            code == "ProductGroup" or
            code == "Rental" or
            code == "RoomOffer" or
            code == "DormitoryOffer" or
            code == "HotelRoomOffer" or
            code == "DoubleRoomOffer" or
            code == "FamilyRoomOffer" or
            code == "SingleRoomOffer" or
            code == "MeetingRoomOffer" or
            code == "StayHelper" or
            code == "Services" or
            code == "SkiTicket" or
            code == "SomeProducts" or
            code == "Sportsgood" or
            code == "SuiteOffer" or
            code == "TableReservation" or
            code == "Ticket" or
            code == "Transport" or
            code == "Vouchers" or
            code == "Wellness"
          ):
        print("Load Product")
        import entity.Family.Product as Family
    elif (code == "Offer"):
        print("Load Offer")
        import entity.Family.Offer as Family
    elif (code == "GuestCard"):
        print("Load GuestCard")
        import entity.Family.GuestCard as Family
    elif (code == "Trail"):
        print("Load Trail")
        import entity.Family.Trail as Family
    elif (code == "Recommendation"):
        print("Load Recommendation")
        import entity.Family.Recommendation as Family
    elif (code == "Organization"):
        print("Load Organization")
        import entity.Family.Organization as Family
    elif (code == "LocalBusiness" or
          code == "AnimalShelter" or
          code == "ArchiveOrganization" or
          code == "AutomotiveBusiness" or
          code == "ChildCare" or
          code == "Dentist" or
          code == "DryCleaningOrLaundry" or
          code == "EmergencyService" or
          code == "EmploymentAgency" or
          code == "EntertainmentBusiness" or
          code == "FinancialService" or
          code == "FoodEstablishment" or
          code == "GovernmentOffice" or
          code == "HealthAndBeautyBusiness" or
          code == "HomeAndConstructionBusiness" or
          code == "InternetCafe" or
          code == "LegalService" or
          code == "Library" or
          code == "MedicalBusiness" or
          code == "ProfessionalService" or
          code == "RadioStation" or
          code == "RealEstateAgent" or
          code == "RecyclingCenter" or
          code == "SelfStorage" or
          code == "ShoppingCenter" or
          code == "SportsActivityLocation" or
          code == "Store" or
          code == "TelevisionStation" or
          code == "TouristInformationCenter" or
          code == "TravelAgency"):
        print("Load LocalBusiness")
        import entity.Family.Place as Family
    elif (code == "Place"):
        print("Load Place")
        import entity.Family.Place as Family
    elif (code == "Tour" or
          code == "Longdistance" or
          code == "Route" or
          code == "GlacierTour" or
          code == "HighTour" or
          code == "MotorisedTours" or
          code == "BusTour" or
          code == "CarTour" or
          code == "MotorTour" or
          code == "QuadTour" or
          code == "SegwayTour" or
          code == "ShipTour" or
          code == "TrainTour" or
          code == "ThemeTrail" or
          code == "ViaFerrata" or
          code == "Way" or
          code == "BikeTrail" or
          code == "CrossCountry" or
          code == "HikingTrail" or
          code == "NatureTrail" or
          code == "SkiRoute" or
          code == "SkiSlope" or
          code == "SnowshoeTrail" or
          code == "TobogganRun" or
          code == "WinterHiking"):
        print("Load Tour")
        import entity.Family.Tour as Family
    else:
        # Default all 
        print("Load Family")
        import entity.Family.Family as Family
    return Family

def patchAkeneoFamily(family, families, target):
    Family = importFamilyEnitity(family["label"])
    print("PATCH Family: ", family["label"])
    print("- Parent Family: ", family["parent"])
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
        print("- Patch family")
        response = akeneo.patchFamily(code, body)
        print("- Response: ", response)
        print("- Status Code: ", response.status_code)
        debug.addToLogFile(code, response.text)
           
    except Exception as e:
        print("Error: ", e)
        print("patch Family: ", code)
        print("Response: ", response)
        debug.addToLogFile(code, response)
    return response