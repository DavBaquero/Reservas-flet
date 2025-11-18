import Model.conexion as conexion

def create_user(username, password):
    conn = conexion.connection()
    cursor = conn.cursor()
    if validate_user(username, password):
        cursor.close()
        conn.close()
        return False
    cursor.execute("INSERT INTO usuarios (email, contra) VALUES (%s, %s)", (username, password))
    conn.commit()
    cursor.close()
    conn.close()
    return True


def validate_user(username, password):
    conn = conexion.connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email = %s AND contra = %s", (username, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user is not None