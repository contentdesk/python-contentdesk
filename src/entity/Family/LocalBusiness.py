import entity.Family.Family as Family
import entity.Family.Place as Place
import service.debug as debug

def getSubClasses():
    subClasses = [
        "LocalBusiness",
        "AnimalShelter",
        "AutomotiveBusiness",
        "AutoDealer",
        "AutoRental",
        "AutoRepair",
        "GasStation",
        "MotorcycleDealer",
        "MotorcycleRepair",
        "BikeSchool",
        "ChildCare",
        "Circus",
        "Corporation",
        "HotelGroup",
        "CourseOrganizer",
        "DryCleaningOrLaundry",
        "EChargingStation",
        "EBikeChargingStation",
        "ECarChargingStation",
        "EmergencyService",
        "EmploymentAgency",
        "EntertainmentBusiness",
        "AdultEntertainment",
        "AmusementPark",
        "ArtGallery",
        "Casino",
        "Cinema",
        "ComedyClub",
        "DancePlace",
        "EscapeRoom",
        "NightClub",
        "FinancialService",
        "GovernmentOffice",
        "PostOffice",
        "HealthAndBeautyBusiness",
        "DaySpa",
        "HairSalon",
        "HealthClub",
        "NailSalon",
        "Solarium",
        "HomeAndConstructionBusiness",
        "LegalService",
        "Library",
        "MedicalBusiness",
        "Dentist",
        "Doctor",
        "MedicalClinic",
        "Pharmacy",
        "MountainSchool",
        "ProfessionalService",
        "Railway",
        "RetirementAndNursingHome",
        "Sauna",
        "ShoppingCenter",
        "SkiSchool",
        "SportsActivityLocation",
        "AdventurePoolOrAquaPark",
        "BikePark",
        "Billard",
        "BMXFacility",
        "BocciaField",
        "BowlingAlley",
        "BungeejumpingPlace",
        "ClimbingGarden",
        "ClimbingHall",
        "CrosscountryCenter",
        "ExerciseGym",
        "FitnessParkour",
        "FlightSchool",
        "GoKartTrack",
        "GolfCourse",
        "HighRopesCourse",
        "IceField",
        "MinigolfCourse",
        "ParaglidingSite",
        "PublicSwimmingPool",
        "IndoorPool",
        "OutdoorPool",
        "PumpTrack",
        "Ropepark",
        "SkatingRink",
        "SkiJumpPlace",
        "SnowPark",
        "SportHall",
        "SportsClub",
        "StadiumOrArena",
        "SummerTobogganTrack",
        "TennisComplex",
        "VolleyballPlace",
        "WinterTobogganTrack",
        "YachtClub",
        "Store",
        "AutoPartsStore",
        "BikeRental",
        "BikeService",
        "BikeStore",
        "BookStore",
        "ButcherShop",
        "ClothingStore",
        "ComputerStore",
        "ConvenienceStore",
        "DepartmentStore",
        "EBikeService",
        "ElectronicsStore",
        "FarmShop",
        "Florist",
        "FurnitureStore",
        "GardenStore",
        "GroceryStore",
        "HardwareStore",
        "HobbyShop",
        "HomeGoodsStore",
        "ITFirm",
        "JewelryStore",
        "Kiosk",
        "LiquorStore",
        "MensClothingStore",
        "MobilePhoneStore",
        "MovieRentalStore",
        "MusicStore",
        "OfficeEquipmentStore",
        "Opticians",
        "OutletStore",
        "Perfumery",
        "Smith",
        "SnowsportRental",
        "SportingGoodsStore",
        "TobaccoShop",
        "WatersportRental",
        "WholesaleStore",
        "ThermalSpa",
        "TouristInformationCenter",
        "TravelAgency",
        "YouthClub",
    ]
    #"LodgingBusiness",
    return subClasses

# Place specific properties
def getProperties():
    properties = {}
    
    properties['currenciesAccepted'] = 'currenciesAccepted'
    properties['openingHours'] = 'openingHours'
    properties['paymentAccepted'] = 'paymentAccepted'
    properties['priceRange'] = 'priceRange'
    
    return properties

def setBody(family, families):
    body = Family.setBody(family, families)
    
    attribute_requirements = {"sku": "sku", "name": "name", "image": "image", "license": "license", "openstreetmap_id": "openstreetmap_id"}

    body['attributes']['license'] = 'license'
    body['attributes']['copyrightHolder'] = 'copyrightHolder'
    body['attributes']['author'] = 'author'

    body['attributes']['currenciesAccepted'] = 'currenciesAccepted'
    body['attributes']['openingHours'] = 'openingHours'
    body['attributes']['paymentAccepted'] = 'paymentAccepted'
    body['attributes']['priceRange'] = 'priceRange'

    body['attributes']['metaTitle'] = 'metaTitle'
    body['attributes']['metaDescription'] = 'metaDescription'
    body['attributes']['canonicalUrl'] = 'canonicalUrl'
    
    body['attributes']['openstreetmap_id'] = 'openstreetmap_id'

    body['attributes']['image_summer'] = 'image_summer'
    body['attributes']['image_winter'] = 'image_winter'

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
    
    # marker Icon
    body['attributes']['markerIcon'] = 'markerIcon'
    
    # discover.swiss Testing
    body['attributes']['parking'] = 'parking'
    body['attributes']['publicTransport'] = 'publicTransport'
    
    body['attribute_requirements'] = {}
    body["attribute_requirements"]['ecommerce'] = attribute_requirements
    body["attribute_requirements"]['mice'] = attribute_requirements
    
    ## plus Properties from Place! 
    
    # Add and merge properties from Place    
    placeProperties = Place.getProperties()
    
    for key, value in placeProperties.items():
        print(key, value)
        body["attributes"][key] = value
        
    debug.addToLogFileBody(family, body)
    
    return body