#from tabulate import tabulate
import modules.getClients as cliente
import modules.getEmpleados as Empleados
import modules.getPedidos as Pedidos
import modules.getOficina as Oficina
import modules.getPagos as Pag

def menu():
      print(f"""
            
  __  __                    _____      _            _             _ 
 |  \/  |                  |  __ \    (_)          (_)           | |
 | \  / | ___ _ __  _   _  | |__) | __ _ _ __   ___ _ _ __   __ _| |
 | |\/| |/ _ \ '_ \| | | | |  ___/ '__| | '_ \ / __| | '_ \ / _` | |
 | |  | |  __/ | | | |_| | | |   | |  | | | | | (__| | |_) | (_| | |
 |_|  |_|\___|_| |_|\__,_| |_|   |_|  |_|_| |_|\___|_| .__/ \__,_|_|
                                                     | |            
                                                     |_|            
1. Cliente
2. Oficina
3. Empleados
4. Pedidos""")
      
      opcion = int(input(f"""
                         
Seleccione una de las opciones: """))
      if (opcion == 1):
            cliente.menu()
      elif (opcion == 2):
            Empleados.menu()
      elif (opcion == 3):
            Pedidos.menu()
      elif (opcion == 4):
            Oficina.menu()
      elif (opcion == 5):
            Pag.menu()
            
      
menu()