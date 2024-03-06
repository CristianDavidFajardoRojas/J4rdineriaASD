import storages.pedido as ped

def getAllEstadosPedido():
    pedidoEstado = []
    for val in ped.pedido:
        pedidoEstado.append({
            "codigo_pedido": val.get('codigo_pedido'),
            "estado": val.get('estado')
        })
    return pedidoEstado