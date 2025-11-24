# Model/reservation_storage_db.py
from datetime import date, datetime
from typing import List

import Model.conexion as conexion
from Model.reservation_model import Reservation, Dish


def _parse_date(value: str) -> date:
    """
    Convierte 'YYYY-MM-DD' o 'YYYY-MM-DD HH:MM:SS' a datetime.date.
    """
    try:
        return date.fromisoformat(value)
    except ValueError:
        return datetime.fromisoformat(value).date()


def load_reservations() -> List[Reservation]:

    conn = conexion.connection()
    cur = conn.cursor(dictionary=True)

    cur.execute(
        """
        SELECT id, fecha, hora, personas, estado, tipo, obser, usuario_id
        FROM reserva
        """
    )
    rows = cur.fetchall()

    cur.close()
    conn.close()

    reservations: List[Reservation] = []

    for row in rows:
        reservations.append(
            Reservation(
                date=_parse_date(row["fecha"]),
                time=row["hora"],
                people=row["personas"],
                dishes=[],  # Los platos se eligen en runtime, no se cargan de BD
                notes=row["obser"],
                user_id=row["usuario_id"],
            )
        )

    return reservations


def save_reservation(reservation: Reservation) -> None:

    conn = conexion.connection()
    cur = conn.cursor()

    fecha_str = reservation.date.isoformat()

    if reservation.dishes:
        tipo = ", ".join(d.name for d in reservation.dishes)
    else:
        tipo = "Reserva restaurante"

    cur.execute(
        """
        INSERT INTO reserva (fecha, hora, personas, estado, tipo, obser, usuario_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        (
            fecha_str,
            reservation.time,
            reservation.people,
            1,
            tipo,
            reservation.notes,
            reservation.user_id or 1,
        ),
    )

    conn.commit()
    cur.close()
    conn.close()
