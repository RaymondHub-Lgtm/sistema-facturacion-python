import sqlite3
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "sistema.db")

def guardar_producto(nombre, precio):
    conexion = sqlite3.connect(db_path) 
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS productos (id INTEGER PRIMARY KEY, nombre TEXT, precio REAL)")
    cursor.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)", (nombre, precio))
    conexion.commit()
    conexion.close()

def obtener_productos():
    conexion = sqlite3.connect(db_path)
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, precio FROM productos")
    datos = cursor.fetchall()
    conexion.close()
    return datos