import json
import requests
from tabulate import tabulate
import os
import re
import modules.getPedidos as GP
import modules.getClients as GC

def GuardarPedido():
    pedido = dict()
    while True:
        try:
            if not pedido.get("codigo_pedido"):
                codigo = input("Ingrese el codigo del pedido: ")
                if re.match(r'^[0-9]+$',codigo)is not None:
                    codigo = int(codigo)
                    asd = GP.getAllCodigoPedidos(codigo)
                    if asd:
                        raise Exception("El codigo del pedido ya existe.")
                    else:
                        pedido["codigo_pedido"] = codigo
                else:
                    raise Exception("Codigo no valido, recuerde ingresar solo digitos numéricos")
                
            if not pedido.get("fecha_pedido"):
                fecha_pedido = input("Ingrese la fecha del pedido: ")
                if re.match(r'^\d{4}-\d{2}-\d{2}$',fecha_pedido)is not None:
                    pedido["fecha_pedido"] = fecha_pedido
                else:
                    raise Exception("Fecha no valida, utilice el formato (Año-mes-dia) con digitos númericos.")

            if not pedido.get("fecha_esperada"):
                fecha_esperada = input("Ingrese la fecha estimada: ")
                if re.match(r'^\d{4}-\d{2}-\d{2}$',fecha_esperada)is not None:
                    pedido["fecha_esperada"] = fecha_esperada
                else:
                    raise Exception("Fecha no valida, utilice el formato (Año-mes-dia) con digitos númericos.")
            
            if not pedido.get("fecha_entrega"):
                fecha_entrega = input("Ingrese la fecha de entrega ( si no se ha realizado la entrega, escriba *None*): ")
                if fecha_entrega.strip().lower() == "none":
                    pedido["fecha_entrega"] = None
                elif re.match(r'^\d{4}-\d{2}-\d{2}$',fecha_entrega)is not None:
                    pedido["fecha_entrega"] = fecha_entrega
                else:
                    raise Exception("Fecha no valida, utilice el formato (Año-mes-dia) con digitos númericos.")

            if not pedido.get("estado"):
                estado = input("Ingrese el estado del pedido: ")
                if re.match(r'^[A-Z][a-z]*$',estado)is not None:
                    asd = GP.getAllEstadooo(estado)
                    if asd:
                        pedido["estado"] = estado
                    else:
                        raise Exception("Estados validos: ( Entregado / Rechazado / Pendiente )")
                else:
                    raise Exception("Estados validos: ( Entregado / Rechazado / Pendiente )")
                
            if not pedido.get("comentario"):
                comentario = input("Ingrese un comentario: ")
                if comentario.strip() == "":
                    pedido["comentario"] = None
                else:
                    pedido["comentario"] = comentario

            if not pedido.get("codigo_cliente"):
                codigo = input("Ingrese el codigo del cliente: ")
                if re.match(r'^[0-9]+$',codigo)is not None:
                    codigo = int(codigo)
                    asd = GC.getOneClienteCodigo(codigo)
                    if asd:
                        pedido["codigo_cliente"] = codigo
                        break
                    else:
                        raise Exception("El codigo del cliente no esta registrado.")
                else:
                    raise Exception("El codigo del cliente no esta registrado.")

        except Exception as error:
            print(error)
                
    peticion = requests.post("http://154.38.171.54:5007/pedidos", data=json.dumps(pedido, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Pedido Guardado"
    return [res]

def DeletePedido(id):
    data = GP.DeletePedidoasdasd(id)
    if len(data):
        peticion = requests.delete(f"http://154.38.171.54:5007/pedidos/{id}")
        if peticion.status_code == 204:
            data.append({"message":  "Pedido eliminado correctamente"})
            return {
                "body": data,
                "status": peticion.status_code,
            }     
    else:
        return {
                "body":[{
                    "Mensaje": "Pedido no encontrado.",
                    "id": id,
            }],
            "status": 400,
            }

def ModificarPedido(id):
    data = GP.DeletePedidoasdasd(id)
    if data is None:
            print(f"""

Id del pedido no encontrado. """)
    
    while True:
        try:
            print(tabulate(data, headers="keys", tablefmt="rounded_grid"))
            print(f"""
Datos para modificar: """)
            for i, (val, asd) in enumerate(data[0].items()):
                print(f"{i+1}. {val}")

            opcion = int(input(f"""
Seleccione una opción: """))
            datoModificar = list(data[0].keys())[opcion - 1]
            nuevoValor = input(f"""
Ingrese el nuevo valor para {datoModificar}: """)
            if datoModificar in data[0]:
                if datoModificar == "codigo_pedido" or "codigo_cliente":
                    data[0][datoModificar] = int(nuevoValor)
                    break
                else:
                    data[0][datoModificar] = nuevoValor
                    print(tabulate(data[0], headers="keys", tablefmt="rounded_grid"))
                    break
            else:
                 print(f"""
Seleccion incorrecta""")
                
        except ValueError as error:
            print(error)
    
    peticion = requests.put(f"http://154.38.171.54:5007/pedidos/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Pedido Modificado"
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
2. Eliminar un pedido.
3. Modificar pedido.

0. Regresar                                                                                                    
 """)
        
        opcion = int(input(f"""

Seleccione una opción: """))
        if opcion == 1:
            print(tabulate(GuardarPedido(), headers="keys", tablefmt="github"))
            input(f"""
Escriba una tecla para continuar: """)
            
        elif opcion == 2:
                idPedido = input("Ingrese el id del Pedido: ")
                print(tabulate(DeletePedido(idPedido), headers="keys", tablefmt="github"))
                input(f"""
Escriba una tecla para continuar: """)
                
        elif opcion == 3:
                idPedido = input("Ingrese el id del Pedido: ")
                print(tabulate(ModificarPedido(idPedido), headers="keys", tablefmt="github"))
                input(f"""
Escriba una tecla para continuar: """)


        if opcion == 0:
            break