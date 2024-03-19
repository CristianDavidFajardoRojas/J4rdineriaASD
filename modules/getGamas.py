import json
import requests

#json-server storages/gama_producto.json -b 5509
def getAllGama():
    peticion = requests.get("http://154.38.171.54:5004/gama")
    data = peticion.json()
    return data

def getAllNombre(gama):
    for val in getAllGama():
        if val.get("gama") == gama:
            return [val]
    
    