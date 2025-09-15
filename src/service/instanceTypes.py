import importlib


def getInstanceTypes(target):
    print(" - LOAD InstanceTypes")
    types = {}
    
    if target.getHost() == "https://ziggy.contentdesk.io":
        print(" - LOAD InstanceTypes for ziggy")
        instanceModule = importlib.import_module("entity.Instance.ziggy")
    elif target.getHost() == "https://demo.contentdesk.io":
        print(" - LOAD InstanceTypes for demo")
        instanceModule = importlib.import_module("entity.Instance.demo")
    elif target.getHost() == "https://hlt.contentdesk.io":
        print(" - LOAD InstanceTypes for hlt")
        instanceModule = importlib.import_module("entity.Instance.hlt")
    elif target.getHost() == "https://sgbt.contentdesk.io":
        print(" - LOAD InstanceTypes for sgbt")
        instanceModule = importlib.import_module("entity.Instance.sgbt")
    else:
        print(" - LOAD InstanceTypes for default")
        instanceModule = importlib.import_module("entity.Instance.default")
    types = instanceModule.getTypes()

    return types