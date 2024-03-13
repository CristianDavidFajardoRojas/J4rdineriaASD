import json
import requests

#json-server storage/producto.json -b 5501
def getAllGama():
    peticion = requests.get("http://172.16.100.124:5502")
    data = peticion.json()
    return data

def getAllNombre():
    gamanombre = []
    for val in getAllGama():
        gamanombre.append(val.get("gama"))
        return gamanombre
    
    