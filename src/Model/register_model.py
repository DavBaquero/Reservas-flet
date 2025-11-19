import Model.conexion as conexion


# Función para crear un nuevo usuario
def create_user(username, password):
    # Establecer la conexión a la base de datos
    conn = conexion.connection()
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Verificar si el usuario ya existe
    if validate_user(username, password):
        cursor.close()
        conn.close()
        return False
    # Insertar el nuevo usuario en la base de datos
    cursor.execute("INSERT INTO usuarios (email, contra) VALUES (%s, %s)", (username, password))
    
    # Guardar los cambios en la base de datos
    conn.commit()
    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()
    # Retornar True indicando que el usuario fue creado exitosamente
    return True


# Función para validar si un usuario existe
def validate_user(username, password):
    # Establecer la conexión a la base de datos
    conn = conexion.connection()
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Consultar si el usuario existe en la base de datos
    cursor.execute("SELECT * FROM usuarios WHERE email = %s AND contra = %s", (username, password))
    
    # Obtener el resultado de la consulta
    user = cursor.fetchone()
    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()
    # Retornar True si el usuario existe, de lo contrario False
    return user is not None