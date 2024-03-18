import json
import requests
from tabulate import tabulate
import os
import re
import modules.getProducto as GP
import modules.getGamas as GG

def GuardarProducto():
    producto = dict()
    while True:
        try:
            if not producto.get("codigo_producto"):
                codigo = input("Ingrese el codigo del prodcuto: ")
                if re.match(r'^[A-Z]{2}-\d{3}$', codigo) is not None:
                    if GP.getProductoCodigo(codigo):
                        raise Exception("El codigo ingresado ya existe.")
                    else:
                        producto["codigo_producto"] = codigo
                else:
                    raise Exception(f"El codigo no cumple con el estandar establecido ( ejm: XX-111 ).")
                
            if not producto.get("nombre"):
                nombre = input(f"Ingrese el nombre del producto: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', nombre) is not None:
                    producto["nombre"] = nombre
                else:
                    raise Exception("Nombre no valido, recuerde que todas las palabras deben iniciar con mayúsculas.")
                
            if not producto.get("gama"):
                gama = input("Ingrese la gama del producto: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s.]*$', nombre) is not None:
                    asd = GG.getAllNombre(gama)
                    if asd:
                        producto["gama"] = gama
                    else:
                        raise Exception("Gamas validas: ( Herbaceas, Herramientas, Aromáticas, Frutales, Ornamentales )")
                else:
                    raise Exception("Gamas validas: ( Herbaceas, Herramientas, Aromáticas, Frutales, Ornamentales )")
                
            if not producto.get("dimensiones"):
                dimensiones = input("Ingrese las dimensiones del producto: ")
                if re.match(r'^\d+-\d+$', dimensiones) is not None:
                    producto["dimensiones"] = dimensiones
                else:
                    raise Exception("Dimensiones no válidas, la forma correcta es ( numero-numero ).")
                
            if not producto.get("proveedor"): 
                proveedor = input("Ingrese el proveedor: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s.]*$', proveedor) is not None:
                    producto["proveedor"] = proveedor
                else:
                    raise Exception("Proveedor no valido, recuerde que la primera palabra debe iniciar con mayúsculas.")
                
            if not producto.get("descripcion"):
                descripcion = input("Ingrese una descripción: ")
                producto["descripcion"] = descripcion
            
            if not producto.get("cantidad_en_stock"):
                cantidad = input("Ingrese el precio de venta: ")
                if re.match(r'^[0-9]+$', cantidad) is not None:
                    cantidad = int(cantidad)
                    producto["cantidad_en_stock"] = cantidad
                else:
                    raise Exception("Cantidad no valida, asegurese de ingresar solo dígitos numéricos.")
                
            if not producto.get("precio_venta"):
                PrecioVenta = input("Ingrese el precio de venta: ")
                if re.match(r'^[0-9]+$', PrecioVenta) is not None:
                    PrecioVenta = int(PrecioVenta)
                    producto["cantidad_en_stock"] = PrecioVenta
                else:
                    raise Exception("Precio de venta no valido, asegurese de ingresar solo dígitos numéricos.")
                
            if not producto.get("precio_proveedor"):
                PrecioProveedor = input("Ingrese el precio del proveedor: ")
                if re.match(r'^[0-9]+$', PrecioProveedor) is not None:
                    PrecioProveedor = int(PrecioProveedor)
                    producto["precio_proveedor"] = PrecioProveedor
                    break
                else:
                    raise Exception("Precio de proveedor no valido, asegurese de ingresar solo dígitos numéricos.")
        
        except Exception as error:
            print(error)                     
    
    peticion = requests.post("http://192.168.1.6:5501", data=json.dumps(producto, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]

def DeleteProducto(id):
    data = GP.getgetProductoooCodigoasd(id)
    if len(data):
        peticion = requests.delete(f"http://192.168.1.6:5501/productos/{id}")
        if peticion.status_code == 204:
            data.append({"message":  "Producto eliminado correctamente"})
            return {
                "body": data,
                "status": peticion.status_code,
            }     
    else:
        return {
                "body":[{
                    "Mensaje": "Producto no encontrado.",
                    "id": id,
            }],
            "status": 400,
            }
    
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
2. Eliminar un producto.

0. Regresar                                                                                                    
 """)
        
        opcion = int(input((f"""

Seleccione una opción: """)))
        if opcion == 1:
                print(tabulate(GuardarProducto(), headers="keys", tablefmt="github"))
                input(f"""
Escriba una tecla para continuar: """)
            
        elif opcion == 2:
                idProducto = int(input("Ingrese el id del producto: "))
                print(tabulate(DeleteProducto(idProducto), headers="keys", tablefmt="github"))
                input(f"""
Escriba una tecla para continuar: """)
            
        
        elif opcion == 0:
                break
            
        else:
                print(f"Error: Seleccion no valida. ")
                input(f"Escriba una letra para regresar: ")
                
        
