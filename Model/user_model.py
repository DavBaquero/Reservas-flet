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