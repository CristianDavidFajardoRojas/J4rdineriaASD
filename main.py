from tabulate import tabulate
import modules.getClients as cliente
import modules.getEmpleados as Empleados

print(tabulate(Empleados.getAllNombreApellidosPuestoNoRepVentas(), tablefmt="grid"))