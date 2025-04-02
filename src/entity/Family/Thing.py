import entity.Family.Family as Family

def getSubClasses():
    subClasses = [

    ]
    #"LodgingBusiness",
    return subClasses

def getProperties():
    properties = {}
    
    properties['sku'] = 'sku'
    properties['name'] = 'name'
    properties['disambiguatingDescription'] = 'disambiguatingDescription'
    properties['description'] = 'description'
    properties['image'] = 'image'
    properties['image_description'] = 'image_description'
    
    # License
    properties['license'] = 'license'
    properties['copyrightHolder'] = 'copyrightHolder'
    properties['author'] = 'author'
    
    return properties