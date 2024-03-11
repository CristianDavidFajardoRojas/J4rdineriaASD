import storages.oficina as of
from tabulate import tabulate
import keyboard

def getAllCodigoCiudad():
    codigoCiudad = []
    for val in of.oficina:
        codigoCiudad.append({
            "codigo": val.get("codigo_oficina"),
            "ciudad": val.get("ciudad")
        })
    return codigoCiudad

def getAllCiudadTelefono(pais):
    ciudadTelefono = []
    for val in of.oficina:
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
    for val in of.oficina:
        Direcciones.append({
            "Codigo Oficina": val.get("codigo_oficina"),
            "Pais": val.get("pais"),
            "Ciudad": val.get("ciudad"),
            "Direccion": f'{val.get("linea_direccion1")},{val.get("linea_direccion2")}'
        })
    return Direcciones

def menu():
    while True:
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
""")
    
        opcion = int(input(f"""
                        
    Seleccione una de las opciones: """))
        
        if opcion == 1:
            print(tabulate(getAllCodigoCiudad(), headers="keys", tablefmt="rounded_grid"))

        if opcion == 2:
            paais = input(f"""
    Ingrese el pais: """)
            if keyboard.is_pressed('ctrl') and keyboard.is_pressed('c'):
                print("Se presionó Ctrl + C. Saliendo del bucle.")
                break
            print(tabulate(getAllCiudadTelefono(paais), headers="keys", tablefmt="rounded_grid"))

        if opcion == 3:
            print(tabulate(getAllDirecciones(), headers="keys", tablefmt="rounded_grid"))
            
        if opcion == 0:
            break