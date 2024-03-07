import storages.pago as pag
from datetime import datetime

def getAll2008Paypal():
    PagosPaypal2008 = list()
    for val in pag.pago:
        FechaPagoo = "/".join(val.get("fecha_pago").split("-")[::-1])
        start = datetime.strptime(FechaPagoo, "%d/%m/%Y")
        if (val.get("forma_pago") == "Paypal") and start.month == 2008:
            PagosPaypal2008.append(val)
    return PagosPaypal2008
    
