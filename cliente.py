# Contenido de mi_paquete/cliente.py

class Cliente:
    def __init__(self, nombre, direccion, historial_compras=None):
        self.nombre = nombre
        self.direccion = direccion
        self.historial_compras = historial_compras or []

    def realizar_compra(self, producto, cantidad, precio_unitario):
        total = cantidad * precio_unitario
        self.historial_compras.append(f"Compra de {cantidad} {producto} por ${total}")

    def obtener_historial_compras(self):
        return self.historial_compras

    def __str__(self):
        return f"Cliente: {self.nombre}, Dirección: {self.direccion}"


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


# %%
import zipfile

# Crear un archivo ZIP
with zipfile.ZipFile('mi_paquete.zip', 'w') as mi_zip:
    # Agregar el código directamente al ZIP
    mi_zip.writestr('mi_paquete/cliente.py', '''
class Cliente:
    def __init__(self, nombre, direccion, historial_compras=None):
        self.nombre = nombre
        self.direccion = direccion
        self.historial_compras = historial_compras or []

    def realizar_compra(self, producto, cantidad, precio_unitario):
        total = cantidad * precio_unitario
        self.historial_compras.append(f"Compra de {cantidad} {producto} por ${total}")

    def obtener_historial_compras(self):
        return self.historial_compras

    def __str__(self):
        return f"Cliente: {self.nombre}, Dirección: {self.direccion}"
''')

print("Archivo ZIP creado: mi_paquete.zip")



