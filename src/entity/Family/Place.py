import service.debug as debug
import json
import entity.Family.Thing as Thing

def merge_dicts(dict1, dict2):
    dict1.update(dict2)
    return dict1

def getIgnoreProperties():
    with open('../../output/index/ignoreProperties.json', 'r') as f:
        ignoreProperties = json.load(f)

    ignoreProperties = [prop["label"] for prop in ignoreProperties]

    return ignoreProperties

def getFullPropertiesbyType(code):
    with open('../../output/typesFullProperties.json', 'r') as f:
        typeFullProperties = json.load(f)
    
    typeSchema = "schema:"+code
    attributes = []
    #print("Get Full Properties: ", typeSchema)
    #print(typeFullProperties[typeSchema])
    if typeSchema in typeFullProperties:
        for item in typeFullProperties[typeSchema]:
            attributes.append(item.split(":")[1])

    return attributes

def removeIgnoreProperties(properties, ignoreProperties):
    newProperties = {}
    for prop in properties:
        #print("Check Ignore Property: ", prop)
        #print("Ignore Properties: ", ignoreProperties)
        if prop not in ignoreProperties:
            #print("Add Property: ", prop)
            newProperties[prop] = properties[prop]
        #else:
            #print("Ignore Property: ", prop)
    return newProperties

def getTypeProperties(code):
    attributes = {}
    print("Get Family Attributes: ", code)
    typeClassProperties = getFullPropertiesbyType(code)

    #attributes = attributes + typeClassProperties
    # add array to dict
    for prop in typeClassProperties:
        attributes[prop] = prop

    #if "rdfs:subClassOf" in typeClass:
        #print(type(typeClass["rdfs:subClassOf"]))
        #if type(typeClass["rdfs:subClassOf"]) == dict:
        #    attributes = merge_dicts(attributes, getTypeProperties(typeClass["rdfs:subClassOf"]["@id"].split(":")[1]))
        #elif type(typeClass["rdfs:subClassOf"]) == list:
        #    for typeChild in typeClass["rdfs:subClassOf"]:
        #        attributes = merge_dicts(attributes, getTypeProperties(typeChild["@id"].split(":")[1]))

    return attributes

def getParentAttributes(type, types, attributes):
    if type['attributes'] != None:
        #print("Merge Parent Attributes:")
        # make type['attributes'] to dict with two values
        # by Google Sheet
        typeAttributes = {attr: attr for attr in type['attributes'].split(",")} 
        # by Schema.org
        typeClassProperties = getTypeProperties(type["label"])
        #print("Parent Attributes Schema.org:")
        #print(typeClassProperties)

        attributes = merge_dicts(attributes, typeClassProperties)
        #print("Attributes with Schema.org:")
        #print(attributes)

        # Merge Attributes
        #print("Parent Attributes:")
        #print(typeAttributes)
        attributes = merge_dicts(attributes, typeAttributes)
    if 'parent' in type:
        if type['parent'] != None:
            if type['label'] != "Thing":
                print("Parent Type: ", type['parent'])
                # find in types array type['parent'] as type['label']
                parent = [parent for parent in types if parent["label"] == type['parent']]
                #print("Check Parent: ")
                #print(parent)
                getParentAttributes(parent[0], types, attributes)
    return attributes

def getParentAttributesRequirements(type, types, attribute_requirements):
    if type['attribute_requirements.ecommerce'] != None:
        #print("Merge Parent Attributes Requirements:")
        # make type['attributes'] to dict with two values
        typeAttributes = {attr: attr for attr in type['attribute_requirements.ecommerce'].split(",")}
        # Merge Attributes
        #print(typeAttributes)
        attribute_requirements = merge_dicts(attribute_requirements, typeAttributes)
    if 'parent' in type:
        if type['parent'] != None:
            if type['label'] != "Thing":
                print("Parent Type: ", type['parent'])
                #print("Parent Type: ", type['parent'])
                # find in types array type['parent'] as type['label']
                parent = [parent for parent in types if parent["label"] == type['parent']]
                #print("Check Parent: ")
                #print(parent)
                attribute_requirements = getParentAttributesRequirements(parent[0], types, attribute_requirements)

    return attribute_requirements

