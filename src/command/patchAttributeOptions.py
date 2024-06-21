import json
from akeneo.akeneo import Akeneo
import pandas as pd

import sys
sys.path.append("..")

from service.loadEnv import loadEnv, getEnvironment
import service.cliArguments as cliArguments

def readCsv(url):
    # Read the CSV data into a pandas DataFrame
    df = pd.read_csv(url)
    return df

# Load properties.json
def getAttributeOptions():
    # get From Google Sheet
    othersUrl = "https://docs.google.com/spreadsheets/d/1J0iDoPqamlvWzBvxmZPDB0_uks0U3UuPLvizGolVeYg/gviz/tq?tqx=out:csv&sheet=others"
    starRatingUrl = "https://docs.google.com/spreadsheets/d/1VtVxnO0YfJ3ztRwcsK3elN8orGhlSRSDbkn8Whl523Y/gviz/tq?tqx=out:csv&sheet=starRating"
    servesCuisineUrl = "https://docs.google.com/spreadsheets/d/1B3yJroHLuNgIDSCDfxIY5tpX13zyn1ngigGMlNaxVgk/gviz/tq?tqx=out:csv&sheet=servesCuisine"
    amenityFeatureUrl = "https://docs.google.com/spreadsheets/d/1eK8PI9OEfdeBPDYXegdmA6rs3hl5RcDCAUYlJ5iIrV4/gviz/tq?tqx=out:csv&sheet=amenityFeature"
    awardUrl = "https://docs.google.com/spreadsheets/d/1XDmYmyp46la94TQ4ztPXirWzHPgw4mAwCBf61tEAYIo/gviz/tq?tqx=out:csv&sheet=award"
    # Set DataFrame
    dfOthers = readCsv(othersUrl)
    dfStarRating = readCsv(starRatingUrl)
    dfServesCuisine = readCsv(servesCuisineUrl)
    dfAmenityFeature = readCsv(amenityFeatureUrl)
    dfAward = readCsv(awardUrl)

    # Merge DataFrame
    df = pd.concat([dfOthers, dfStarRating, dfServesCuisine, dfAmenityFeature, dfAward])

    #print(df)

    json_data = df.to_json(orient="records")

    #print(json_data)
    return json.loads(json_data)


def patchAttributeOptionsAkeneo(akeneo, attributeOptions):
    for attributOption in attributeOptions:
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

def main():
    environments = cliArguments.getEnvironment(sys)
    #arguments = cliArguments.getArguments(sys)

    print("START PATCH ATTRIBUTES")
    for environment in environments:
        targetCon = loadEnv(environment)
        target = Akeneo(targetCon["host"], targetCon["clientId"], targetCon["secret"], targetCon["user"], targetCon["passwd"])

        # Get Attribute Options
        #attributeFileToLoad = ["others", "starRating", "amentityFeature", "potentialAction", "award", "typeOfBed" ]
        # leisure --> direct from discover.swiss Categories

        # Load Attribute Options
        attributeOptions = getAttributeOptions()

        # Patch Attributes
        patchAttributeOptionsAkeneo(target, attributeOptions)
    print("FINISH PATCH ATTRIBUTES")

if __name__ == '__main__':
    main()