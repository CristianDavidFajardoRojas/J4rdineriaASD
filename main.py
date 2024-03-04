from tabulate import tabulate
import modules.getClients as cliente

print(tabulate(cliente.getAllClientsPaisegionCiudad(None, None, "Madrid"), tablefmt="grid"))