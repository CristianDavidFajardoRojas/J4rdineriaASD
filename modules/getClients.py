import json
import requests
from tabulate import tabulate 

#json-server storages/cliente.json -b 5002
def dataClientes():
    peticion = requests.get("http://172.16.100.124:5002")
    data = peticion.json()
    return data

#json-server storages/empleados.json -b 5003
def dataEmpleados():
    peticion = requests.get("http://172.16.100.124:5003")
    data = peticion.json()
    return data


def search():
    ClienteName = list()
    for val in dataClientes():
        CodName = dict({
            "Codigo": val.get("codigo_cliente"),
            "Nombre": val.get("nombre_cliente")
        })
        ClienteName.append(CodName)
    return ClienteName

def getOneClienteCodigo(codigo):
    for val in dataClientes():
        if(val.get("codigo_cliente") == codigo):
            return[{
                "codigo_cliente": val.get("codigo_cliente"),
                "nombre_cliente": val.get("nombre_cliente")
            }]
        
def getAllClientsCreditCiudad(limiteCredit, ciudad):
    clienteCredito = list()
    for val in dataClientes():
        if(val.get("limite_credito") >= limiteCredit and val.get("ciudad") == ciudad):
            clienteCredito.append({
                "Codigo":val.get("codigo_cliente"),
                "Nombre":val.get("nombre_cliente"),
                "Contacto":f'{val.get("nombre_contacto")} {val.get("apellido_contacto")}',
                "Telefono":val.get("telefono"),
                "Fax":val.get("fax"),
                "Direccion": f'{val.get("linea_direccion1")} / {val.get("linea_direccion2")}',
                "Pais":val.get("pais"),
                "Ciudad":val.get("ciudad"),
                "Codigo Postal":val.get("codigo_postal"),
                "Codigo rep. de ventas":val.get("codigo_empleado_rep_ventas"),
                "Limite de Credito":val.get("limite_credito")
            })
    return clienteCredito

def getAllClientsPaisegionCiudad(Pais, Region=None, Ciudad=None):
    ClienteZona = list()
    for val in dataClientes():
        if (
            val.get("pais") == Pais or 
            (val.get("region") == Region or val.get("region") == None) and 
            (val.get("ciudad") == Ciudad or val.get("ciudad") == None)
        ):
            ClienteZona.append(val)
    return ClienteZona

# 5 filtros extra 
def getAllClientsMismoFax(Fax):
    ClientFax = list()
    for val in dataClientes():
        if (val.get("fax") == Fax):
            ClientFax.append({
                "Codigo":val.get("codigo_cliente"),
                "Nombre":val.get("nombre_cliente"),
                "Contacto":f'{val.get("nombre_contacto")} {val.get("apellido_contacto")}',
                "Telefono":val.get("telefono"),
                "Fax":val.get("fax"),
                "Direccion": f'{val.get("linea_direccion1")} / {val.get("linea_direccion2")}',
                "Pais":val.get("pais"),
                "Ciudad":val.get("ciudad"),
                "Codigo Postal":val.get("codigo_postal"),
                "Codigo rep. de ventas":val.get("codigo_empleado_rep_ventas"),
                "Limite de Credito":val.get("limite_credito")
            })
    return ClientFax

def getAllClientsMismoCodigo_empleado_rep_ventas(Codigo):
    CodigoEmpleado = list()
    for val in dataClientes():
        if val.get("codigo_empleado_rep_ventas") == Codigo:
            CodigoEmpleado.append({
                "Codigo":val.get("codigo_cliente"),
                "Nombre":val.get("nombre_cliente"),
                "Contacto":f'{val.get("nombre_contacto")} {val.get("apellido_contacto")}',
                "Telefono":val.get("telefono"),
                "Fax":val.get("fax"),
                "Direccion": f'{val.get("linea_direccion1")} / {val.get("linea_direccion2")}',
                "Pais":val.get("pais"),
                "Ciudad":val.get("ciudad"),
                "Codigo Postal":val.get("codigo_postal"),
                "Codigo rep. de ventas":val.get("codigo_empleado_rep_ventas"),
                "Limite de Credito":val.get("limite_credito")
            })
    return CodigoEmpleado

def getAllClientsNombrePostal():
    NombreYPostal = list()
    for val in dataClientes():
        datos = dict({"Nombre Cliente": val.get("nombre_cliente"), "Codigo Postal": val.get("codigo_postal")})
        NombreYPostal.append(datos)
    return NombreYPostal

def getAllClientsLineaDirecciones():
    direcciones = list()
    for val in dataClientes():
        direccion1y2 = dict({"Nombre":val.get("nombre_cliente"), "Direccion":f'{val.get("linea_direccion1")} / {val.get("linea_direccion2")}'})
        direcciones.append(direccion1y2)
    return direcciones

def getAllclientsApellidoContacto(apellido):
    apellidos = list()
    for val in dataClientes():
        if (val.get("apellido_contacto") == apellido):
            apellidos.append({
                "Codigo":val.get("codigo_cliente"),
                "Nombre":val.get("nombre_cliente"),
                "Contacto":f'{val.get("nombre_contacto")} {val.get("apellido_contacto")}',
                "Telefono":val.get("telefono"),
                "Fax":val.get("fax"),
                "Direccion": f'{val.get("linea_direccion1")} / {val.get("linea_direccion2")}',
                "Pais":val.get("pais"),
                "Ciudad":val.get("ciudad"),
                "Codigo Postal":val.get("codigo_postal"),
                "Codigo rep. de ventas":val.get("codigo_empleado_rep_ventas"),
                "Limite de Credito":val.get("limite_credito")
            })
    return apellidos

