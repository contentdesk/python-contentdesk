import service.debug as debug
import logging
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

def removeProperties(product):
    updateProduct = {}
    
    updateProduct['identifier'] = product['identifier']
    updateProduct['values'] = product['values']
    
    return updateProduct
    
def transform(products):
    print("Transform Products")
    productsUpdated = []
    for product in products:
        if "license" in product['values']:
            if product['values']["license"][0]['data'] == "cc_by":
                product['values']["license"][0]['data'] = "ccby"
                updateProduct = removeProperties(product)
                productsUpdated.append(updateProduct)
            elif(product['values']["license"][0]['data'] == "cc_by_sa"):
                product['values']["license"][0]['data'] = "ccbysa"
                updateProduct = removeProperties(product)
                productsUpdated.append(updateProduct)
            elif(product['values']["license"][0]['data'] == "cc_by_nd"):
                product['values']["license"][0]['data'] = "ccbynd"
                updateProduct = removeProperties(product)
                productsUpdated.append(updateProduct)
            elif(product['values']["license"][0]['data'] == "copyrightHolder"):
                product['values']["license"][0]['data'] = "copyright"
                updateProduct = removeProperties(product)
                productsUpdated.append(updateProduct)
    
    return productsUpdated
    
def uploadProducts(target, products):
    logging.basicConfig(
        filename="output/logs/migrations/app.log",
        encoding="utf-8",
        filemode="a",
        format="{asctime} - {levelname} - {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M",
    )
    for product in products:
        print("Upload Product: ", product['identifier'])
        print("Product: ", product)
        try:
            response = target.patchProductByCode(product['identifier'], product)
            print("Response: ", response)
        except Exception as e:
            print("Error: ", e)
            # Add To Error Log File
            logging.error("Error: ", e)
        
    print("Upload Products")