def checkParentType(type, types, checkType):
    if type['label'] == checkType:
        return True
    
    if 'parent' in type:
        if type['parent'] != None:
            if type['label'] != "Thing":
                print("Check Parent Type: ", type['parent'])
                # find in types array type['parent'] as type['label']
                parent = [parent for parent in types if parent["label"] == type['parent']]
                #print("Check Parent: ")
                #print(parent)
                return checkParentType(parent[0], types, checkType)

def getFamilyAttributes(code, attributes):
    # Dict to Array
    attributes = merge_dicts(attributes, getTypeProperties(code))
    # add sku to attributes dict
    attributes["sku"] = "sku"
    attributes["name"] = "name"
    #print ("Clear Attributes: ", attributes)
    return attributes

def removeProperties(code, attributes):
    # Dict to Array
    attributes = merge_dicts(attributes, getTypeProperties(code))
    #print ("Complete Attributes befor Removed: ", attributes)
    ignoreProperties = getIgnoreProperties()
    #print ("Ignore Properties: ")
    #print(ignoreProperties)
    attributes = removeIgnoreProperties(attributes, ignoreProperties)
    # add sku to attributes dict
    attributes["sku"] = "sku"
    #print ("Clear Attributes: ", attributes)
    return attributes

# Place specific properties
def getProperties():
    properties = {}
    
    # Allgemein
    properties['sku'] = 'sku'
    properties['name'] = 'name'
    properties['description'] = 'description'
    properties['disambiguatingDescription'] = 'disambiguatingDescription'
    properties['image'] = 'image'
    properties['image_description'] = 'image_description'
    
    # License
    properties['license'] = 'license'
    properties['copyrightHolder'] = 'copyrightHolder'
    properties['author'] = 'author'

    # Coordinations
    properties['longitude'] = 'longitude'
    properties['latitude'] = 'latitude'

    # Address
    properties['streetAddress'] = 'streetAddress'
    properties['postalCode'] = 'postalCode'
    properties['addressLocality'] = 'addressLocality'
    properties['addressCountry'] = 'addressCountry'
    properties['addressRegion'] = 'addressRegion'
    # Contact
    properties['legalName'] = 'legalName'
    properties['department'] = 'department'
    properties['honorificPrefix'] = 'honorificPrefix'
    properties['givenName'] = 'givenName'
    properties['familyName'] = 'familyName'
    properties['telephone'] = 'telephone'
    properties['email'] = 'email'
    properties['url'] = 'url'
    
    properties['openingHoursSpecification'] = 'openingHoursSpecification'
    properties['openingHours'] = 'openingHours'
    
    # Media
    properties['google_image_gallery_use_pro_channel'] = 'google_image_gallery_use_pro_channel'
    properties['image_01_scope'] = 'image_01_scope'
    properties['image_02_scope'] = 'image_02_scope'
    properties['image_03_scope'] = 'image_03_scope'
    properties['image_04_scope'] = 'image_04_scope'
    properties['image_05_scope'] = 'image_05_scope'
    properties['image_06_scope'] = 'image_06_scope'
    properties['image_07_scope'] = 'image_07_scope'
    properties['image_08_scope'] = 'image_08_scope'
    properties['image_09_scope'] = 'image_09_scope'
    properties['image_10_scope'] = 'image_10_scope'
    
    properties['image_01_scope_description'] = 'image_01_scope_description'
    properties['image_02_scope_description'] = 'image_02_scope_description'
    properties['image_03_scope_description'] = 'image_03_scope_description'
    properties['image_04_scope_description'] = 'image_04_scope_description'
    properties['image_05_scope_description'] = 'image_05_scope_description'
    properties['image_06_scope_description'] = 'image_06_scope_description'
    properties['image_07_scope_description'] = 'image_07_scope_description'
    properties['image_08_scope_description'] = 'image_08_scope_description'
    properties['image_09_scope_description'] = 'image_09_scope_description'
    properties['image_10_scope_description'] = 'image_10_scope_description'
    
    #properties['publicAccess'] = 'publicAccess'
    properties['isAccessibleForFree'] = 'isAccessibleForFree'
    
    ## Contentdesk.io Settings
    properties['openstreetmap_id'] = 'openstreetmap_id'
    
    properties['search_text_pro_channel'] = 'search_text_pro_channel'
    properties['promo_sort_order_scope'] = 'promo_sort_order_scope'
    properties['potentialAction'] = 'potentialAction'
    properties['target'] = 'target'
    
    properties['metaTitle'] = 'metaTitle'
    properties['metaDescription'] = 'metaDescription'
    properties['canonicalUrl'] = 'canonicalUrl'
    
    # Add and merge properties from Place    
    thingProperties = Thing.getProperties()
    
    for key, value in thingProperties.items():
        print(key, value)
        properties[key] = value
    
    return properties

