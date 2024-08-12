# Export all Products with Attribute license

# Mapping License options
# cc_by to ccby

# Remove old Options

# Upload all Products with Attribute license

def getProducts(target, attribute):
    #search = 'search={"openingHours_text":[{"operator":"NOT EMPTY","value":"","locale":"de_CH"}]}'
    search = '{"license":[{"operator":"NOT EMPTY","value":""}]}'
    products = target.getProductBySearch(search)
    return products
    
def transform(products):
    print("Transform Products")
    
def uploadProducts(products):
    print("Upload Products")