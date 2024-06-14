# Contenido de mi_paquete/main.py
from mi_paquete.cliente import Cliente

# Crear un objeto Cliente
cliente1 = Cliente(nombre="Juan", direccion="123 Calle Principal")

# Realizar una compra
cliente1.realizar_compra(producto="Camiseta", cantidad=2, precio_unitario=15.0)

# Imprimir información del cliente
print(str(cliente1))

# Obtener historial de compras
historial = cliente1.obtener_historial_compras()
print("Historial de compras:")
for compra in historial:
    print("-", compra)
