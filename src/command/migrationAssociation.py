import json
import requests
import pandas as pd
from akeneo.akeneo import Akeneo
import sys
sys.path.append("..")

from service.loadEnv import loadEnv
import service.debug as debug
import service.cliArguments as cliArguments
import service.migrationAssociaton as migrationAssociaton

def main():
    environments = cliArguments.getEnvironment(sys)
    arguments = cliArguments.getArguments(sys)

    print("START PATCH PRODUCTS")
    for environment in environments:
        targetCon = loadEnv(environment)
        target = Akeneo(targetCon["host"], targetCon["clientId"], targetCon["secret"], targetCon["user"], targetCon["passwd"])
        migrationAssociaton.main(environment, target, arguments)
        
    print("FINISH PATCH PRODUCTS")

if __name__ == '__main__':
    main()