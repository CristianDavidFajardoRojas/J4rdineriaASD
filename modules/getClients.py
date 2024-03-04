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