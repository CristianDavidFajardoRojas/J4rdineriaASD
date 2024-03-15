import json
import requests
from tabulate import tabulate
import os
import modules.postEmpleados as PsEmpleados

#json-server storages/empleados.json -b 5003
def dataEmpleados():
    peticion = requests.get("http://172.16.104.22:5003")
    data = peticion.json()
    return data

def getAllNombreApellidoEmailJefe(codigo):
    NombreApellidoEmail = []
    for val in dataEmpleados():
        if val.get("codigo_jefe") == codigo:
            NombreApellidoEmail.append(
                {
                    "nombre":val.get("nombre"),
                    "apellidos":f'{val.get("apellido1")}{val.get("apellido2")}',
                    "email":val.get("email"),
                    "jefe":val.get("codigo_jefe")
                }
            )
    return NombreApellidoEmail

def getAllPuestoNombreApellidosEmailJefe():
    DatosJefe = list()
    for val in dataEmpleados():
        if val.get("codigo_jefe") == None:
            DatosJefe.append({
                "Puesto":val.get("puesto"),
                "Nombre":val.get("nombre"),
                "Apellido": val.get("apellido1"),
                "Email": val.get("email")
            })
    return DatosJefe

def getAllNombreApellidosPuestoNoRepVentas():
    InfoNoRepVentas = list()
    for val in dataEmpleados():
        if val.get("puesto") != "Representante Ventas":
            InfoNoRepVentas.append({
                "Puesto":val.get("puesto"),
                "Nombre":val.get("nombre"),
                "Apellido": val.get("apellido1"),
            })
    return InfoNoRepVentas

def menuEmpleados():
    while True:
        os.system("clear")
        print(f"""
    __  ___                        __                             __           __            
   /  |/  /__  ____  __  __   ____/ /__     ____  _________  ____/ /_  _______/ /_____  _____
  / /|_/ / _ \/ __ \/ / / /  / __  / _ \   / __ \/ ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/
 / /  / /  __/ / / / /_/ /  / /_/ /  __/  / /_/ / /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  ) 
/_/  /_/\___/_/ /_/\__,_/   \__,_/\___/  / .___/_/   \____/\__,_/\__,_/\___/\__/\____/____/  
                                        /_/                                                  

1. Información de Empleados.
2. Administrar Empleados
              
0. Regresar.
""")
        opcion = int(input((f"""

Seleccione una opción: """)))
        
        if opcion == 1:
            menu()

        if opcion == 2:
            PsEmpleados.menu()

        if opcion == 0:
            break

def menu():
    while True:
        os.system("clear")
        print(f"""
          
    ____                        __                                    __               __          
   / __ \___  ____  ____  _____/ /____  _____   ___  ____ ___  ____  / /__  ____ _____/ /___  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / _ \/ __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  /  __/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \___/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/  
          /_/                                              /_/                                     


1. Obtener información con el codigo jefe.
2. Obtener información del director general.
3. Obtener nombres de los empleados que no son representates de ventas.

0. Regresar al menu principal.
""")
        opcion = int(input(f"""

Seleccione una de las opciones: """))
        if opcion == 1:
            codigojefe = int(input(f"""
                            
Ingrese el codigo de jefe: """))
            print(tabulate(getAllNombreApellidoEmailJefe(codigojefe), headers="keys", tablefmt="rounded_grid"))
            input(f"Escriba una tecla para continuar: ")

        if opcion == 2:
            print(tabulate(getAllPuestoNombreApellidosEmailJefe(), headers="keys", tablefmt="rounded_grid"))
            input(f"Escriba una tecla para continuar: ")

        if opcion == 3:
            print(tabulate(getAllNombreApellidosPuestoNoRepVentas(), headers="keys", tablefmt="rounded_grid"))
            input(f"Escriba una tecla para continuar: ")
            
        if opcion == 0:
            break