# TODO: CHEck if needed!
def create(family, families, akeneo):
    code = family["label"]

    # Set default values
    if family["attribute_requirements.ecommerce"] != None:
        attribute_requirements = {attrRequ: attrRequ for attrRequ in family["attribute_requirements.ecommerce"].split(",")}
        #attribute_requirements = family["attribute_requirements.ecommerce"].split(",")
    else:
        attribute_requirements = {"sku": "sku", "name": "name", "image": "image", "openstreetmap_id": "openstreetmap_id"}

    if family["attribute_as_label"] == None:
        family["attribute_as_label"] = "name"

    if family["attribute_as_image"] == None:
        family["attribute_as_image"] = "image"

    print("Attribute Requirements - Create")
    attribute_requirements = getParentAttributesRequirements(family, families, attribute_requirements)
    
    #print("Attribute Requirements: ")
    #print(attribute_requirements)

    # Create body
    body = {
        "code": code,
        "attribute_as_label": family["attribute_as_label"],
        "attribute_as_image": family["attribute_as_image"],
        "attribute_requirements": {
            "ecommerce": attribute_requirements,
        },
        "labels": {
            "en_US": family["label.en_US"],
            "de_CH": family["label.de_CH"],
            "fr_FR": family["label.fr_FR"],
            "it_IT": family["label.it_IT"],
        }
    }

    # Type specific attributes
    if family["attributes"] != None:
        attributes = {attr: attr for attr in family["attributes"].split(",")}
    else:
        attributes = {}
    attributes = getFamilyAttributes(code, attributes)
    #print("Attributes: ")
    #print(attributes)

    # add Parent Attributes
    attributes = getParentAttributes(family, families, attributes)

    # Check if Place Type
    if checkParentType(family, families, "Place"):
        print("Yes - Place Type")

    # Check if specific attributes are set
    # examples license needs add copyrightHolder and author
    # examples potentialAction needs traget
    
    if 'image' not in attributes:
        attributes['image'] = 'image'
        attributes['image_description'] = 'image_description'

    if 'openingHoursSpecification' in attributes:
        attributes['google_opening_hours_use'] = 'google_opening_hours_use'
        attributes['openingHours'] = 'openingHours'

    # Images / Gallery
    if code != "Person" or code != "Organization":
        if 'image_01_scope' in attributes:
            attributes['image_01_scope_description'] = 'image_01_scope_description'
            attributes['google_image_gallery_use_pro_channel'] = 'google_image_gallery_use_pro_channel'
        if 'image_02_scope' in attributes:
            attributes['image_02_scope_description'] = 'image_02_scope_description'
        if 'image_03_scope' in attributes:
            attributes['image_03_scope_description'] = 'image_03_scope_description'
        if 'image_04_scope' in attributes:
            attributes['image_04_scope_description'] = 'image_04_scope_description'
        if 'image_05_scope' in attributes:
            attributes['image_05_scope_description'] = 'image_05_scope_description'
        if 'image_06_scope' in attributes:
            attributes['image_06_scope_description'] = 'image_06_scope_description'
        if 'image_07_scope' in attributes:
            attributes['image_07_scope_description'] = 'image_07_scope_description'
        if 'image_08_scope' in attributes:
            attributes['image_08_scope_description'] = 'image_08_scope_description'
        if 'image_09_scope' in attributes:
            attributes['image_09_scope_description'] = 'image_09_scope_description'
        if 'image_10_scope' in attributes:
            attributes['image_10_scope_description'] = 'image_10_scope_description'
        # marker Icon
        attributes['markerIcon'] = 'markerIcon'
            
    if 'geo' in attributes:
        attributes['longitude'] = 'longitude'
        attributes['latitude'] = 'latitude'

    if 'address' in attributes:
        attributes['streetAddress'] = 'streetAddress'
        attributes['postalCode'] = 'postalCode'
        attributes['addressLocality'] = 'addressLocality'
        attributes['addressCountry'] = 'addressCountry'
        attributes['addressRegion'] = 'addressRegion'
        # Contact
        attributes['legalName'] = 'legalName'
        attributes['department'] = 'department'
        attributes['honorificPrefix'] = 'honorificPrefix'
        attributes['givenName'] = 'givenName'
        attributes['familyName'] = 'familyName'
        attributes['email'] = 'email'

    if (
        code == "FoodEstablishment" or
        code == "Bakery" or
        code == "BarOrPub" or
        code == "Brewery" or
        code == "CafeOrCoffeeShop" or 
        code == "Distillery" or
        code == "FastFoodRestaurant" or
        code == "IceCreamShop" or 
        code == "Restaurant" or
        code == "Winery"
        ):
        if 'starRating' in attributes:
            attributes.pop('starRating')

    # Add to all
    attributes['search_text_pro_channel'] = 'search_text_pro_channel'
    attributes['promo_sort_order_scope'] = 'promo_sort_order_scope'
    #attributes['license'] = 'license'
    attributes['potentialAction'] = 'potentialAction'

    attributes['license'] = 'license'
    attributes['copyrightHolder'] = 'copyrightHolder'
    attributes['author'] = 'author'
    attributes['openstreetmap_id'] = 'openstreetmap_id'
    
    if 'potentialAction' in attributes:
        attributes['target'] = 'target'

    #print("Attributes: ")
    #print(attributes)

    # Remove Properties
    #print("Remove Attributes: ")
    ##print(code)
    attributes = removeProperties(code, attributes)

    # add Attributes to Body
    body["attributes"] = attributes
    
    clearBody = {
        "code": code,
        "attribute_as_label": family["attribute_as_label"],
        "attribute_as_image": family["attribute_as_image"],
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
            "en_US": family["label.en_US"],
            "de_CH": family["label.de_CH"],
            "fr_FR": family["label.fr_FR"],
            "it_IT": family["label.it_IT"],
        },
        "attributes": [
            "sku",
            "name",
            "image",
        ]
    }
    try:
        # Clear Attributes
        #print("Clear Attributes")
        response = akeneo.patchFamily(code, clearBody)
        # DEBUG - Write to file
        debug.addToFile(code, body)
        # To Akeneo
        print("Patch family: ", code)
        response = akeneo.patchFamily(code, body)
        debug.addToLogFile(code, response)
           
    except Exception as e:
        print("Error: ", e)
        print("patch Family: ", code)
        print("Response: ", response)
        debug.addToLogFile(code, response)
    return response

