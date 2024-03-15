import json
import requests
from tabulate import tabulate
import os

def GuardarPago():
    pagos = {
                "codigo_cliente": int(input("Ingrese el codigo del cliente: ")),
                "forma_pago": input("Ingrese el metodo de pago: "),
                "id_transaccion": input("Ingrese el id de transaccion: "),
                "fecha_pago": input("Ingrese la fecha cuando realizo el pago ( ejm: año-mes-dia ): "),
                "total": int(input("Ingrese el total del pago: "))
                }
    peticion = requests.get("http://172.16.100.124:5005", data=json.dumps(pagos, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Pago Guardado"
    return [res]

def menu():
    while True:
        os.system("clear")
        print(f"""
    ___       __          _       _      __                     ____                        
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   / __ \____ _____ _____  _____
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / /_/ / __ `/ __ `/ __ \/ ___/
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / ____/ /_/ / /_/ / /_/ (__  ) 
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/     /_/    \__,_/\__, /\____/____/  
                                                                        /____/              



1. Guardar una pago nuevo.

0. Regresar                                                                                                    
 """)
        
        opcion = int(input((f"""

Seleccione una opción: """)))
        if opcion == 1:
            print(tabulate(GuardarPago(), headers="keys", tablefmt="github"))
            input(f"""
Escriba una tecla para continuar: """)
            
        if opcion == 0:
            break