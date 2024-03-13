from tabulate import tabulate
import json
import requests
import modules.postProducto as psProducto
import modules.getGamas as gG

#json-server storage/producto.json -b 5501
def getAllData():
    peticion = requests.get("http://172.16.100.124:5001")
    data = peticion.json()
    return data

#Ejercicio Teacher
def getAllStocksPriceGama(gama, stock):
    condiciones = list()
    for val in getAllData():
        if val.get("gama") == gama and val.get("cantidad_en_stock") >= stock:
            condiciones.append(val)
            
    def price(val):
        return val.get("precio_venta")
    condiciones.sort(key=price, reverse = True)
    for i, val in enumerate(condiciones):
        if(condiciones[i].get("descripcion")):
            condiciones[i]["descripcion"] = f'{condiciones[i]["descripcion"][:5]}...'
    return condiciones  
    
def menu():
    while True:
        print(f"""
    ____                        __                   __        ____                 __           __            
   / __ \___  ____  ____  _____/ /____  _____   ____/ /__     / __ \_________  ____/ /_  _______/ /_____  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / /_/ / ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / ____/ /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/  /_/   /_/   \____/\__,_/\__,_/\___/\__/\____/____/  
          /_/                                                                                                  
          
1. Obtener todos los productos por gama y cantidad minima en stock ordenado de mayor a menor.
2. Guardar.
              
0. Regresar al menu principal.
""")
    
        opcion = int(input(f"""
Seleccione una de las opciones: """))
    
        if opcion == 1:
            gamaa = input("Ingrese la gama del producto: ")
            stoock = int(input("Ingrese cantidad minima en stock a revisar: "))
            print(tabulate(getAllStocksPriceGama(gamaa, stoock), headers="keys", tablefmt="rounded_grid"))
        if opcion ==2:
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
            psProducto.postProducto(producto)
            print(producto)
        
        if opcion == 0:
            break