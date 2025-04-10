import json
import requests
import pandas as pd
from akeneo.akeneo import Akeneo
import sys
sys.path.append("..")

from service.loadEnv import loadEnv
import service.debug as debug
import service.cliArguments as cliArguments
import service.migrationProductAttributeOptions as migrationProductAttributeOptions

############################################################################################################
# CLI Parameters 
# env attribute oldOption newOptions
# Example: python src/command/patchProducts.py dev award fisch goldenFisch
############################################################################################################

def main():
    environments = cliArguments.getEnvironment(sys)
    arguments = cliArguments.getArguments(sys)

    print("START PATCH PRODUCTS")
    for environment in environments:
        targetCon = loadEnv(environment)
        target = Akeneo(targetCon["host"], targetCon["clientId"], targetCon["secret"], targetCon["user"], targetCon["passwd"])
        migrationProductAttributeOptions.main(environment, target, arguments)
        
    print("FINISH PATCH PRODUCTS")

if __name__ == '__main__':
    main()

# Attributes
# openingHours_text to openingHours (optional)
# features zu amenityFeature - options change
# labels zu award - options change
# starRating - options change
# action_button_url zu target - copy
# action_button_text zu potentialAction - options change
# indoor_outdoor zu weatherDependency - options change
# accommodation_classification_garni zu garni
# accommodation_classification_superior zu superior
# servesCuisine - options change
# license - options change

# associations
# RECOMMEND zu Recommendation - copy
# MICE_ROOM zu MeetingRoom - copy