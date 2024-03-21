import json
import requests
from tabulate import tabulate
import os
import modules.getClients as GC
import re

def GuardarClientes():
    cliente = dict()
    while True:
        try:
            if not cliente.get("codigo_cliente"):
                codigo = input(f"Escriba el codigo del cliente: ")
                if re.match(r'^[0-9]+$', codigo) is not None:
                    codigo = int(codigo)
                    if GC.getOneClienteCodigo(codigo):
                        raise Exception("El codigo del cliente ya existe.")
                    else:
                        cliente["codigo_cliente"] = codigo
                else:
                    raise Exception("Codigo ingresado no valido, asegurese de ingresar solo dígitos numéricos")
                
            if not cliente.get("nombre_cliente"):
                nombre = input(f"Ingrese el nombre del cliente: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', nombre) is not None:
                    cliente["nombre_cliente"] = nombre
                else:
                    raise Exception("Nombre no valido, recuerde que todas las palabras deben iniciar con mayúsculas.")
                
            if not cliente.get("nombre_contacto"):
                nombreContacto = input(f"Ingrese el nombre contacto del cliente: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', nombreContacto) is not None:
                    cliente["nombre_contacto"] = nombreContacto
                else:
                    raise Exception("Nombre del contacto no valido, recuerde que todas las palabras deben iniciar con mayúsculas.")

            if not cliente.get("apellido_contacto"):
                ApellidoContacto = input(f"Ingrese el apellido contacto del cliente: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', ApellidoContacto) is not None:
                    cliente["apellido_contacto"] = ApellidoContacto
                else:
                    raise Exception("Apellido del contacto no valido, recuerde que todas las palabras deben iniciar con mayúsculas.")
                
            if not cliente.get("telefono"):
                telefono = input("Ingrese el número de telefono: ")
                if re.match(r'^\d{1,3} ?\d{4}-?\d{4}$', telefono) is not None:
                    if GC.getAllTelefono(telefono):
                        raise Exception("El telefono ingresado ya existe.")
                    else:
                        cliente["telefono"] = telefono
                else:
                    raise Exception("Telefono no valido ( ejm: 654352981 o 2 8005-7162 )")
                
            if not cliente.get("fax"):
                fax = input("Ingrese el Fax: ")
                if re.match(r'^\d{1,3} ?\d{4}-?\d{4}$', fax) is not None:
                    cliente["fax"] = fax
                else:
                    raise Exception("Fax no valido ( ejm: 654352981 o 2 8005-7162 )")
                
            if not cliente.get("linea_direccion1"):
                linea_direccion1 = input(f"Ingrese la linea de direccion 1: ")
                cliente["linea_direccion1"] = linea_direccion1

            if not cliente.get("linea_direccion2"):
                linea_direccion2 = input(f"Ingrese la linea de direccion 2: ")
                cliente["linea_direccion2"] = linea_direccion2

            if not cliente.get("ciudad"):
                ciudad = input(f"Ingrese la ciudad: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', ciudad) is not None:
                    cliente["ciudad"] = ciudad
                else:
                    raise Exception("Ciudad no valida, recuerde que todas las palabras deben iniciar con mayúsculas.")
                
            if not cliente.get("region"):
                region = input(f"Ingrese la Region: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', region) is not None:
                    cliente["region"] = region
                else:
                    raise Exception("Region no valida, recuerde que todas las palabras deben iniciar con mayúsculas.")
                
            if not cliente.get("pais"):
                pais = input(f"Ingrese el pais: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', pais) is not None:
                    cliente["pais"] = pais
                else:
                    raise Exception("Pais no valida, recuerde que todas las palabras deben iniciar con mayúsculas.")
                
            if not cliente.get("codigo_postal"):
                codigo_postal = input("Ingrese el Codigo postal: ")
                if re.match(r'^\d{4,5}$', codigo_postal) is not None:
                    cliente["codigo_postal"] = codigo_postal
                else:
                    raise Exception("Codigo postal no valido, asegurese de ingresar 4 o 5 dígitos numéricos")
                
            if not cliente.get("codigo_empleado_rep_ventas"):
                codigo_empleado_rep_ventas = input(f"Escriba el codigo del representante de ventas: ")
                if re.match(r'^[0-9]+$', codigo_empleado_rep_ventas) is not None:
                    codigo_empleado_rep_ventas = int(codigo_empleado_rep_ventas)
                    cliente["codigo_empleado_rep_ventas"] = codigo_empleado_rep_ventas
                else:
                    raise Exception("Codigo ingresado no valido, asegurese de ingresar solo dígitos numéricos")
                
            if not cliente.get("limite_credito"):
                limite_credito = input(f"Escriba el limite de credito: ")
                if re.match(r'^[0-9]+$', limite_credito) is not None:
                    limite_credito = float(limite_credito)
                    cliente["limite_credito"] = limite_credito
                    break
                else:
                    raise Exception("Limite de credito ingresado no valido, asegurese de ingresar solo dígitos numéricos")
                                   
        except Exception as error:
            print(error)

    peticion = requests.post("http://154.38.171.54:5001/cliente", data=json.dumps(cliente, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Cliente Guardado"
    return [res]

def DeleteClientes(id):
    data = GC.DeleteClienteCodigoasd(id)
    if len(data):
        peticion = requests.delete(f"http://154.38.171.54:5001/cliente/{id}")
        if peticion.status_code == 204:
            data.append({"message":  "Cliente eliminado correctamente"})
            return {
                "body": data,
                "status": peticion.status_code,
            }     
    else:
        return {
                "body":[{
                    "Mensaje": "Cliente no encontrado.",
                    "id": id,
            }],
            "status": 400,
            }

def ModificarCliente(id):
    data = data = GC.DeleteClienteCodigoasd(id)
    if data is None:
            print(f"""

Id del Cliente no encontrado. """)
    
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
                if data[0][datoModificar] == data[0]["codigo_cliente"] or data[0][datoModificar] == data[0]["limite_credito"] or data[0][datoModificar]== data[0]["codigo_empleado_rep_ventas"]:
                    data[0][datoModificar] = int(nuevoValor)
                else:
                    data[0][datoModificar] = nuevoValor
                break
            else:
                 print(f"""
Seleccion incorrecta""")
                
        except ValueError as error:
            print(error)
    
    peticion = requests.put(f"http://154.38.171.54:5001/cliente/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Cliente Modificado"
    return [res]

def menu():
    while True:
        os.system("clear")
        print(f"""

    ___       __          _       _      __                     _________            __           
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   / ____/ (_)__  ____  / /____  _____
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / /   / / / _ \/ __ \/ __/ _ \/ ___/
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / /___/ / /  __/ / / / /_/  __(__  ) 
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/      \____/_/_/\___/_/ /_/\__/\___/____/  
                                                                                                  


1. Guardar un cliente nuevo.
2. Eliminar un cliente.
3. Modificar un cliente.
              
0. Regresar
""")
        opcion = int(input(f"""
                       
Seleccione una opción: """))
    
        if opcion == 1:
            print(tabulate(GuardarClientes(), headers="keys", tablefmt="github"))
            input(f"""
Escriba una tecla para continuar: """)
            
        elif opcion == 2:
                idCliente = input("Ingrese el id del cliente: ")
                print(tabulate(DeleteClientes(idCliente), headers="keys", tablefmt="github"))
                input(f"""
Escriba una tecla para continuar: """)
                
        elif opcion == 3:
                idEmpleado = input("Ingrese el id del Empleado: ")
                print(tabulate(ModificarCliente(idEmpleado), headers="keys", tablefmt="github"))
                input(f"""
Escriba una tecla para continuar: """)

        if opcion == 0:
            break