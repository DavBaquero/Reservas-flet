import Model.conexion as conexion

def validate_login(username, password):
    conn = conexion.connection()
    cursor = conn.cursor()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email = %s AND contra = %s", (username, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user is not None

def validate_user_exists(username):
    conn = conexion.connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email = %s", (username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user is not None
