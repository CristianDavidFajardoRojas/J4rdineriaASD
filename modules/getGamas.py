import json
import requests

#json-server storages/gama_producto.json -b 5509
def getAllGama():
    peticion = requests.get("http://192.168.1.6:5509")
    data = peticion.json()
    return data

def getAllNombre(gama):
    for val in getAllGama():
        if val.get("gama") == gama:
            return [val]
    
    