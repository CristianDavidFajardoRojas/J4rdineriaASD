import json
import requests
from tabulate import tabulate
import os
import modules.getClients as GC
import re
import modules.getPagos as GP

def GuardarPago():
    pagos = dict()
    while True:
        try:
            if not pagos.get("codigo_cliente"):
                codigo =  input("Ingrese el codigo del cliente: ")
                if re.match(r'^[0-9]+$', codigo) is not None:
                    codigo =int(codigo)
                    XDXDXDXDXD = GC.getOneClienteCodigo(codigo)
                    if XDXDXDXDXD:
                        pagos["codigo_cliente"] = codigo
                    else:
                        raise Exception("Codigo cliente no encontrado.")
                else:
                    raise Exception("Codigo no valido, asegurese que de ingresar solo digitos numéricos.")
                
            if not pagos.get("forma_pago"):
                forma_pago = input("Ingrese el metodo de pago: ")
                if re.match(r'^[A-Z][a-zA-Z0-9-\s]*$', forma_pago) is not None:
                    asdasd = GP.getFormasPagoXd(forma_pago)
                    if asdasd:
                        pagos["forma_pago"] = forma_pago
                    else:
                        raise Exception("Formas de pago validas: ( PayPal / Transferencia / Cheque )")
                else:
                    raise Exception("Formas de pago validas: ( PayPal / Transferencia / Cheque )")
                
            if not pagos.get("id_transaccion"):
                id_transaccion = input("Ingrese el ID de transaccion: ")
                if re.match(r'^[a-zA-Z]{2}-[a-zA-Z]{3}-\d{6}$', id_transaccion) is not None:
                    lololol = GP.getIDTransac(id_transaccion)
                    if lololol:
                        raise Exception("El ID de transaccion ya existe.")
                    else:
                        pagos["id_transaccion"] = id_transaccion
                else:
                    raise Exception("ID no valido, porfavor siga el siguiente formato ( ejm: ak-std-000026 )")

            if not pagos.get("fecha_pago"):
                fecha_pago = input("Ingrese la fecha del pedido: ")
                if re.match(r'^\d{4}-\d{2}-\d{2}$',fecha_pago)is not None:
                    pagos["fecha_pago"] = fecha_pago
                else:
                    raise Exception("Fecha no valida, utilice el formato (Año-mes-dia) con digitos númericos.")

            if not pagos.get("total"):
                total = input("Ingrese el total del pago: ")
                if re.match(r'^[0-9]+$', total) is not None:
                    total = int(total)
                    pagos["total"] = total
                    break
                else:
                    raise Exception("Total no valido, asegurese de ingresar solo digitos numericos.")

        except Exception as error:
            print(error)
                
    peticion = requests.post("http://192.168.1.6:5005", data=json.dumps(pagos, indent=4).encode("UTF-8"))
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