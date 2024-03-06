import storages.oficina as of

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
                "oficinas" : val.get("cpodigo_oficina"),
                "pais" : val.get("pais") 
            })
    return ciudadTelefono