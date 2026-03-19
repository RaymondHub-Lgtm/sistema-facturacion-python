import tkinter as tk
from database import conexion

def ventana_clientes(root): 
    ventana = tk.Toplevel(root)
    ventana.title("Gestión de Clientes")
    ventana.geometry("400x500")

    tk.Label(ventana, text="Agregar Cliente", font=("Arial", 16, "bold")).pack(pady=10)
    
    tk.Label(ventana, text="Nombre Completo").pack()
    entrada_nombre = tk.Entry(ventana)
    entrada_nombre.pack(pady=5)

    tk.Label(ventana, text="Teléfono").pack()
    entrada_telefono = tk.Entry(ventana)
    entrada_telefono.pack()

    lista_clientes = tk.Listbox(ventana)
    lista_clientes.pack(fill="both", expand=True, pady=10)

    def agregar_cliente_ui():
        nombre = entrada_nombre.get()
        telefono = entrada_telefono.get()
        if nombre != "" and telefono != "":
            conexion.guardar_cliente(nombre, telefono)
            clientes = conexion.obtener_clientes()
            ultimo = clientes[-1]
            lista_clientes.insert(tk.END, f"ID:{ultimo[0]} - {ultimo[1]} - Tel:{ultimo[2]}")
            entrada_nombre.delete(0, tk.END)
            entrada_telefono.delete(0, tk.END)

    tk.Button(ventana, text="Registrar Cliente", command=agregar_cliente_ui).pack(pady=5)

    def eliminar_cliente_ui():
        seleccion = lista_clientes.curselection()
        if not seleccion:
            return
        
        seleccionado = lista_clientes.get(seleccion[0])
        cliente_id = seleccionado.split(" - ")[0].replace("ID:", "")
        conexion.eliminar_cliente(cliente_id)
        lista_clientes.delete(seleccion[0])

    tk.Button(ventana, text="Eliminar Seleccionado", fg="white", bg="red", command=eliminar_cliente_ui).pack(pady=5)

    for cli in conexion.obtener_clientes():
        lista_clientes.insert(tk.END, f"ID:{cli[0]} - {cli[1]} - Tel:{cli[2]}")

def abrir_ventana(root):
    ventana_clientes(root)