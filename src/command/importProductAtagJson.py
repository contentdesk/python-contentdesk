import json
import os
import uuid
from akeneo.akeneo import Akeneo
import sys
sys.path.append("..")

from service.loadEnv import loadEnv
import service.debug as debug
import service.cliArguments as cliArguments
import service.importProductAtagJson as importProductAtagJson

def main():
    environments = cliArguments.getEnvironment(sys)
    arguments = cliArguments.getArguments(sys)

    print("START Import PRODUCTS")
    for environment in environments:
        targetCon = loadEnv(environment)
        target = Akeneo(targetCon["host"], targetCon["clientId"], targetCon["secret"], targetCon["user"], targetCon["passwd"])
        importProductAtagJson.main(environment, target)
        
    print("FINISH Import PRODUCTS")
    
if __name__ == "__main__":
    main()