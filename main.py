from tabulate import tabulate
import modules.getClients as cliente
import modules.getEmpleados as Empleados
import modules.getPedidos as Pedidos
import modules.getOficina as Oficina

print(tabulate(Pedidos.getAllPedidosEntregadosEnero(), tablefmt="rounded_grid"))