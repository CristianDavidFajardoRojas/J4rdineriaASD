import storages.cliente as cli

def search():
    ClienteName = list()
    for val in cli.clientes:
        CodName = dict({
            "codigo_cliente": val.get("codigo_cliente"),
            "nombre_cliente": val.get("nombre_cliente")
        })
        ClienteName.append(CodName)
    return ClienteName

def getOneClienteCodigo(codigo):
    for val in cli.clientes:
        if(val.get("codigo_cliente") == codigo):
            return{
                "codigo_cliente": val.get("codigo_cliente"),
                "nombre_cliente": val.get("nombre_cliente")
            }
        
def getAllClientsCreditCiudad(limiteCredit, ciudad):
    clienteCredito = list()
    for val in cli.clientes:
        if(val.get("limite_credito") >= limiteCredit and val.get("ciudad") == ciudad):
            clienteCredito.append(val)
    return clienteCredito

def getAllClientsPaisegionCiudad(Pais, Region=None, Ciudad=None):
    ClienteZona = list()
    for val in cli.clientes:
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
    for val in cli.clientes:
        if (val.get("fax") == Fax):
            ClientFax.append(val)
    return ClientFax

def getAllClientsMismoCodigo_empleado_rep_ventas(Codigo):
    CodigoEmpleado = list()
    for val in cli.clientes:
        if val.get("codigo_empleado_rep_ventas") == Codigo:
            CodigoEmpleado.append(val)
    return CodigoEmpleado

def getAllClientsNombrePostal():
    NombreYPostal = list()
    for val in cli.clientes:
        datos = dict({"Nombre_Cliente": val.get("nombre_cliente"), "Codigo_Postal": val.get("codigo_postal")})
        NombreYPostal.append(datos)
    return NombreYPostal

def getAllClientsLineaDirecciones():
    direcciones = list()
    for val in cli.clientes:
        direccion1y2 = dict({"Nombre":val.get("nombre_cliente"), "Direccion_1":val.get("linea_direccion1"),"Direccion_2":val.get("linea_direccion2")})
        direcciones.append(direccion1y2)
    return direcciones

def getAllclientsApellidoContacto(apellido):
    apellidos = list()
    for val in cli.clientes:
        if (val.get("apellido_contacto") == apellido):
            apellidos.append(val)
    return apellidos

#punto 7
def getAllNombresSpain():
    nombresEspaña = list()
    for val in cli.clientes:
        if val.get("pais") == "Spain":
            nombresEspaña.append({"nombre":val.get("nombre_cliente"),
                                  "Pais":val.get("pais")})
    return nombresEspaña
            
