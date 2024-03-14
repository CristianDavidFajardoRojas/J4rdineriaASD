from tabulate import tabulate
import json
import requests
import modules.postProducto as psProducto


#json-server storage/producto.json -b 5501
def getAllData():
    peticion = requests.get("http://172.16.100.124:5501")
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
        condiciones[i] = {
                "codigo": val.get("codigo_producto"),
                "venta": val.get("precio_venta"),
                "nombre": val.get("nombre"),
                "gama": val.get("gama"),
                "dimensiones": val.get("dimensiones"),
                "proveedor": val.get("proveedor"),
                "descripcion": f'{val.get("descripcion")[:5]}...' if condiciones[i].get("descripcion") else None,
                "stock": val.get("cantidad_en_stock"),
                "base": val.get("precio_proveedor")
            }
    return condiciones  
    
def menu():
    while True:
        print(f"""
    ____                 __           __            
   / __ \_________  ____/ /_  _______/ /_____  _____
  / /_/ / ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/
 / ____/ /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  ) 
/_/   /_/   \____/\__,_/\__,_/\___/\__/\____/____/                                                                                                   
          
1. Obtener todos los productos por gama y cantidad minima en stock ordenado de mayor a menor.
              
0. Regresar al menu principal.
""")
    
        opcion = int(input(f"""
Seleccione una de las opciones: """))
    
        if opcion == 1:
            gamaa = input("Ingrese la gama del producto: ")
            stoock = int(input("Ingrese cantidad minima en stock a revisar: "))
            print(tabulate(getAllStocksPriceGama(gamaa, stoock), headers="keys", tablefmt="rounded_grid"))
        
        if opcion == 0:
            break

def menuProductos():
    while True:
        print(f"""
    __  ___                        __                             __           __            
   /  |/  /__  ____  __  __   ____/ /__     ____  _________  ____/ /_  _______/ /_____  _____
  / /|_/ / _ \/ __ \/ / / /  / __  / _ \   / __ \/ ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/
 / /  / /  __/ / / / /_/ /  / /_/ /  __/  / /_/ / /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  ) 
/_/  /_/\___/_/ /_/\__,_/   \__,_/\___/  / .___/_/   \____/\__,_/\__,_/\___/\__/\____/____/  
                                        /_/                                                  

1. Información de productos.
2. Administrar productos
              
0. Regresar.
""")
        opcion = int(input((f"""

Seleccione una opción: """)))
        
        if opcion == 1:
            menu()

        if opcion == 2:
            psProducto.menu()

        if opcion == 0:
            break

