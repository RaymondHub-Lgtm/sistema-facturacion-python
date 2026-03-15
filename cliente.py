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
            lista_clientes.insert(tk.END, f"{nombre} - Tel: {telefono}")
            entrada_nombre.delete(0, tk.END)
            entrada_telefono.delete(0, tk.END)

    tk.Button(ventana, text="Registrar Cliente", command=agregar_cliente_ui).pack(pady=5)

    
    def eliminar_cliente_ui():
        try:
            seleccion = lista_clientes.curselection()
            if not seleccion:
                print("No se seleccionó nada")
                return
            
            seleccionado = lista_clientes.get(seleccion[0])
            nombre = seleccionado.split(" - ")[0]
            
            conexion.eliminar_cliente(nombre)
            lista_clientes.delete(seleccion[0])
            print(f"Cliente {nombre} eliminado")
        except Exception as e:
            print(f"Error técnico detectado: {e}")

    
    tk.Button(ventana, text="Eliminar Seleccionado", fg="white", bg="red", command=eliminar_cliente_ui).pack(pady=5)

    
    for cli in conexion.obtener_clientes():
        lista_clientes.insert(tk.END, f"{cli[0]} - Tel: {cli[1]}")

def abrir_ventana(root):
    ventana_clientes(root)