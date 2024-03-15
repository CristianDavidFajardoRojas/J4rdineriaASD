import json
import requests
from tabulate import tabulate
import os

def GuardarClientes():
    Cliente = {
        "codigo_cliente": int(input(f"Escriba el codigo del cliente: ")),
        "nombre_cliente": input(f"Escriba el nombre del cliente: "),
        "nombre_contacto": input(f"Escriba el nombre del contacto: "),
        "apellido_contacto": input(f"Escriba el apellido del contacto: "),
        "telefono": input(f"Escriba el numero de telefono: "),
        "fax": input(f"Escriba el fax: "),
        "linea_direccion1": input(f"Escriba la linea de direccion 1: "),
        "linea_direccion2": input(f"Escriba la linea de direccion 2: "),
        "ciudad": input(f"Escriba la ciudad: "),
        "region": input(f"Escriba la region: "),
        "pais": input(f"Escriba el pais: "),
        "codigo_postal": input(f"Escriba el codigo postal: "),
        "codigo_empleado_rep_ventas": int(input(f"Escriba el codigo del representante de ventas: ")),
        "limite_credito": float(input(f"Escriba el limite de credito: "))
    }
    peticion = requests.get("http://172.16.100.124:5002", data=json.dumps(Cliente, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Cliente Guardado"
    return [res]

def menu():
    while True:
        os.system("clear")
        print(f"""
    ___       __          _       _      __                _________            __           
   /   | ____/ /___ ___  (_)___  (_)____/ /_____ ______   / ____/ (_)__  ____  / /____  _____
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ __ `/ ___/  / /   / / / _ \/ __ \/ __/ _ \/ ___/
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /_/ / /     / /___/ / /  __/ / / / /_/  __(__  ) 
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/\__,_/_/      \____/_/_/\___/_/ /_/\__/\___/____/  

1. Guardar un cliente nuevo.

0. Regresar
""")
        opcion = int(input(f"""
                       
Seleccione una opción: """))
    
        if opcion == 1:
            GuardarClientes()
        if opcion == 0:
            break