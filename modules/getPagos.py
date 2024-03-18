import json
import requests
from datetime import datetime
from tabulate import tabulate
import os
import modules.postPagos as PsPagos

#json-server storages/pago.json -b 5005
def dataPagos():
    peticion = requests.get("http://192.168.1.6:5005")
    data = peticion.json()
    return data

#json-server storages/cliente.json -b 5002
def dataClientes():
    peticion = requests.get("http://172.16.104.22:5002")
    data = peticion.json()
    return data

#json-server storages/empleados.json -b 5003
def dataEmpleados():
    peticion = requests.get("http://172.16.104.22:5003")
    data = peticion.json()
    return data

def getPagoCodigoasd(codigo):
    peticion = requests.get(f"http://192.168.1.6:5505/pagos/{codigo}")
    return [peticion.json()] if peticion.ok else []

def getIDTransac(id):
    for val in dataPagos():
        if val.get("id_transaccion") == id:
            return [val]

def getFormasPagoXd(Pago):
    for val in dataPagos():
        if val.get("forma_pago") == Pago:
            return [val]

def getAllPagos2008():
    Pagos2008SinRepetir = list()
    PagosRepetidos = set()
    for val in dataPagos():
        FechaPago = "/".join(val.get("fecha_pago").split("-")[::-1])
        start = datetime.strptime(FechaPago, "%d/%m/%Y")
        if start.year == 2008:
            if val.get("codigo_cliente") not in PagosRepetidos:
                Pagos2008SinRepetir.append(val)
                PagosRepetidos.add(val.get("codigo_cliente"))
    return Pagos2008SinRepetir
        
def getAllPaypal2008():
    Paypal2008 = list()
    for val in dataPagos():
        FechaPago = "/".join(val.get("fecha_pago").split("-")[::-1])
        start = datetime.strptime(FechaPago, "%d/%m/%Y")
        if start.year == 2008:
            Paypal2008.append(val)
    return Paypal2008

def getAllFormasDePago():
    FormaPago = list()
    FormaPagoRepetida = set()
    for val in dataPagos():
        if val.get("forma_pago") not in FormaPagoRepetida:
            FormaPago.append({"Formas De Pago:": val.get("forma_pago")})
            FormaPagoRepetida.add(val.get("forma_pago"))
    return FormaPago

def getAllNombreClientesYSuRepresentanteConPago():
    ListoNose = list()
    Repetidos = set()
    for val in dataClientes():
        for cris in dataEmpleados():
            for juan in dataPagos():
                if(juan.get("codigo_cliente") == val.get("codigo_cliente"))and(val.get("codigo_empleado_rep_ventas") == cris.get("codigo_empleado")):
                    if val.get("nombre_cliente") not in ListoNose:
                        ListoNose.append({
                        "Nombre Cliente": val.get("nombre_cliente"),
                        "Representante de ventas": f'{cris.get("nombre")} {cris.get("apellido1")}'
                    })
                        Repetidos.add(val.get("nombre_cliente"))
    return ListoNose

def getAllNombreClientesYSuRepresentantesSINPago():
    ListoNose = list()
    Repetidos = set()
    for val in dataClientes():
        for cris in dataEmpleados():
            for juan in dataPagos():
                if(juan.get("codigo_cliente") != val.get("codigo_cliente"))and(val.get("codigo_empleado_rep_ventas") == cris.get("codigo_empleado")):
                    ListoNose.append({
                        "Nombre Cliente": val.get("nombre_cliente"),
                    "Representante de ventas": f'{cris.get("nombre")} {cris.get("apellido1")}'
                    })
    return ListoNose

def menuPagos():
    while True:
        os.system("clear")
        print(f"""
    __  ___                        __        ____                        
   /  |/  /__  ____  __  __   ____/ /__     / __ \____ _____ _____  _____
  / /|_/ / _ \/ __ \/ / / /  / __  / _ \   / /_/ / __ `/ __ `/ __ \/ ___/
 / /  / /  __/ / / / /_/ /  / /_/ /  __/  / ____/ /_/ / /_/ / /_/ (__  ) 
/_/  /_/\___/_/ /_/\__,_/   \__,_/\___/  /_/    \__,_/\__, /\____/____/  
                                                     /____/              


1. Información de Pagos.
2. Administrar Pagos.
              
0. Regresar.
""")
        opcion = int(input((f"""

Seleccione una opción: """)))
        
        if opcion == 1:
            menu()

        if opcion == 2:
            PsPagos.menu()

        if opcion == 0:
            break

def menu():
    while True:
        os.system("clear")
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
4. Obtener clientes y su representante de los que tienen pago.
5. Obtener clientes y su representante de los que NO tienen pago.  

0. Regresar al menu principal.        
          """)
    
        opcion = int(input(f"""
                        
    Seleccione una de las opciones: """))
        
        if opcion == 1:
            print(tabulate(getAllPagos2008(), headers="keys", tablefmt="rounded_grid"))
            input(f"Escriba una tecla para continuar: ")

        if opcion == 2:
            print(tabulate(getAllPaypal2008(), headers="keys", tablefmt="rounded_grid"))
            input(f"Escriba una tecla para continuar: ")

        if opcion == 3:
            print(tabulate(getAllFormasDePago(), headers="keys", tablefmt="rounded_grid"))
            input(f"Escriba una tecla para continuar: ")

        if opcion == 4:
            print(tabulate(getAllNombreClientesYSuRepresentanteConPago(), headers="keys", tablefmt="rounded_grid"))
            input(f"Escriba una tecla para continuar: ")

        if opcion == 5:
            print(tabulate(getAllNombreClientesYSuRepresentantesSINPago(), headers="keys", tablefmt="rounded_grid"))
            input(f"Escriba una tecla para continuar: ")
            
        if opcion == 0:
            break
