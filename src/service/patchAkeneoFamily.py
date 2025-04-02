import service.debug as debug
import importlib
import service.instanceAttributes as instanceAttributes

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
    
    if "MeetingRoom" in code:
        print(" - Module - Load MeetingRoom")
        module = importlib.import_module("entity.Family.MeetingRoom")
        return module
    elif "Webcam" in code:
        print(" - Module - Load Webcam")
        module = importlib.import_module("entity.Family.Webcam")
        return module
    elif "FoodEstablishment" in code:
        print(" - Module - Load FoodEstablishment")
        module = importlib.import_module("entity.Family.FoodEstablishment")
        return module
    elif parent in import_map:
        import_path, message = import_map[parent]
        print(" - Module - "+message)
        #import_path = __import__(import_path, fromlist=['Family'])
        module = importlib.import_module(import_path)
        print(import_path)
        #if hasattr(module, 'setBody'):
        #    result = module.setBody(code, parent)  # Aufruf der Funktion get_info() aus dem Modul
        #    print(f"{code} Info: {result}")
        return module
    else:
        # Default-Fall
        print("Load Family")
        module = importlib.import_module("entity.Family.Family")
        #import_path = __import__("entity.Family.Family", fromlist=['Family'])
        return module

def patchAkeneoFamily(family, families, target):
    # Load Family Modul
    print (" - LOAD Module")
    #print (" - Family: ", family["label"])
    #print (" - Parent: ", family["parent"])
    if family["parent"] == None:
        module = importFamilyEnitity(family["label"], family["label"])
    else:
        module = importFamilyEnitity(family["label"],family["parent"])

    # Set Body by Modul
    #print("- Parent Family: ", family["parent"])
    body = module.setBody(family, families, target)
    print(" - DEBUG - ", family['label'])
    debug.addToLogFileBody(str(family['label']), body)
    
    # Load instanceAttributes
    getInstanceAttributes = instanceAttributes.getInstanceAttributes(target)
        
    # Add instanceAttributes to body['attributes']
    for key, value in getInstanceAttributes.items():
        print(key, value)
        body["attributes"][key] = value
    
    # Patch Family
    print("- PATCH Family: ", family["label"])
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