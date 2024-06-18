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
        code == "Resort"
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
    elif ( code == "TouristAttraction"):
        import entity.Family.TouristAttraction as Family
    elif ( code == "CivicStructure"):
        import entity.Family.CivicStructure as Family
    else:
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
        print("Clear Attributes")
        response = akeneo.patchFamily(code, clearBody)
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