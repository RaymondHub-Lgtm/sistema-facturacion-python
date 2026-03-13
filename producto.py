import tkinter as tk
from database import conexion

def ventana_productos():
    ventana = tk.Toplevel()
    ventana.title("Productos")
    ventana.geometry("400x500")

    
    tk.Label(ventana, text="Agregar producto", font=("Arial", 16, "bold")).pack(pady=10)
    
    tk.Label(ventana, text="Nombre del producto").pack()
    entrada_nombre = tk.Entry(ventana)
    entrada_nombre.pack(pady=5)

    tk.Label(ventana, text="Precio").pack()
    entrada_precio = tk.Entry(ventana)
    entrada_precio.pack()

    
    lista_productos = tk.Listbox(ventana)
    lista_productos.pack(fill="both", expand=True, pady=10)

   
    def agregar_producto():
        nombre = entrada_nombre.get()
        precio = entrada_precio.get()
        if nombre != "" and precio != "":
            
            conexion.guardar_producto(nombre, precio)
            
            lista_productos.insert(tk.END, f"{nombre} - ${precio}")
            
            entrada_nombre.delete(0, tk.END)
            entrada_precio.delete(0, tk.END)

    tk.Button(ventana, text="Agregar producto", command=agregar_producto).pack(pady=10)

    
    for prod in conexion.obtener_productos():
        lista_productos.insert(tk.END, f"{prod[0]} - ${prod[1]}")

def abrir_productos():
    ventana_productos()
