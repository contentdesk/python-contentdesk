import importlib


def getInstanceAttributes(target):
    print(" - LOAD InstanceAttributes")
    print(" - Target: ", target)
    print(target.getHost())
    
    if target.getHost() == "https://ziggy.contentdesk.io":
        print(" - LOAD InstanceAttributes for ziggy")
        instanceModule = importlib.import_module("entity.Instance.ziggy")
    elif target.getHost() == "https://demo.contentdesk.io":
        print(" - LOAD InstanceAttributes for demo")
        instanceModule = importlib.import_module("entity.Instance.demo")
    elif target.getHost() == "https://hlt.pim.tso.ch":
        print(" - LOAD InstanceAttributes for hlt")
        instanceModule = importlib.import_module("entity.Instance.hlt")

    attributes = {}

    attributes = instanceModule.getProperties()
    
    return attributes