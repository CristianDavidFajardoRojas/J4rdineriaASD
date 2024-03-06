import storages.empleados as em 

def getAllNombreApellidoEmailJefe(codigo):
    NombreApellidoEmail = []
    for val in em.empleados:
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
    for val in em.empleados:
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
    for val in em.empleados:
        if val.get("puesto") != "Representante Ventas":
            InfoNoRepVentas.append({
                "Puesto":val.get("puesto"),
                "Nombre":val.get("nombre"),
                "Apellido": val.get("apellido1"),
            })
    return InfoNoRepVentas

