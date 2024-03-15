import json
import requests
from tabulate import tabulate
import os

def GuardarEmpleado():
    empleado = {
                "codigo_empleado": int(input(f"Ingrese el codigo del empleado: ")),
                "nombre": input(f"Ingrese el nombre del empleado: "),
                "apellido1": input(f"Ingrese el primer apellido: "),
                "apellido2": input(f"Ingrese el segundo apellido: "),
                "extension": input(f"Ingrese la extension del empleado: "),
                "email": input(f"Ingrese el email del empleado: "),
                "codigo_oficina": input(f"Ingrese el codigo de la oficina: "),
                "codigo_jefe": int(input(f"Ingrese el codigo del jefe: ")),
                "puesto": input(f"Ingrese el puesto del empleado: ")
                }
    peticion = requests.get("http://172.16.100.124:5003", data=json.dumps(empleado, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Empleado Guardado"
    return [res]

def menu():
    while True:
        os.system("clear")
        print(f"""
    ___       __          _       _      __                     ______                __               __          
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   / ____/___ ___  ____  / /__  ____ _____/ /___  _____
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / __/ / __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / /___/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  ) 
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/     /_____/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/  
                                                                           /_/                                     
          
1. Guardar un nuevo empleado.
          
0. Regresar.
          """)
        opcion = int(input(f"""

Seleccione una opciòn: """))
        
        if opcion==1:
            print(tabulate(GuardarEmpleado(), headers="keys", tablefmt="github"))
            input(f"""
Escriba una tecla para continuar: """)

        elif opcion ==0:
            break