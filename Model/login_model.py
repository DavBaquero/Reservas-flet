import Model.conexion as conexion

# Función para validar las credenciales de inicio de sesión
def validate_login(username, password):
    # Establecer la conexión a la base de datos
    conn = conexion.connection()
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Ejecutar la consulta para verificar las credenciales del usuario
    cursor.execute("SELECT * FROM usuarios WHERE email = %s AND contra = %s", (username, password))
    # Obtener el resultado de la consulta
    user = cursor.fetchone()
    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()
    # Retornar True si el usuario existe, de lo contrario False
    return user is not None

# Función para validar si un usuario existe
def validate_user_exists(username):
    # Establecer la conexión a la base de datos
    conn = conexion.connection()
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Ejecutar la consulta para verificar si el usuario existe
    cursor.execute("SELECT * FROM usuarios WHERE email = %s", (username,))
    # Obtener el resultado de la consulta
    user = cursor.fetchone()
    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()
    # Retornar True si el usuario existe, de lo contrario False
    return user is not None
