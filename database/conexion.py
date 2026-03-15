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

def guardar_cliente(nombre, telefono):
    conexion = sqlite3.connect(db_path)
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nombre TEXT, telefono TEXT)")
    cursor.execute("INSERT INTO clientes (nombre, telefono) VALUES (?, ?)", (nombre, telefono))
    conexion.commit()
    conexion.close()

def obtener_clientes():
    conexion = sqlite3.connect(db_path)
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nombre TEXT, telefono TEXT)")
    cursor.execute("SELECT nombre, telefono FROM clientes")
    datos = cursor.fetchall()
    conexion.close()
    return datos

def eliminar_producto(nombre):
    conexion = sqlite3.connect(db_path)
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM productos WHERE nombre = ?", (nombre,))
    conexion.commit()
    conexion.close()

def eliminar_cliente(nombre):
    conexion = sqlite3.connect(db_path)
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM clientes WHERE nombre = ?", (nombre,))
    conexion.commit()
    conexion.close()
