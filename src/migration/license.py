# Export all Products with Attribute license

# Mapping License options
# cc_by to ccby

# Remove old Options

# Upload all Products with Attribute license

# https://tourismus.atlassian.net/browse/PIM-483

def getProducts(target, attribute):
    #search = 'search={"openingHours_text":[{"operator":"NOT EMPTY","value":"","locale":"de_CH"}]}'
    search = '{"license":[{"operator":"IN","value":["cc_by","cc_by_sa","cc_by_nd","copyrightHolder"]}]}&attributes=license'
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
            elif(product['values']["license"][0]['data'] == "cc_by_sa"):
                product['values']["license"][0]['data'] = "ccbysa"
                productsUpdated.append(product)
            elif(product['values']["license"][0]['data'] == "cc_by_nd"):
                product['values']["license"][0]['data'] = "ccbynd"
                productsUpdated.append(product)
            elif(product['values']["license"][0]['data'] == "copyrightHolder"):
                product['values']["license"][0]['data'] = "copyright"
                productsUpdated.append(product)
    
    return productsUpdated
    
def uploadProducts(target, products):
    for product in products:
        print("Upload Product: ", product['identifier'])
        response = target.patchProductByCode(product['identifier'], product)
        print("Response: ", response)
        
    print("Upload Products")