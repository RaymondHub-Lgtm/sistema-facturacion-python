import tkinter as tk
import producto
import inventario


def abrir_clientes():
    print("Abrir modulo de clientes")


def abrir_productos():
    producto.ventana_productos()
    print("Abrir modulo de productos")


def abrir_inventario():
    inventario.mostrar_inventario()
    print("abrir modulo de inventario")


def abrir_facturas():
    print("Abrir modulo de facturas")


ventana = tk.Tk()
ventana.title("Sistema de Facturacion")
ventana.geometry("600x400")
ventana.config(bg="#2c3e50")

titulo = tk.Label(
    ventana,
    text="Sistema de Facturacion",
    font=("Arial", 22, "bold"),
    bg="#2c3e50",
    fg="White",
)

boton_clientes = tk.Button(
    ventana, text="Clientes", width=20, height=2, command=abrir_clientes
)

boton_clientes.pack(pady=10)

boton_productos = tk.Button(
    ventana, text="Productos", width=20, height=2, command=abrir_productos
)

boton_productos.pack(pady=10)

boton_inventario = tk.Button(
    ventana, text="Inventario", width=20, height=2, command=abrir_inventario
)

boton_inventario.pack(pady=10)

boton_facturas = tk.Button(
    ventana, text="Facturas", width=20, height=2, command=abrir_facturas
)

boton_facturas.pack(pady=10)

ventana.mainloop()
