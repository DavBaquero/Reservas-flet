import Model.conexion as con

def get_user(user_id):
    conexion = con.connection()
    cursor = conexion.cursor(dictionary=True)

    query = "SELECT * FROM usuarios WHERE id = %s"
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()

    cursor.close()
    conexion.close()

    return user


def get_reservations_by_user(user_id):
    conexion = con.connection()
    cursor = conexion.cursor(dictionary=True)

    query = "SELECT * FROM reserva WHERE usuario_id = %s"
    cursor.execute(query, (user_id,))
    reservations = cursor.fetchall()

    cursor.close()
    conexion.close()

    return reservations

def set_observation(reservation_id, observation, user_id):
    conexion = con.connection()
    cursor = conexion.cursor()
    print("Updating observation:", reservation_id, observation, user_id)  # Debugging line
    query = "UPDATE reserva SET obser = %s WHERE id = %s AND usuario_id = %s"
    cursor.execute(query, (observation, reservation_id, user_id))
    conexion.commit()

    cursor.close()
    conexion.close()

def get_password_hashed(user_id):
    conexion = con.connection()
    cursor = conexion.cursor()
    query = f"select contra from usuarios where id = {user_id}"
    cursor.execute(query)
    password = cursor.fetchone()
    cursor.close()
    conexion.close()
    return password

def set_password(user_id, new_pass):
    conexion = con.connection()
    cursor = conexion.cursor()
    query = f"update usuarios set contra = '{new_pass}' where id = {user_id}"
    cursor.execute(query)
    conexion.commit()
    cursor.close()
    conexion.close()

def log_out(user_id):
    conexion = con.connection()
    cursor = conexion.cursor()
    estado = 0
    query = f"update usuarios set logeado = {0} where id = {user_id}"
    cursor.execute(query)
    conexion.commit()
    cursor.close()
    conexion.close()

def change_theme(valor,user_id):
    conexion = con.connection()
    cursor = conexion.cursor()
    query = f"update usuarios set dark_mode = {valor} where id ={user_id}"
    cursor.execute(query)
    conexion.commit()
    cursor.close()
    conexion.close()

def get_theme(user_id):
    conexion = con.connection()
    cursor = conexion.cursor()
    query = f"select dark_mode from usuarios where id = {user_id}"
    cursor.execute(query)
    valor = cursor.fetchone()
    cursor.close()
    conexion.close()
    return valor

def set_state_reserva(id_reserva, estado):
    conexion = con.connection()
    cursor = conexion.cursor()
    query = f"update reserva set estado = {estado} where id = {int(id_reserva)}"
    cursor.execute(query)
    conexion.commit()
    cursor.close()
    conexion.close()