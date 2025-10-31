import entity.Family.Family as Family
import entity.Family.Place as Place

def getSubClasses():
    subClasses = [
        "CivicStructure",
        "AdministrativeArea",
        "City",
        "Country",
        "District",
        "MountainArea",
        "NatureReserve",
        "ProtectedArea",
        "State",
        "Alp",
        "NaturePark",
        "Airport",
        "AnimalPark",
        "Aquarium",
        "ArtObject",
        "ATM",
        "BathingSpot",
        "Beach",
        "Biotope",
        "BoatTerminal",
        "Bunker",
        "BusStop",
        "Cave",
        "Cemetery",
        "CityHall",
        "ClubHouse",
        "ConcertHall",
        "Court",
        "Crematorium",
        "CulturalCentre",
        "DamOrWeir",
        "EducationalOrganization",
        "EventVenue",
        "Farm",
        "Ferry",
        "Fireplace",
        "FireStation",
        "FootBridge",
        "Forest",
        "Forsthaus",
        "Gallery",
        "Garden",
        "GlacierGarden",
        "GovernmentBuilding",
        "Harbour",
        "HerbGarden",
        "Hospital",
        "InfoPoint",
        "InternetPoint",
        "LandingStage",
        "Lighthouse",
        "Mansion",
        "Market",
        "MeetingPoint",
        "Military",
        "Mill",
        "Mine",
        "MountainRescue",
        "Museum",
        "MusicVenue",
        "Observatory",
        "OperaHouse",
        "OutdoorStage",
        "ParkingFacility",
        "Pavillon",
        "PedestrianArea",
        "PerformingArtsTheater",
        "PicnicArea",
        "PlaceOfWorship",
        "BuddhistTemple",
        "Chapel",
        "Church",
        "CatholicChurch",
        "HinduTemple",
        "Monastery",
        "Mosque",
        "Synagogue",
        "Playground",
        "PoliceStation",
        "PublicToilet",
        "RecyclingPoint",
        "RVPark",
        "SaltCave",
        "Sbahn",
        "Shelter",
        "Sluice",
        "Street",
        "TaxiStand",
        "Theatre",
        "Bisse",
        "Bridge",
        "Castle",
        "Fortress",
        "Fountain",
        "IndustrialMonument",
        "Monument",
        "NaturalMonument",
        "ObservationTower",
        "Park",
        "Ruin",
        "Square",
        "StalactiteCave",
        "Viewpoint",
        "WaysideShrine",
        "TransportationSystemStation",
        "BusStation",
        "CableCarStation",
        "CogwheelTrainStation",
        "FunicularStation",
        "SubwayStation",
        "TrainStation",
        "TramStation",
        "Vineyard",
        "VisitorCenter",
        "WaysideCross",
        "Zoo",
        "TransportationSystemCivicStructure",
        "TransportationSystem"
    ]
    return subClasses

def getProperties():
    properties = {}
    
    # https://schema.org/CivicStructure
    properties['openingHours'] = 'openingHours'
    
    properties['paymentAccepted'] = 'paymentAccepted'
    properties['currenciesAccepted'] = 'currenciesAccepted'
    properties['typicalAgeRange'] = 'typicalAgeRange'
    properties['gender'] = 'gender'
    
    # Add and merge properties from Place    
    placeProperties = Place.getProperties()
    
    for key, value in placeProperties.items():
        properties[key] = value
    
    return properties

def setBody(family, families):
    body = Family.setBody(family, families)
    
    attribute_requirements = {"sku": "sku", "name": "name", "image": "image", "license": "license", "openstreetmap_id": "openstreetmap_id"}
    
    body['attribute_requirements'] = {}
    body["attribute_requirements"]['ecommerce'] = attribute_requirements
    body["attribute_requirements"]['mice'] = attribute_requirements
    
    body['attributes'] = {}
    body['attributes'] = getProperties()

    return body