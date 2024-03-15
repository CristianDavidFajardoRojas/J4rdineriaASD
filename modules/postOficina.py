import json
import requests
from tabulate import tabulate
import os

def GuardarOficina():
    oficina = {
                "codigo_oficina": input("Ingrese el codigo de oficina: "),
                "ciudad": input("Ingrese la ciudad: "),
                "pais": input("Ingrese el pais: "),
                "region": input("Ingrese la region: "),
                "codigo_postal": input("Ingrese el codigo postal: "),
                "telefono": input("Ingrese el telefono: "),
                "linea_direccion1": input("Ingrese la direccion 1: "),
                "linea_direccion2": input("Ingrese la direccion 2: ")
                }
    peticion = requests.get("http://172.16.100.124:5004", data=json.dumps(oficina, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Oficina Guardado"
    return [res]

def menu():
    while True:
        os.system("clear")
        print(f"""
    ___       __          _       _      __                     ____  _____      _                 
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   / __ \/ __(_)____(_)___  ____ ______
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / / / / /_/ / ___/ / __ \/ __ `/ ___/
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / /_/ / __/ / /__/ / / / / /_/ (__  ) 
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/      \____/_/ /_/\___/_/_/ /_/\__,_/____/  
                                                                                                   



1. Guardar una oficina nueva.

0. Regresar                                                                                                    
 """)
        
        opcion = int(input((f"""

Seleccione una opción: """)))
        if opcion == 1:
            print(tabulate(GuardarOficina(), headers="keys", tablefmt="github"))
            input(f"""
Escriba una tecla para continuar: """)
            
        if opcion == 0:
            break