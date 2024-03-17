#from tabulate import tabulate
import modules.getClients as cliente
import modules.getEmpleados as Empleados
import modules.getPedidos as Pedidos
import modules.getOficina as Oficina
import modules.getPagos as Pag
import modules.getProducto as Produc
import os

def menu():
      while True:
            os.system("clear")
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
2. Empleados
3. Pedidos
4. Oficina
5. Pagos
6. Productos 

0. Salir""")
            try:
                  opcion = int(input(f"""
                         
Seleccione una de las opciones: """))
                  if (opcion == 1):
                        cliente.menuClientes()
                  elif (opcion == 2):
                        Empleados.menuEmpleados()
                  elif (opcion == 3):
                        Pedidos.menuPedidos()
                  elif (opcion == 4):
                        Oficina.menuOficinas()
                  elif (opcion == 5):
                        Pag.menuPagos()
                  elif (opcion == 6):
                        Produc.menuProductos()
                  elif (opcion == 0):
                        print(f"""
                        
Gracias por usar el servicio, vuelva pronto!""")
                        break
            
            except ValueError as error:
                  print(f"""
Usuario, error en la selección de opciones: {error} """)
                  input(f"Escriba una letra para regresar: ")
      
menu()
            