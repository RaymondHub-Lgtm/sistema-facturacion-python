import tkinter as tk
from database import conexion

def ventana_facturas():

    ventana = tk.Toplevel()
    ventana.title("Facturación")
    ventana.geometry("500x550")

    total = 0

    tk.Label(
        ventana,
        text="Nueva Factura",
        font=("Arial", 18, "bold")
    ).pack(pady=10)

  
    tk.Label(ventana, text="ID del Cliente").pack()
    entrada_cliente = tk.Entry(ventana)
    entrada_cliente.pack(pady=5)

   
    tk.Label(ventana, text="ID del Producto").pack()
    entrada_producto = tk.Entry(ventana)
    entrada_producto.pack(pady=5)

    lista = tk.Listbox(ventana)
    lista.pack(fill="both", expand=True, pady=10)

    label_total = tk.Label(
        ventana,
        text="Total: $0",
        font=("Arial", 14, "bold")
    )
    label_total.pack(pady=10)

    def agregar_producto():
        nonlocal total
        valor = entrada_producto.get().strip()

        if not valor.isdigit():
          lista.insert(tk.END, "ID inválido")
          return

        id_producto = int(valor)

        productos = conexion.obtener_productos()

        try:
            id_producto = int(entrada_producto.get())

            productos = conexion.obtener_productos()

            for prod in productos:
                id_db = prod[0]
                nombre = prod[1]
                precio = float(prod[2])

                if id_db == id_producto:
                 lista.insert(tk.END, f"{nombre} - ${precio}")
                 total += precio
                 label_total.config(text=f"Total: ${total}")
                 break
            else:
              lista.insert(tk.END, "Producto no encontrado")

        except:
            lista.insert(tk.END, "ID inválido")

        entrada_producto.delete(0, tk.END)

    tk.Button(
        ventana,
        text="Agregar Producto",
        command=agregar_producto
    ).pack(pady=5)

    
    def finalizar_factura():
        cliente_id = entrada_cliente.get()

        if cliente_id == "":
            lista.insert(tk.END, "Ingrese ID del cliente")
            return

        lista.insert(tk.END, "------ FACTURA GENERADA ------")
        lista.insert(tk.END, f"Cliente ID: {cliente_id}")
        lista.insert(tk.END, f"TOTAL: ${total}")

    tk.Button(
        ventana,
        text="Finalizar Factura",
        bg="green",
        fg="white",
        command=finalizar_factura
    ).pack(pady=10)
