import service.debug as debug
import entity.Family.Family as Family

def setBody(family, families):
    #body = Family.setBody(family, families)

    if family["attribute_requirements.ecommerce"] != None:
        attribute_requirements = {attrRequ: attrRequ for attrRequ in family["attribute_requirements.ecommerce"].split(",")}
    else:
        attribute_requirements = {"sku": "sku", "name": "name", "image": "image"}

    if family["attributes"] != None:
        attributes = {attr: attr for attr in family["attributes"].split(",")}
    else:
        attributes = {}

    code = family["label"]
    body = {}
    body["code"] = code
    body["attribute_as_image"] = "media"
    body["attribute_as_label"] = "name"
    body["attribute_requirements"] = attribute_requirements
    body["labels"] = {
        "en_US": family["label"],
        "de_CH": family["label"],
        "fr_FR": family["label"],
        "it_IT": family["label"]
    }
    body["attributes"] = attributes

    return body
