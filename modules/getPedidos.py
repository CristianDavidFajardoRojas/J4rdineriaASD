import storages.pedido as ped
from datetime import datetime
from tabulate import tabulate

def getAllEstadosPedido():
    pedidoEstado = []
    for val in ped.pedido:
        pedidoEstado.append({
            "codigo_pedido": val.get('codigo_pedido'),
            "estado": val.get('estado')
        })
    return pedidoEstado

def getAllPedidosEntregadosAtrasadosDeTiempo():
    pedidosEntregado = list()
    for val in ped.pedido:
        if (val.get("estado") == "Entregado" and val.get("fecha_entrega") == None):
            val["fecha_entrega"] = val.get("fecha_esperada")
        if (val.get("estado") == "Entregado"):
            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if diff.days < 0:
                pedidosEntregado.append({
                    "codigo_de_pedido": val.get("codigo_pedido"),
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_esperada": val.get("fecha_esperada"),
                    "fecha_de_entrega": val.get("fecha_entrega")
                })
    return pedidosEntregado

#Filtro 10
def getAllPedidosEntregadosAlmenos2DiasAntes():
    pedidosEntregado = list()
    for val in ped.pedido:
        if (val.get("estado") == "Entregado" and val.get("fecha_entrega") == None):
            val["fecha_entrega"] = val.get("fecha_esperada")
        if (val.get("estado") == "Entregado"):
            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if diff.days >= 2:
                pedidosEntregado.append({
                    "codigo_de_pedido": val.get("codigo_pedido"),
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_esperada": val.get("fecha_esperada"),
                    "fecha_de_entrega": val.get("fecha_entrega")
                })
    return pedidosEntregado

#Filtro 11
def getAllPedidosRechazados2009():
    rechazados2009 = list()
    for val in ped.pedido:
        FechaPedido = "/".join(val.get("fecha_pedido").split("-")[::-1])
        start = datetime.strptime(FechaPedido, "%d/%m/%Y")
        if val.get("estado") == "Rechazado" and start.year == 2009:
            rechazados2009.append(val)
    return rechazados2009

#Filtro 12
def getAllPedidosEntregadosEnero():
    EntregadosEnero = list()
    for val in ped.pedido:
        if (val.get("estado") == "Entregado" and val.get("fecha_entrega") != None):
            FechaEntregada = "/".join(val.get("fecha_entrega").split("-")[::-1])
            start = datetime.strptime(FechaEntregada, "%d/%m/%Y")
            if val.get("estado") == "Entregado" and start.month == 1:
                EntregadosEnero.append(val)
    return EntregadosEnero

def ReportesDePedidos():
    print(f"""
    ____                        __                   __        ____           ___     __          
   / __ \___  ____  ____  _____/ /____  _____   ____/ /__     / __ \___  ____/ (_)___/ /___  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / /_/ / _ \/ __  / / __  / __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / ____/  __/ /_/ / / /_/ / /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/  /_/    \___/\__,_/_/\__,_/\____/____/  
          /_/                                                                                     
          
1. Obtener el estado del pedido ( Entregado, Rechazado o Pendiente ).
2. Lista de pedidos atrasados de tiempo. 
3. Lista de pedidos entregados con anterioridad de 2 o mas dias.
4. Lista de pedidos Rechazados en el año 2009.
5. Lista de pedidos Entregados en el mes de enero de cualquier año. 
""")
    
    opcion = int(input(f"""
Seleccione una de las opciones: """))
    
    if opcion == 1:
        print(tabulate(getAllEstadosPedido(), headers="keys", tablefmt="rounded_grid"))

    elif opcion == 2:
        print(tabulate(getAllPedidosEntregadosAtrasadosDeTiempo(), headers="keys", tablefmt="rounded_grid")) 

    elif opcion == 3:
        print(tabulate(getAllPedidosEntregadosAlmenos2DiasAntes(), headers="keys", tablefmt="rounded_grid"))

    elif opcion == 4:
        print(tabulate(getAllPedidosRechazados2009(), headers="keys", tablefmt="rounded_grid"))

    elif opcion == 5:
        print(tabulate(getAllPedidosEntregadosEnero(), headers="keys", tablefmt="rounded_grid"))  