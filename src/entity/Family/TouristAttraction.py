import entity.Family.Family as Family

def setBody(family, families):
    body = Family.setBody(family, families)

    body['attributes']['paymentAccepted'] = 'paymentAccepted'
    body['attributes']['currenciesAccepted'] = 'currenciesAccepted'

    return body