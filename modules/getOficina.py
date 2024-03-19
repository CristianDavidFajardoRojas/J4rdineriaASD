import json
import requests
from tabulate import tabulate
import keyboard
import modules.postOficina as PsOficina
import os

#json-server storages/oficina.json -b 5004
def dataOficinas():
    peticion = requests.get("http://154.38.171.54:5005/oficinas")
    data = peticion.json()
    return data

def DeleteOficinaHahaDoges(id):
    peticion = requests.get(f"http://154.38.171.54:5005/oficinas/{id}")
    return [peticion.json()] if peticion.ok else []

def getOficinaCodigoasd(codigo):
    peticion = requests.get(f"http://154.38.171.54:5005/oficinas/{codigo}")
    return [peticion.json()] if peticion.ok else []

def getCodigoOficina(codigo):
    for val in dataOficinas():
        if val.get("codigo_oficina") == codigo:
            return [val]

def getAllCodigoCiudad():
    codigoCiudad = []
    for val in dataOficinas():
        codigoCiudad.append({
            "codigo": val.get("codigo_oficina"),
            "ciudad": val.get("ciudad")
        })
    return codigoCiudad

def getAllCiudadTelefono(pais):
    ciudadTelefono = []
    for val in dataOficinas():
        if (val.get("pais") == pais):
            ciudadTelefono.append({
                "ciudad": val.get("ciudad"),
                "telefono": val.get("telefono"),
                "oficinas" : val.get("codigo_oficina"),
                "pais" : val.get("pais") 
            })
    return ciudadTelefono

def getAllDirecciones():
    Direcciones = list()
    for val in dataOficinas():
        Direcciones.append({
            "Codigo Oficina": val.get("codigo_oficina"),
            "Pais": val.get("pais"),
            "Ciudad": val.get("ciudad"),
            "Direccion": f'{val.get("linea_direccion1")},{val.get("linea_direccion2")}'
        })
    return Direcciones

def menuOficinas():
    while True:
        os.system("clear")
        print(f"""
    __  ___                        __        ____  _____      _                 
   /  |/  /__  ____  __  __   ____/ /__     / __ \/ __(_)____(_)___  ____ ______
  / /|_/ / _ \/ __ \/ / / /  / __  / _ \   / / / / /_/ / ___/ / __ \/ __ `/ ___/
 / /  / /  __/ / / / /_/ /  / /_/ /  __/  / /_/ / __/ / /__/ / / / / /_/ (__  ) 
/_/  /_/\___/_/ /_/\__,_/   \__,_/\___/   \____/_/ /_/\___/_/_/ /_/\__,_/____/  
                                                                                

1. Información de oficinas.
2. Administrar oficinas.
              
0. Regresar.
""")
        opcion = int(input((f"""

Seleccione una opción: """)))
        
        if opcion == 1:
            menu()

        if opcion == 2:
            PsOficina.menu()

        if opcion == 0:
            break

def menu():
    while True:
        os.system("clear")
        print(f"""
    ____                        __                   __        ____  _____      _                 
   / __ \___  ____  ____  _____/ /____  _____   ____/ /__     / __ \/ __(_)____(_)___  ____ ______
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / / / / /_/ / ___/ / __ \/ __ `/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / /_/ / __/ / /__/ / / / / /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/   \____/_/ /_/\___/_/_/ /_/\__,_/____/  
          /_/                                                                                     
          
          
1. Obtener el codigo de la oficina y su ciudad.
2. Obtener información según el pais.
3. Obtener las direcciones de las oficinas.
              
0. Regresar al menu principal.
""")
    
        opcion = int(input(f"""
                        
    Seleccione una de las opciones: """))
        
        if opcion == 1:
            print(tabulate(getAllCodigoCiudad(), headers="keys", tablefmt="rounded_grid"))
            input(f"Escriba una tecla para continuar: ")

        if opcion == 2:
            paais = input(f"""
    Ingrese el pais: """)
            print(tabulate(getAllCiudadTelefono(paais), headers="keys", tablefmt="rounded_grid"))
            input(f"Escriba una tecla para continuar: ")

        if opcion == 3:
            print(tabulate(getAllDirecciones(), headers="keys", tablefmt="rounded_grid"))
            input(f"Escriba una tecla para continuar: ")
            
        if opcion == 0:
            break