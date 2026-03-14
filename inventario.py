import tkinter as tk
from database import conexion


def mostrar_inventario():  # <-- Ahora es una función directa, sin clases
    ventana_inv = tk.Toplevel()
    ventana_inv.title("Estado del Inventario")
    ventana_inv.geometry("400x500")

    tk.Label(ventana_inv, text="Productos en Stock", font=("Arial", 16, "bold")).pack(
        pady=10
    )

    lista_visual = tk.Listbox(ventana_inv)
    lista_visual.pack(fill="both", expand=True, padx=20, pady=20)

    try:
        productos_db = conexion.obtener_productos()
        if not productos_db:
            lista_visual.insert(tk.END, "El inventario está vacío")
        else:
            for prod in productos_db:
                lista_visual.insert(tk.END, f"📦 {prod[0]} - ${prod[1]}")
    except Exception as e:
        lista_visual.insert(tk.END, "Error al leer la base de datos")
