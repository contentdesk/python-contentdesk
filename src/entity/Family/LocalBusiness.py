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

# Specific properties
def getProperties():
    properties = {}
    
    properties['currenciesAccepted'] = 'currenciesAccepted'
    properties['openingHours'] = 'openingHours'
    properties['paymentAccepted'] = 'paymentAccepted'
    properties['priceRange'] = 'priceRange'
    
    properties['award'] = 'award'
    
    # Add and merge properties from Place    
    placeProperties = Place.getProperties()
    
    for key, value in placeProperties.items():
        properties[key] = value
    
    return properties

def setBody(family, families):
    #body = Family.setBody(family, families)
    code = family["label"]
    
    print ("SET BODY - LocalBusiness!")
    attribute_requirements = {
        "sku": "sku", 
        "name": "name", 
        "image": "image", 
        "license": "license", 
        "openstreetmap_id": "openstreetmap_id"
        }
    
    # Create body
    body = {
        "code": code,
        "attribute_as_label": 'name',
        "attribute_as_image": 'image',
        "attribute_requirements": {
            "ecommerce": attribute_requirements,
            "mice": attribute_requirements,
        },
        "labels": {
            "en_US": family["label.en_US"],
            "de_CH": family["label.de_CH"],
            "fr_FR": family["label.fr_FR"],
            "it_IT": family["label.it_IT"],
        }
    }

    body['attribute_requirements'] = {}
    body["attribute_requirements"]['ecommerce'] = attribute_requirements
    body["attribute_requirements"]['mice'] = attribute_requirements
        
    body['attributes'] = {}
    body['attributes'] = getProperties()
    
    return body