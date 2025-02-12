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
    ]
    return subClasses

def setBody(family, families):
    body = Family.setBody(family, families)
    
    attribute_requirements = {"sku": "sku", "name": "name", "image": "image", "license": "license", "openstreetmap_id": "openstreetmap_id"}

    # https://schema.org/CivicStructure
    body['attributes']['openingHours'] = 'openingHours'
    
    # Contentdesk.io Settings
    body['attributes']['paymentAccepted'] = 'paymentAccepted'
    body['attributes']['currenciesAccepted'] = 'currenciesAccepted'

    body['attributes']['license'] = 'license'
    body['attributes']['copyrightHolder'] = 'copyrightHolder'
    body['attributes']['author'] = 'author'

    body['attributes']['typicalAgeRange'] = 'typicalAgeRange'
    body['attributes']['gender'] = 'gender'

    body['attributes']['metaTitle'] = 'metaTitle'
    body['attributes']['metaDescription'] = 'metaDescription'
    body['attributes']['canonicalUrl'] = 'canonicalUrl'

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
    
    body['attribute_requirements'] = {}
    body["attribute_requirements"]['ecommerce'] = attribute_requirements
    
    # Add and merge properties from Place    
    placeProperties = Place.getProperties()
    
    for key, value in placeProperties.items():
        print(key, value)
        if key not in body["attributes"]:
            body["attributes"][key] = value

    return body