import json
import requests
from tabulate import tabulate
import os
import re
import modules.getEmpleados as GE

def GuardarEmpleado():
    empleado = dict()
    while True:
        try:
            if not empleado.get("codigo_empleado"):
                codigo = input("Ingrese el codigo del empleado: ")
                if re.match(r'^[0-9]+$', codigo) is not None:
                    codigo = int(codigo)
                    xd = GE.getEmpleadoCodigo(codigo)
                    if xd:
                        raise Exception("El codigo ingresado ya existe.")
                    else:
                        empleado["codigo_empleado"] = codigo
                else:
                    raise Exception(f"El codigo no cumple con el estandar establecido.")
            
            if not empleado.get("nombre"):
                nombre = input(f"Ingrese el nombre del empleado: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', nombre) is not None:
                    empleado["nombre"] = nombre
                else:
                    raise Exception("Nombre no valido, recuerde que todas las palabras deben iniciar con mayúsculas.")
                
            if not empleado.get("apellido1"):
                apellido1 = input(f"Ingrese el apellido 1 del empleado: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', apellido1) is not None:
                    empleado["apellido1"] = apellido1
                else:
                    raise Exception("Apellido no valido, recuerde que todas las palabras deben iniciar con mayúsculas.")

            if not empleado.get("apellido2"):
                apellido2 = input(f"Ingrese el apellido 2 del empleado: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', apellido2) is not None:
                    empleado["apellido2"] = apellido2
                else:
                    raise Exception("Apellido no valido, recuerde que todas las palabras deben iniciar con mayúsculas.")
                
            if not empleado.get("extension"):
                extension = input(f"Ingrese la extension del empleado: ")
                if re.match(r'^\d{4}$', extension) is not None:
                    empleado["extension"] = extension
                else:
                    raise Exception("Extension no valida, asegurese de ingresar 4 dígitos numéricos.")
                
            if not empleado.get("email"):
                email = input(f"Ingrese el email del empleado: ")
                if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$', email) is not None:
                    empleado["email"] = email
                else:
                    raise Exception("Email no valido, intentelo.")
                
            if not empleado.get("codigo_oficina"):
                codigo_oficina = input(f"Ingrese codigo de la oficina: ")
                if re.match(r'^[A-Z]{3}-[A-Z]{2,3}$', codigo_oficina) is not None:
                    empleado["codigo_oficina"] = codigo_oficina
                else:
                    raise Exception("Codigo no valido, use el formato (XXX-XX) o (XXX-XXX).")

            if not empleado.get("codigo_jefe"):
                codigo = input("Ingrese el codigo del jefe: ")
                if re.match(r'^[0-9]+$', codigo) is not None:
                    codigo = int(codigo)
                    empleado["codigo_jefe"] = codigo
                else:
                    raise Exception(f"El codigo del jefe no es valido, asegurese de ingresar solo dígitos numéricos.")

            if not empleado.get("puesto"):
                puesto = input(f"Ingrese el puesto del empleado: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', puesto) is not None:
                    xd = GE.getPuestoAsd(puesto)
                    if xd:
                        empleado["puesto"] = puesto
                        break
                    else:
                        raise Exception("Puestos validos: ( Representante Ventas, Subdirector Marketing, Subdirector Ventas, Secretaria, Director Oficina )")
                else:
                    raise Exception("Puestos validos: ( Representante Ventas, Subdirector Marketing, Subdirector Ventas, Secretaria, Director Oficina )")

        except Exception as error:
            print(error)
    
    peticion = requests.post("http://154.38.171.54:5003/empleados", data=json.dumps(empleado, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Empleado Guardado"
    return [res]

def DeleteEmpleado(id):
    data = GE.getEmpleadoCodigoasd(id)
    if len(data):
        peticion = requests.delete(f"http://154.38.171.54:5003/empleados/{id}")
        if peticion.status_code == 204:
            data.append({"message":  "Empleado eliminado correctamente"})
            return {
                "body": data,
                "status": peticion.status_code,
            }     
    else:
        return {
                "body":[{
                    "Mensaje": "Empleado no encontrado.",
                    "id": id,
            }],
            "status": 400,
            }

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
2. Eliminar un empleado.
          
0. Regresar.
          """)
        opcion = int(input(f"""

Seleccione una opciòn: """))
        
        if opcion==1:
            print(tabulate(GuardarEmpleado(), headers="keys", tablefmt="github"))
            input(f"""
Escriba una tecla para continuar: """)
            
        elif opcion == 2:
                idEmpleado = int(input("Ingrese el id del Empleado: "))
                print(tabulate(DeleteEmpleado(idEmpleado), headers="keys", tablefmt="github"))
                input(f"""
Escriba una tecla para continuar: """)

        elif opcion ==0:
            break