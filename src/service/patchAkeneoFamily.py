import service.debug as debug
import entity.Family.Family as Family
import entity.Family.LodgingBusiness as LodgingBusiness
import entity.Family.LocalBusiness as LocalBusiness
import entity.Family.FoodEstablishment as FoodEstablishment
import entity.Family.Landform as Landform
import entity.Family.Event as Event
import entity.Family.CivicStructure as CivicStructure
import entity.Family.Product as Product

def importFamilyEnitity(code):
    import_map = {
        "MeetingRoom": ("entity.Family.MeetingRoom", "Load MeetingRoom"),
        "TouristAttraction": ("entity.Family.TouristAttraction", "Load TouristAttraction"),
        "Schedule": ("entity.Family.Schedule", "Load Schedule"),
        "Offer": ("entity.Family.Offer", "Load Offer"),
        "GuestCard": ("entity.Family.GuestCard", "Load GuestCard"),
        "Trail": ("entity.Family.Trail", "Load Trail"),
        "Recommendation": ("entity.Family.Recommendation", "Load Recommendation"),
        "Organization": ("entity.Family.Organization", "Load Organization"),
        "Place": ("entity.Family.Place", "Load Place"),
    }

    subclass_map = {
        LodgingBusiness: ("entity.Family.LodgingBusiness", "Load LodgingBusiness"),
        FoodEstablishment: ("entity.Family.FoodEstablishment", "Load FoodEstablishment"),
        CivicStructure: ("entity.Family.CivicStructure", "Load CivicStructure"),
        Event: ("entity.Family.Event", "Load Event"),
        Landform: ("entity.Family.Landform", "Load Landform"),
        Product: ("entity.Family.Product", "Load Product"),
        LocalBusiness: ("entity.Family.Place", "Load LocalBusiness"),
    }
    
    if code in import_map:
        import_path, message = import_map[code]
        print(message)
        import_path = __import__(import_path, fromlist=['Family'])
        return import_path

    # Überprüfen, ob der Code in den Subklassen vorhanden ist
    for cls, (import_path, message) in subclass_map.items():
        if code in cls.getSubClasses():
            print(message)
            import_path = __import__(import_path, fromlist=['Family'])
            return import_path
        
    # Default-Fall
    print("Load Family")
    import_path = __import__("entity.Family.Family", fromlist=['Family'])
    return import_path

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