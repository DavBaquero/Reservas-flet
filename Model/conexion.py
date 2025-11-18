import mysql.connector

def connection():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="reservas")
    return conexion