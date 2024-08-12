# Export all Products with Attribute license

# Mapping License options
# cc_by to ccby

# Remove old Options

# Upload all Products with Attribute license

def getProducts(target, attribute):
    search = {
        "search": {
            "query": {
                "query": "*",
                "fields": ["categories"]
            }
        }
    }
    target.getProducts()
    print("Get Products")
    
def transform(products):
    print("Transform Products")
    
def uploadProducts(products):
    print("Upload Products")