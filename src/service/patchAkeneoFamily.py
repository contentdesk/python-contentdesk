import service.debug as debug
import entity.Family.Family as Family
import entity.Family.LodgingBusiness as LodgingBusiness
import entity.Family.LocalBusiness as LocalBusiness
import entity.Family.FoodEstablishment as FoodEstablishment
import entity.Family.Landform as Landform
import entity.Family.Event as Event
import entity.Family.CivicStructure as CivicStructure
import entity.Family.Product as Product
import importlib

def importFamilyEnitity(code, parent):
    import_map = {
        "CivicStructure": ("entity.Family.CivicStructure", "Load CivicStructure"),
        "Event": ("entity.Family.Event", "Load Event"),
        "FoodEstablishment": ("entity.Family.FoodEstablishment", "Load FoodEstablishment"),
        "GuestCard": ("entity.Family.GuestCard", "Load GuestCard"),
        "Landform": ("entity.Family.Landform", "Load Landform"),
        "LocalBusiness": ("entity.Family.LocalBusiness", "Load LocalBusiness"),
        "LodgingBusiness": ("entity.Family.LodgingBusiness", "Load LodgingBusiness"),
        "MediaObject": ("entity.Family.MediaObject", "Load MediaObject"),
        "MeetingRoom": ("entity.Family.MeetingRoom", "Load MeetingRoom"),
        "Offer": ("entity.Family.Offer", "Load Offer"),
        "Organization": ("entity.Family.Organization", "Load Organization"),
        "Place": ("entity.Family.Place", "Load Place"),
        "Product": ("entity.Family.Product", "Load Product"),
        "Schedule": ("entity.Family.Schedule", "Load Schedule"),
        "Tour": ("entity.Family.Tour", "Load Tour"),
        "TouristAttraction": ("entity.Family.TouristAttraction", "Load TouristAttraction"),
        "Trail": ("entity.Family.Trail", "Load Trail"),
        "Webcam": ("entity.Family.Webcam", "Load Webcam"),
    }
    
    if parent in import_map:
        import_path, message = import_map[parent]
        print(" - Module - "+message)
        #import_path = __import__(import_path, fromlist=['Family'])
        module = importlib.import_module(import_path)
        print(import_path)
        #if hasattr(module, 'setBody'):
        #    result = module.setBody(code, parent)  # Aufruf der Funktion get_info() aus dem Modul
        #    print(f"{code} Info: {result}")
        return module
    elif "MeetingRoom" in code:
        print(" - Module - Load MeetingRoom")
        module = importlib.import_module("entity.Family.MeetingRoom")
        return module
    else:
        # Default-Fall
        print("Load Family")
        module = importlib.import_module("entity.Family.Family")
        #import_path = __import__("entity.Family.Family", fromlist=['Family'])
        return module

def patchAkeneoFamily(family, families, target):
    print (" - LOAD Module")
    module = importFamilyEnitity(family["label"],family["parent"])
    print("- PATCH Family: ", family["label"])
    print("- Parent Family: ", family["parent"])
    body = module.setBody(family, families)
    print(" - DEBUG - ", family['label'])
    debug.addToLogFileBody(str(family['label']), body)
    
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