import storages.pago as pag
from datetime import datetime
from tabulate import tabulate

def getAllPagos2008():
    Pagos2008SinRepetir = list()
    PagosRepetidos = set()
    for val in pag.pago:
        FechaPago = "/".join(val.get("fecha_pago").split("-")[::-1])
        start = datetime.strptime(FechaPago, "%d/%m/%Y")
        if start.year == 2008:
            if val.get("codigo_cliente") not in PagosRepetidos:
                Pagos2008SinRepetir.append(val)
                PagosRepetidos.add(val.get("codigo_cliente"))
    return Pagos2008SinRepetir
        
def getAllPaypal2008():
    Paypal2008 = list()
    for val in pag.pago:
        FechaPago = "/".join(val.get("fecha_pago").split("-")[::-1])
        start = datetime.strptime(FechaPago, "%d/%m/%Y")
        if start.year == 2008:
            Paypal2008.append(val)
    return Paypal2008

def getAllFormasDePago():
    FormaPago = list()
    FormaPagoRepetida = set()
    for val in pag.pago:
        if val.get("forma_pago") not in FormaPagoRepetida:
            FormaPago.append({"Formas De Pago:": val.get("forma_pago")})
            FormaPagoRepetida.add(val.get("forma_pago"))
    return FormaPago

def menu():
    while True:
        print(f"""
    ____                        __                   __        ____                        
   / __ \___  ____  ____  _____/ /____  _____   ____/ /__     / __ \____ _____ _____  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / /_/ / __ `/ __ `/ __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / ____/ /_/ / /_/ / /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/  /_/    \__,_/\__, /\____/____/  
          /_/                                                          /____/              
          
1. Obtener lista de pagos realizados en 2008.
2. Obtener lista de pagos realizados por medio de "Paypal".
3. Obtener lista de formas de pago.          
          """)
    
        opcion = int(input(f"""
                        
    Seleccione una de las opciones: """))
        
        if opcion == 1:
            print(tabulate(getAllPagos2008(), headers="keys", tablefmt="rounded_grid"))

        if opcion == 2:
            print(tabulate(getAllPaypal2008(), headers="keys", tablefmt="rounded_grid"))

        if opcion == 3:
            print(tabulate(getAllFormasDePago(), headers="keys", tablefmt="rounded_grid"))
            
        if opcion == 0:
            break
