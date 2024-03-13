import json
import requests

#json-server storage/producto.json -b 5501
def postProducto(producto):
    peticion = requests.get("http://172.16.100.124:5501", data=json.dumps(producto))
    res = peticion.json()
    return res