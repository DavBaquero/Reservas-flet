import mysql.connector

# Función para establecer la conexión a la base de datos
def connection():
    conexion = mysql.connector.connect(
        host="localhost", # El host de la base de datos
        user="root", # El usuario de la base de datos
        password="root", # La contraseña de la base de datos
        database="reservas" # El nombre de la base de datos
        )
    # Retornar el objeto de conexión
    return conexion