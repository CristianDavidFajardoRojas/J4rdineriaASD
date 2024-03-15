import json
import requests
from tabulate import tabulate
import os

def GuardarPedido():
    pedido = {
                "codigo_pedido": int(input("Ingrese el codigo del pedido: ")),
                "fecha_pedido": input("Ingrese la fecha cuando realizo el pedido ( ejm: año-mes-dia ): "),
                "fecha_esperada": input("Ingrese la fecha estimada de entrega ( ejm: año-mes-dia ): "),
                "fecha_entrega": input("Ingrese la fecha de entrega ( ejm: año-mes-dia ): "),
                "estado": input("Ingrese el estado del pedido ( Entregado/ Pendiente / Rechazado ): "),
                "comentario": input(" Ingrese el comentario del cliente: "),
                "codigo_cliente": int(input("Ingrese el codigo del cliente: "))
                }
    peticion = requests.get("http://172.16.100.124:5006", data=json.dumps(pedido, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Pedido Guardado"
    return [res]

def menu():
    while True:
        os.system("clear")
        print(f"""
    ___       __          _       _      __                     ____           ___     __          
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   / __ \___  ____/ (_)___/ /___  _____
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / /_/ / _ \/ __  / / __  / __ \/ ___/
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / ____/  __/ /_/ / / /_/ / /_/ (__  ) 
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/     /_/    \___/\__,_/_/\__,_/\____/____/  
                                                                                                   

1. Guardar un producto nuevo.

0. Regresar                                                                                                    
 """)
        
        opcion = int(input(f"""

Seleccione una opción: """))
        if opcion == 1:
            print(tabulate(GuardarPedido(), headers="keys", tablefmt="github"))
            
        if opcion == 0:
            break