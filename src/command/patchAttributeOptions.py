import json
from akeneo.akeneo import Akeneo
import pandas as pd

import sys
sys.path.append("..")

from service.loadEnv import loadEnv, getEnvironment
import service.cliArguments as cliArguments

# Load properties.json
def getAttributeOptions():
    # get From Google Sheet
    othersUrl = "https://docs.google.com/spreadsheets/d/1J0iDoPqamlvWzBvxmZPDB0_uks0U3UuPLvizGolVeYg/gviz/tq?tqx=out:csv&sheet=others"
    starRatingUrl = "https://docs.google.com/spreadsheets/d/1VtVxnO0YfJ3ztRwcsK3elN8orGhlSRSDbkn8Whl523Y/gviz/tq?tqx=out:csv&sheet=starRating"
    servesCuisineUrl = "https://docs.google.com/spreadsheets/d/1B3yJroHLuNgIDSCDfxIY5tpX13zyn1ngigGMlNaxVgk/gviz/tq?tqx=out:csv&sheet=servesCuisine"
    amenityFeatureUrl = "https://docs.google.com/spreadsheets/d/1eK8PI9OEfdeBPDYXegdmA6rs3hl5RcDCAUYlJ5iIrV4/gviz/tq?tqx=out:csv&sheet=amenityFeature"
    awardUrl = "https://docs.google.com/spreadsheets/d/1XDmYmyp46la94TQ4ztPXirWzHPgw4mAwCBf61tEAYIo/gviz/tq?tqx=out:csv&sheet=award"
    potentialActionUrl = "https://docs.google.com/spreadsheets/d/10kMpDMQRUPbyuDpFlAaJIjIf_vdKllKPQd0a0PppDq8/gviz/tq?tqx=out:csv&sheet=potentialAction"
    leisureUrl = "https://docs.google.com/spreadsheets/d/1AyPg-4SXP5Cm6BbWnFpxtrLvqaO51P1unlmw0KH4UHg/gviz/tq?tqx=out:csv&sheet=leisure"
    outdooractivePoiCategoriesUrl = "https://docs.google.com/spreadsheets/d/13_igR13FPi2MZevvQGLVcWx8Qv6tznELCIYDUE6dYOY/gviz/tq?tqx=out:csv&sheet=outdooractive_poi_category"

    # Set DataFrame
    dfOthers = pd.read_csv(othersUrl)
    dfStarRating = pd.read_csv(starRatingUrl)
    dfServesCuisine = pd.read_csv(servesCuisineUrl)
    dfAmenityFeature = pd.read_csv(amenityFeatureUrl)
    dfAward = pd.read_csv(awardUrl)
    dfPotentialAction = pd.read_csv(potentialActionUrl)
    dfLeisure = pd.read_csv(leisureUrl)
    dfOutdooractivePoiCategories = pd.read_csv(outdooractivePoiCategoriesUrl)

    # Merge DataFrame
    df = pd.concat([dfOthers, dfStarRating, dfServesCuisine, dfAmenityFeature, dfAward, dfPotentialAction, dfLeisure, dfOutdooractivePoiCategories])

    #print(df)

    json_data = df.to_json(orient="records")

    #print(json_data)
    return json.loads(json_data)

def patchAttributeOptionsAkeneo(akeneo, attributOption):
    print("Attribute: ", attributOption['attribute'])
    print("Code: ", attributOption['code'])
    attribute = attributOption['attribute']
    code = str(attributOption['code'])
    body = {
        "code": str(attributOption['code']),
        "attribute": attributOption['attribute'],
        "sort_order": attributOption['sort_order'],
        "labels": {
            "en_US": attributOption['labels.en_US'],
            "de_CH": attributOption['labels.de_CH'],
            "fr_FR": attributOption['labels.fr_FR'],
            "it_IT": attributOption['labels.it_IT'],
        }
    }
    response = akeneo.patchAttributOptionsByCode(code, attribute, body)
    print(response)

def checkAttributeOptionsInstance(target, attributeOptions):
    for attributOption in attributeOptions:
        if attributOption["instance"] != None:
            checkInstanceArray = attributOption["instance"].split(",")
            print(" - Check Instance: ", checkInstanceArray)
            print(" - Host Instance: ", target.getHost())
            if target.getHost() in checkInstanceArray:
                patchAttributeOptionsAkeneo(target, attributOption)
            else:
                print(" - Skip Patching")
                print(" - Not in Instance: ", target.getHost())
        else:
            patchAttributeOptionsAkeneo(target, attributOption)

def main():
    environments = cliArguments.getEnvironment(sys)
    arguments = cliArguments.getArguments(sys)

    # Load Attribute Options
    attributeOptions = getAttributeOptions()

    print("START PATCH ATTRIBUTES")
    for environment in environments:
        targetCon = loadEnv(environment)
        target = Akeneo(targetCon["host"], targetCon["clientId"], targetCon["secret"], targetCon["user"], targetCon["passwd"])

        # Get Attribute Options
        #attributeFileToLoad = ["others", "starRating", "amentityFeature", "potentialAction", "award", "typeOfBed" ]
        # leisure --> direct from discover.swiss Categories

        if arguments == None:
            checkAttributeOptionsInstance(target, attributeOptions)
        else:
            # Filter Attribute Options by arguements (attribute)
            attributeOptions = [attribute for attribute in attributeOptions if attribute["attribute"] in arguments]
            checkAttributeOptionsInstance(target, attributeOptions)
    print("FINISH PATCH ATTRIBUTES")

if __name__ == '__main__':
    main()