def setBody(family, families):
    code = family["label"]

    # Set default values
    if family["attribute_requirements.ecommerce"] != None:
        attribute_requirements = {attrRequ: attrRequ for attrRequ in family["attribute_requirements.ecommerce"].split(",")}
        #attribute_requirements = family["attribute_requirements.ecommerce"].split(",")
    else:
        attribute_requirements = {"sku": "sku", "name": "name", "image": "image", "license": "license", "openstreetmap_id": "openstreetmap_id"}
        attribute_requirementsMice = {"sku": "sku", "name": "name", "image": "image", "license": "license", "openstreetmap_id": "openstreetmap_id"}

    if family["attribute_as_label"] == None:
        family["attribute_as_label"] = "name"

    if family["attribute_as_image"] == None:
        family["attribute_as_image"] = "image"

    print("Attribute Requirements - setBody")
    attribute_requirements = getParentAttributesRequirements(family, families, attribute_requirements)
    
    #print("Attribute Requirements: ")
    #print(attribute_requirements)

    # Create body
    body = {
        "code": code,
        "attribute_as_label": family["attribute_as_label"],
        "attribute_as_image": family["attribute_as_image"],
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

    # Type specific attributes
    if family["attributes"] != None:
        attributes = {attr: attr for attr in family["attributes"].split(",")}
    else:
        attributes = {}
    attributes = getFamilyAttributes(code, attributes)
    #print("Attributes: ")
    #print(attributes)

    # add Parent Attributes
    attributes = getParentAttributes(family, families, attributes)

    # Check if specific attributes are set
    # examples license needs add copyrightHolder and author
    # examples potentialAction needs traget
    if 'image' not in attributes:
        attributes['image'] = 'image'
        attributes['image_description'] = 'image_description'
    if 'image' in attributes:
        attributes['image_description'] = 'image_description'

    if 'openingHoursSpecification' in attributes:
        attributes['google_opening_hours_use'] = 'google_opening_hours_use'
        attributes['openingHours'] = 'openingHours'

    # Images / Gallery
    print ("CHECK GALLERY")
    if code != "Person" or code != "Organization":
        print("No Person or Organization")
        print("Check Partent Place")
        if (family["parent"] == "Place" or
            family["parent"] == "LocalBusiness" or
            family["parent"] == "FoodEstablishment" or
            family["parent"] == "CivicStructure" or
            family["parent"] == "Accommodation" or
            family["parent"] == "Landform" or
            family["parent"] == "LodgingBusiness" or
            family["parent"] == "Store" or
            family["parent"] == "TouristAttraction" or
            family["parent"] == "HealthAndBeautyBusiness" or
            family["parent"] == "SportsActivityLocation" or
            family["parent"] == "PlaceOfWorship" or
            family["parent"] == "Church" or
            family["parent"] == "BodyOfWater" or
            family["parent"] == "AdministrativeArea" or
            family["parent"] == "GovernmentBuilding" or
            family["parent"] == "EducationalOrganization" or
            family["parent"] == "EntertainmentBusiness" or
            family["parent"] == "AutomotiveBusiness" or
            family["parent"] == "Room" or
            family["parent"] == "GovernmentOffice" or
            family["parent"] == "Resort"
            ):
            print("Yes - Place Type")
            attributes['image_01_scope'] = 'image_01_scope'
            attributes['image_02_scope'] = 'image_02_scope'
            attributes['image_03_scope'] = 'image_03_scope'
            attributes['image_04_scope'] = 'image_04_scope'
            attributes['image_05_scope'] = 'image_05_scope'
            attributes['image_06_scope'] = 'image_06_scope'
            attributes['image_07_scope'] = 'image_07_scope'
            attributes['image_08_scope'] = 'image_08_scope'
            attributes['image_09_scope'] = 'image_09_scope'
            attributes['image_10_scope'] = 'image_10_scope'
            
            # Summer and Winter Image
            attributes['image_summer'] = 'image_summer'
            attributes['image_winter'] = 'image_winter'
            
        if 'image_01_scope' in attributes:
            attributes['image_01_scope_description'] = 'image_01_scope_description'
            attributes['google_image_gallery_use_pro_channel'] = 'google_image_gallery_use_pro_channel'
        if 'image_02_scope' in attributes:
            attributes['image_02_scope_description'] = 'image_02_scope_description'
        if 'image_03_scope' in attributes:
            attributes['image_03_scope_description'] = 'image_03_scope_description'
        if 'image_04_scope' in attributes:
            attributes['image_04_scope_description'] = 'image_04_scope_description'
        if 'image_05_scope' in attributes:
            attributes['image_05_scope_description'] = 'image_05_scope_description'
        if 'image_06_scope' in attributes:
            attributes['image_06_scope_description'] = 'image_06_scope_description'
        if 'image_07_scope' in attributes:
            attributes['image_07_scope_description'] = 'image_07_scope_description'
        if 'image_08_scope' in attributes:
            attributes['image_08_scope_description'] = 'image_08_scope_description'
        if 'image_09_scope' in attributes:
            attributes['image_09_scope_description'] = 'image_09_scope_description'
        if 'image_10_scope' in attributes:
            attributes['image_10_scope_description'] = 'image_10_scope_description'
            
    attributes['google_image_gallery_use_pro_channel'] = 'google_image_gallery_use_pro_channel'
    
    attributes['image_01_scope'] = 'image_01_scope'
    attributes['image_02_scope'] = 'image_02_scope'
    attributes['image_03_scope'] = 'image_03_scope'
    attributes['image_04_scope'] = 'image_04_scope'
    attributes['image_05_scope'] = 'image_05_scope'
    attributes['image_06_scope'] = 'image_06_scope'
    attributes['image_07_scope'] = 'image_07_scope'
    attributes['image_08_scope'] = 'image_08_scope'
    attributes['image_09_scope'] = 'image_09_scope'
    attributes['image_10_scope'] = 'image_10_scope'

    attributes['image_01_scope_description'] = 'image_01_scope_description'
    attributes['image_02_scope_description'] = 'image_02_scope_description'
    attributes['image_03_scope_description'] = 'image_03_scope_description'
    attributes['image_04_scope_description'] = 'image_04_scope_description'
    attributes['image_05_scope_description'] = 'image_05_scope_description'
    attributes['image_06_scope_description'] = 'image_06_scope_description'
    attributes['image_07_scope_description'] = 'image_07_scope_description'
    attributes['image_08_scope_description'] = 'image_08_scope_description'
    attributes['image_09_scope_description'] = 'image_09_scope_description'
    attributes['image_10_scope_description'] = 'image_10_scope_description'

    if 'geo' in attributes:
        attributes['longitude'] = 'longitude'
        attributes['latitude'] = 'latitude'

    if 'address' in attributes:
        attributes['streetAddress'] = 'streetAddress'
        attributes['postalCode'] = 'postalCode'
        attributes['addressLocality'] = 'addressLocality'
        attributes['addressCountry'] = 'addressCountry'
        attributes['addressRegion'] = 'addressRegion'
        # Contact
        attributes['legalName'] = 'legalName'
        attributes['department'] = 'department'
        attributes['honorificPrefix'] = 'honorificPrefix'
        attributes['givenName'] = 'givenName'
        attributes['familyName'] = 'familyName'
        attributes['email'] = 'email'

    if (
        code == "FoodEstablishment" or
        code == "Bakery" or
        code == "BarOrPub" or
        code == "Brewery" or
        code == "CafeOrCoffeeShop" or 
        code == "Distillery" or
        code == "FastFoodRestaurant" or
        code == "IceCreamShop" or 
        code == "Restaurant" or
        code == "Winery"
        ):
        if 'starRating' in attributes:
            attributes.pop('starRating')

    # Add to all
    attributes['search_text_pro_channel'] = 'search_text_pro_channel'
    attributes['promo_sort_order_scope'] = 'promo_sort_order_scope'
    attributes['potentialAction'] = 'potentialAction'
    attributes['openstreetmap_id'] = 'openstreetmap_id'
    
    attributes['metaTitle'] = 'metaTitle'
    attributes['metaDescription'] = 'metaDescription'
    attributes['canonicalUrl'] = 'canonicalUrl'

    # License
    if 'license' in attributes:
        attributes['copyrightHolder'] = 'copyrightHolder'
        attributes['author'] = 'author'
    else:
        attributes['license'] = 'license'
        attributes['copyrightHolder'] = 'copyrightHolder'
        attributes['author'] = 'author'
        
    # add license to requirements attributes
    body['attribute_requirements']['ecommerce']['license'] = 'license'
    
    if 'potentialAction' in attributes:
        attributes['target'] = 'target'

    #print("Attributes: ")
    #print(attributes)
    
    #attributes['publicAccess'] = 'publicAccess'
    attributes['isAccessibleForFree'] = 'isAccessibleForFree'

    # Remove Properties
    #print("Remove Attributes: ")
    ##print(code)
    attributes = removeProperties(code, attributes)

    # add Attributes to Body
    body["attributes"] = attributes
    
    # Add and merge properties from Place    
    placeProperties = getProperties()
    
    for key, value in placeProperties.items():
        print(key, value)
        body["attributes"][key] = value
    
    return body