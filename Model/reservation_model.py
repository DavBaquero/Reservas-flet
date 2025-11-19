from dataclasses import dataclass
from datetime import date
from typing import List, Optional


@dataclass
class Dish:
    """Plato del restaurante."""
    id: int
    name: str
    price: float


@dataclass
class Reservation:
    """
    Reserva sencilla: fecha, hora, nº personas y platos.
    """
    date: date          
    time: str          
    people: int
    dishes: List[Dish]

    customer_name: Optional[str] = None
    phone: Optional[str] = None
    notes: Optional[str] = None
