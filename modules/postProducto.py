import json
import requests
from tabulate import tabulate
import os

def GuardarProducto():
    producto = {
                "codigo_producto": input("Ingrese el codigo del prodcuto: "),
                "nombre": input("Ingrese el nombre del prodcuto: "),
                "gama": input("Ingrese la gama del producto: "),
                "dimensiones": input("Ingrese las dimensiones del producto: "),
                "proveedor": input("Ingrese el proveedor del producto: "),
                "descripcion": input("Ingrese una descripción: "), 
                "cantidad_en_stock": input("Ingrese la cantidad en stock: "),
                "precio_venta": input("Ingrese el precio de venta: "),
                "precio_proveedor": input("Ingrese el precio del proveedor: ")
                }
    peticion = requests.get("http://172.16.100.124:5501", data=json.dumps(producto, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]

def menu():
    while True:
        os.system("clear")
        print(f"""
    ___       __          _       _      __                     ____                 __           __            
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   / __ \_________  ____/ /_  _______/ /_____  _____
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / /_/ / ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / ____/ /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  ) 
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/     /_/   /_/   \____/\__,_/\__,_/\___/\__/\____/____/  


1. Guardar un producto nuevo.

0. Regresar                                                                                                    
 """)
        
        opcion = (f""""

Seleccione una opción: """)
        if opcion == 1:
            print(tabulate(GuardarProducto(), headers="keys", tablefmt="github"))
            input(f"""
Escriba una tecla para continuar: """)
            
        if opcion == 0:
            break

