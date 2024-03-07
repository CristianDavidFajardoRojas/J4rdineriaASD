#from tabulate import tabulate
import modules.getClients as cliente
import modules.getEmpleados as Empleados
import modules.getPedidos as Pedidos
import modules.getOficina as Oficina
import modules.getPagos as Pagos

print(Pagos.getAll2008Paypal())
      #, tablefmt="rounded_grid"))