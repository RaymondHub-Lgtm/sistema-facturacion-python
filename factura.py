from database.conexion import obtener_productos, obtener_clientes
def crear_factura():
    productos = obtener_productos()
    clientes = obtener_clientes()

    print("clientes disponibles:")
    for cliente in clientes:
        print(f"{cliente[0]}: {cliente[1]}")

    cliente_id = int(input("ingrese el id del cliente: "))

    factura_items = []
    while True:
        print("productos disponibles:")
        for producto in productos:
            print(f"{producto[0]}: {producto[1]} - ${producto[2]}")
        producto_id = int(input("ingrese el id del producto (0 para finalizar): "))
        if producto_id == 0:
            break
        cantidad = int(input("ingrese la cantidad: "))
        factura_items.append((producto_id, cantidad))

    total = 0
    for item in factura_items:
        producto_id, cantidad = item
        producto = next((p for p in productos if p[0] == producto_id))
        total += producto[2] * cantidad

    print(f"total de la factura: ${total}")
    ventana_factura = tk.toplevel(ventana)