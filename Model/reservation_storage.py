# Model/reservation_storage.py
import json
from pathlib import Path
from typing import List, Any
from datetime import date, datetime

from Model.reservation_model import Reservation, Dish


STORAGE_FILE = Path("data") / "reservations.json"


def reservation_to_dict(r: Reservation) -> dict:
    """Convierte una Reservation en dict serializable a JSON."""
    if isinstance(r.date, datetime):
        date_str = r.date.date().isoformat()
    elif isinstance(r.date, date):
        date_str = r.date.isoformat()
    else:
        date_str = str(r.date)

    return {
        "date": date_str,
        "time": r.time,
        "people": r.people,
        "dishes": [
            {"id": d.id, "name": d.name, "price": d.price}
            for d in r.dishes
        ],
        "customer_name": r.customer_name,
        "phone": r.phone,
        "notes": r.notes,
    }


def _parse_date(value: Any) -> date:
    """
    Intenta interpretar la fecha aunque venga en formato raro.
    Preferimos 'YYYY-MM-DD', pero soportamos algún fallo típico.
    """

    if isinstance(value, str):
        try:
            return date.fromisoformat(value)
        except ValueError:
            try:
                dt = datetime.fromisoformat(value)
                return dt.date()
            except ValueError:
                pass

    if isinstance(value, dict):
        y = value.get("year")
        m = value.get("month")
        d = value.get("day")
        if y and m and d:
            return date(int(y), int(m), int(d))

    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value

    raise ValueError(f"Formato de fecha no soportado: {value!r}")


def dict_to_reservation(data: dict) -> Reservation:
    """Convierte un dict leído de JSON a una Reservation."""
    return Reservation(
        date=_parse_date(data["date"]),
        time=data["time"],
        people=data["people"],
        dishes=[Dish(**d) for d in data["dishes"]],
        customer_name=data.get("customer_name"),
        phone=data.get("phone"),
        notes=data.get("notes"),
    )


def load_reservations() -> List[Reservation]:
    """Carga todas las reservas desde el JSON. Si no existe, devuelve lista vacía."""
    if not STORAGE_FILE.exists():
        return []

    with STORAGE_FILE.open("r", encoding="utf-8") as f:
        raw = json.load(f)

    # raw debería ser una lista de dicts
    return [dict_to_reservation(item) for item in raw]


def save_reservations(reservations: List[Reservation]) -> None:
    """Guarda la lista completa de reservas en el JSON."""
    STORAGE_FILE.parent.mkdir(parents=True, exist_ok=True)

    data = [reservation_to_dict(r) for r in reservations]

    with STORAGE_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
