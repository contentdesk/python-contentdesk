# Export all Products with Attribute license

# Mapping License options
# cc_by to ccby

# Remove old Options

# Upload all Products with Attribute license

def getProducts(target, attribute):
    #search = 'search={"openingHours_text":[{"operator":"NOT EMPTY","value":"","locale":"de_CH"}]}'
    search = '{"license":[{"operator":"IN","value":["cc_by","cc_by_sa","cc_by_nd","cc0"]}]}&attributes=license'
    products = target.getProductBySearch(search)
    return products
    
def transform(products):
    print("Transform Products")
    productsUpdated = []
    for product in products:
        if "license" in product['values']:
            if product['values']["license"][0]['data'] == "cc_by":
                product['values']["license"][0]['data'] = "ccby"
                productsUpdated.append(product)
    
    return productsUpdated
    
def uploadProducts(products):
    print("Upload Products")