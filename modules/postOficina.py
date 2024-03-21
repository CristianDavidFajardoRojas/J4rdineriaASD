import json
import requests
from tabulate import tabulate
import os
import re
import modules.getOficina as GO

def GuardarOficina():
    oficina = dict()
    while True:
        try:
            if not oficina.get("codigo_oficina"):
                codigo_oficina = input(f"Ingrese codigo de la oficina: ")
                if re.match(r'^[A-Z]{3}-[A-Z]{2,3}$', codigo_oficina) is not None:
                    perla = GO.getCodigoOficina(codigo_oficina)
                    if perla:
                        raise Exception("Codigo de oficina ya existente.")
                    else:
                        oficina["codigo_oficina"] = codigo_oficina
                else:
                    raise Exception("Codigo no valido, use el formato (XXX-XX) o (XXX-XXX).")
            
            if not oficina.get("ciudad"):
                ciudad = input(f"Ingrese la ciudad: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', ciudad) is not None:
                    oficina["ciudad"] = ciudad
                else:
                    raise Exception("Ciudad no valida, recuerde que todas las palabras deben iniciar con mayúsculas.")
                
            if not oficina.get("pais"):
                pais = input(f"Ingrese el pais: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', pais) is not None:
                    oficina["pais"] = pais
                else:
                    raise Exception("Pais no valida, recuerde que todas las palabras deben iniciar con mayúsculas.")

            if not oficina.get("region"):
                region = input(f"Ingrese la Region: ")
                if re.match(r'^[A-Z][a-zA-Z0-9-\s]*$', region) is not None:
                    oficina["region"] = region
                else:
                    raise Exception("Region no valida, recuerde que todas las palabras deben iniciar con mayúsculas.")
            
            if not oficina.get("codigo_postal"):
                codigo_postal = input("Ingrese el codigo postal: ")
                if re.match(r'^[A-Z0-9\s-]+$', codigo_postal)is not None:
                    oficina["codigo_postal"] = codigo_postal
                else:
                    raise Exception("Codigo postal no valido.")
                
            if not oficina.get("telefono"):
                telefono = input("Ingrese el telefono: ")
                if re.match(r'^\+\d{1,3}\s\d{1,3}\s\d{4,10}$', telefono)is not None:
                    oficina["telefono"] = telefono
                else:
                    raise Exception("Telefono no valido, formato: +pais(1-3 digitos) codigo_area(1-3 digitos) telefono(4-10 digitos).")

            if not oficina.get("linea_direccion1"):
                linea_direccion1 = input(f"Ingrese la linea de direccion 1: ")
                oficina["linea_direccion1"] = linea_direccion1

            if not oficina.get("linea_direccion2"):
                linea_direccion2 = input(f"Ingrese la linea de direccion 2: ")
                oficina["linea_direccion2"] = linea_direccion2
                break              
                
        except Exception as error:
            print (error)
                             
    peticion = requests.post("http://154.38.171.54:5005/oficinas", data=json.dumps(oficina, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Oficina Guardado"
    return [res]

def DeleteOficina(id):
    data = GO.DeleteOficinaHahaDoges(id)
    if len(data):
        peticion = requests.delete(f"http://154.38.171.54:5005/oficinas/{id}")
        if peticion.status_code == 204:
            data.append({"message":  "Oficina eliminada correctamente"})
            return {
                "body": data,
                "status": peticion.status_code,
            }     
    else:
        return {
                "body":[{
                    "Mensaje": "Oficina no encontrada.",
                    "id": id,
            }],
            "status": 400,
            }

def ModificarOficina(id):
    data = GO.DeleteOficinaHahaDoges(id)
    if data is None:
            print(f"""

Id de la oficina no encontrado. """)
    
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
                data[0][datoModificar] = nuevoValor
                break
            else:
                 print(f"""
Seleccion incorrecta""")
                
        except ValueError as error:
            print(error)
    
    peticion = requests.put(f"http://154.38.171.54:5005/oficinas/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Oficina Modificado"
    return [res]

def menu():
    while True:
        os.system("clear")
        print(f"""
    ___       __          _       _      __                     ____  _____      _                 
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   / __ \/ __(_)____(_)___  ____ ______
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / / / / /_/ / ___/ / __ \/ __ `/ ___/
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / /_/ / __/ / /__/ / / / / /_/ (__  ) 
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/      \____/_/ /_/\___/_/_/ /_/\__,_/____/  
                                                                                                   



1. Guardar una oficina nueva.
2. Eliminar una oficina.
3. Modificar una oficina.

0. Regresar                                                                                                    
 """)
        
        opcion = int(input((f"""

Seleccione una opción: """)))
        if opcion == 1:
            print(tabulate(GuardarOficina(), headers="keys", tablefmt="github"))
            input(f"""
Escriba una tecla para continuar: """)
            
        elif opcion == 2:
                idOficina = input("Ingrese el id de la oficina: ")
                print(tabulate(DeleteOficina(idOficina), headers="keys", tablefmt="github"))
                input(f"""
Escriba una tecla para continuar: """)
                
        elif opcion == 3:
                idEmpleado = input("Ingrese el id de la oficina: ")
                print(tabulate(ModificarOficina(idEmpleado), headers="keys", tablefmt="github"))
                input(f"""
Escriba una tecla para continuar: """)
            
        if opcion == 0:
            break