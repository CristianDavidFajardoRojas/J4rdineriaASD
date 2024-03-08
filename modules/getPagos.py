import storages.pago as pag
from datetime import datetime

def getAllPaypal2008():
    Paypal2008 = list()
    for val in pag.pago:
        FechaPago = "/".join(val.get("fecha_pago").split("-")[::-1])
        start = datetime.strptime(FechaPago, "%d/%m/%Y")
        if start.year == 2008:
            Paypal2008.append(val)
    return Paypal2008
