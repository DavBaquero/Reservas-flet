# Model/reservation_model.py
from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional


@dataclass
class Dish:
    id: int
    name: str
    price: float


@dataclass
class Reservation:
    date: date
    time: str
    people: int
    dishes: List[Dish] = field(default_factory=list)

    customer_name: Optional[str] = None
    phone: Optional[str] = None
    notes: Optional[str] = None
    user_id: Optional[int] = None