#punto 7
def getAllNombresSpain():
    nombresEspaña = list()
    for val in dataClientes():
        if val.get("pais") == "Spain":
            nombresEspaña.append({"nombre":val.get("nombre_cliente"),
                                  "Pais":val.get("pais")})
    return nombresEspaña

def getAllClientsMadridYRepVentas11o30():
    MadridYCodigoRepresentante = list()
    for val in dataClientes():
        if val.get("ciudad") == "Madrid" and (val.get("codigo_empleado_rep_ventas") == 11 or 30):
                MadridYCodigoRepresentante.append({
                "Codigo":val.get("codigo_cliente"),
                "Nombre":val.get("nombre_cliente"),
                "Contacto":f'{val.get("nombre_contacto")} {val.get("apellido_contacto")}',
                "Telefono":val.get("telefono"),
                "Fax":val.get("fax"),
                "Direccion": f'{val.get("linea_direccion1")} / {val.get("linea_direccion2")}',
                "Pais":val.get("pais"),
                "Ciudad":val.get("ciudad"),
                "Codigo Postal":val.get("codigo_postal"),
                "Codigo rep. de ventas":val.get("codigo_empleado_rep_ventas"),
                "Limite de Credito":val.get("limite_credito")
                })
    return MadridYCodigoRepresentante

def getAllClientsYRepresentantes():
    ClientesYSuRepresentante = list()
    for val in dataClientes():
        for cris in dataEmpleados():
            if val.get("codigo_empleado_rep_ventas") == cris.get("codigo_empleado"):
                ClientesYSuRepresentante.append({
                    "Nombre Cliente": val.get("nombre_cliente"),
                    "Representante de ventas": f'{cris.get("nombre")} {cris.get("apellido1")}'
                })
    return ClientesYSuRepresentante





def menu():
    while True:
        print(f"""
 _____                       _                  _             _ _            _            
|  __ \                     | |                | |           | (_)          | |           
| |__) |___ _ __   ___  _ __| |_ ___  ___    __| | ___    ___| |_  ___ _ __ | |_ ___  ___ 
|  _  // _ \ '_ \ / _ \| '__| __/ _ \/ __|  / _` |/ _ \  / __| | |/ _ \ '_ \| __/ _ \/ __|
| | \ \  __/ |_) | (_) | |  | ||  __/\__ \ | (_| |  __/ | (__| | |  __/ | | | ||  __/\__ /
|_|  \_\___| .__/ \___/|_|  \__\ ___||___/  \__,_|\___|  \___|_|_|\___|_| |_|\__\___||___/
            |_|                                                                                                                                             
        
            
1. Obtener todos los clientes ( Codigo y Nombre ).
2. Obtener un cliente por el codigo ( Codigo y Nombre ).
3. Obtener toda la información según el limite de credito y la ciudad.
4. Obtener información de los clientes según su fax.
5. Obtener toda la información con el codigo del representante de ventas.
6. Obtener nombres y postales de los clientes.
7. Obtener las direcciones de los clientes.
8. Obtener la información de los clientes según su apellido.
9. Obtener los nombres de los clientes que viven en españa.
10. Obtener informaciòn de los clientes de madrid con representante de ventas codigo 11 o 30.
11. Obtener nombre de los clientes con el nombre de su representante de ventas.

0. Regresar al menu principal.
        """)

        opcion = int(input(f"""
                
    Seleccione una de las opciones: """))
        if opcion == 1:
            print(tabulate(search(), headers="keys", tablefmt="rounded_grid"))
            
        elif opcion == 2:
            codigocliente = int(input(f"""
    Ingrese el codigo del cliente: """))
            print(tabulate(getOneClienteCodigo(codigocliente), headers="keys", tablefmt="rounded_grid"))
            
        elif opcion == 3:
            limiteCredito = float(input(f"""

    Ingrese el limite de credito: """))
            ciudaad = input(f"""
    Ingrese la ciudad: """)
            print(tabulate(getAllClientsCreditCiudad(limiteCredito, ciudaad), headers="keys", tablefmt="rounded_grid"))
            

        elif opcion == 4:
            faxx = (input(f"""
    Ingrese el fax del cliente: """))
            print(tabulate(getAllClientsMismoFax(faxx),headers="keys", tablefmt="rounded_grid"))
            

        elif opcion == 5:
            codigoEmpleadoRepVentas = int(input(f"""
    Ingrese el codigo del empleado en el reporte de ventas: """))
            print(tabulate(getAllClientsMismoCodigo_empleado_rep_ventas(codigoEmpleadoRepVentas),headers="keys", tablefmt="rounded_grid"))
            

        elif opcion == 6:
            print(tabulate(getAllClientsNombrePostal(),headers="keys", tablefmt="rounded_grid"))
            

        elif opcion == 7:
            print(tabulate(getAllClientsLineaDirecciones(),headers="keys", tablefmt="rounded_grid"))
            

        elif opcion ==8:
            apellidoo = input(f"""
    Escriba el apellido del cliente: """)
            print(tabulate(getAllclientsApellidoContacto(apellidoo),headers="keys", tablefmt="rounded_grid"))
            

        elif opcion == 9:
            print(tabulate(getAllNombresSpain(),headers="keys", tablefmt="rounded_grid"))

        elif opcion == 10:
            print(tabulate(getAllClientsMadridYRepVentas11o30(),headers="keys", tablefmt="rounded_grid"))

        elif opcion == 11:
            print(tabulate(getAllClientsYRepresentantes(),headers="keys", tablefmt="rounded_grid"))


            
        
        elif opcion == 0:
            break
