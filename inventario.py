class Inventario:
    def __init__(self):
        # La lista empieza vacía, lista para que el código de tu compañero la llene
        self.productos = []

    def agregar_producto(self, nombre, cantidad, precio):
        nuevo_producto = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
        self.productos.append(nuevo_producto)
        print(f"✅ Producto '{nombre}' registrado en el sistema.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está actualmente vacío.")
        else:
            for p in self.productos:
                print(p)
