# Controller/reservation_controller.py
from __future__ import annotations

from datetime import date, datetime
from typing import List, Optional, Set, TYPE_CHECKING

from Model.reservation_model import Dish, Reservation
from Model.reservation_storage_db import load_reservations, save_reservation

if TYPE_CHECKING:
    from View.reservation_view import ReservationView


class ReservationController:


    def __init__(self, dishes: List[Dish], user_id: int | None = None):
        self.view: Optional[ReservationView] = None

        self.available_dishes = dishes
        self.user_id = user_id

        self.tables_total = 10
        self.seats_per_table = 4
        self.max_tables_per_reservation = 3

        self.available_slots: List[str] = [
            "12:00", "12:30", "13:00", "13:30",
            "14:00", "14:30", "15:00", "15:30",
            "21:00", "21:30", "22:00", "22:30", "23:00",
        ]

        self.selected_date: Optional[date] = None
        self.selected_time: Optional[str] = None
        self.people: int = 1
        self.selected_dish_ids: Set[int] = set()

        self.reservations: List[Reservation] = load_reservations()


    def attach_view(self, view: "ReservationView") -> None:
        self.view = view


    def _tables_for_people(self, people: int) -> int:

        if people <= 0:
            return 0

        mesas = (people + self.seats_per_table - 1) // self.seats_per_table
        return min(mesas, self.max_tables_per_reservation)

    def _tables_used_in_slot(self, date_: date, time_str: str) -> int:

        total = 0
        for r in self.reservations:
            if r.date == date_ and r.time == time_str:
                total += self._tables_for_people(r.people)
        return total


    def on_date_changed(self, new_date: Optional[date | datetime | str]) -> None:
        if self.view is None:
            return

        if new_date is None:
            self.selected_date = None
            self.view.show_status("No se ha seleccionado fecha.", error=True)
            return

        if isinstance(new_date, datetime):
            new_date = new_date.date()
        elif isinstance(new_date, str):
            try:
                new_date = date.fromisoformat(new_date)
            except ValueError:
                self.selected_date = None
                self.view.show_status("Fecha no válida.", error=True)
                return

        self.selected_date = new_date
        self.view.show_status(
            f"Fecha seleccionada: {new_date.strftime('%d/%m/%Y')}",
            error=False,
        )

    def on_time_changed(self, time_str: Optional[str]) -> None:
        if self.view is None:
            return

        if not time_str:
            self.selected_time = None
            self.view.show_status("Selecciona una hora.", error=True)
            return

        if time_str not in self.available_slots:
            self.selected_time = None
            self.view.show_status("Hora no válida.", error=True)
            return

        self.selected_time = time_str
        self.view.show_status(f"Hora seleccionada: {time_str}", error=False)

    def on_people_changed(self, people: int) -> None:
        if self.view is None:
            return

        if people <= 0:
            self.view.show_status(
                "El número de personas debe ser mayor que 0.", error=True
            )
            return

        max_people_per_reservation = (
            self.max_tables_per_reservation * self.seats_per_table
        )
        if people > max_people_per_reservation:
            self.view.show_status(
                f"Máximo {max_people_per_reservation} personas por reserva "
                f"({self.max_tables_per_reservation} mesas).",
                error=True,
            )
            return

        self.people = people
        self.view.show_status(f"Número de personas: {people}", error=False)

    def on_dish_toggled(self, dish_id: int, checked: bool) -> None:
        if self.view is None:
            return

        if checked:
            self.selected_dish_ids.add(dish_id)
        else:
            self.selected_dish_ids.discard(dish_id)

        if not self.selected_dish_ids:
            self.view.show_status("No hay platos seleccionados.", error=True)
        else:
            self.view.show_status(
                f"Platos seleccionados: {len(self.selected_dish_ids)}",
                error=False,
            )

    def on_confirm_clicked(self) -> None:
        if self.view is None:
            return

        if self.selected_date is None:
            self.view.show_status(
                "Selecciona una fecha antes de confirmar.", error=True
            )
            return

        if self.selected_time is None:
            self.view.show_status(
                "Selecciona una hora antes de confirmar.", error=True
            )
            return

        if self.people <= 0:
            self.view.show_status(
                "El número de personas debe ser mayor que 0.", error=True
            )
            return

        max_people_per_reservation = (
            self.max_tables_per_reservation * self.seats_per_table
        )
        if self.people > max_people_per_reservation:
            self.view.show_status(
                f"Máximo {max_people_per_reservation} personas por reserva "
                f"({self.max_tables_per_reservation} mesas).",
                error=True,
            )
            return

        if not self.selected_dish_ids:
            self.view.show_status(
                "Selecciona al menos un plato.", error=True
            )
            return

        max_tables = self.tables_total
        used_tables = self._tables_used_in_slot(
            self.selected_date, self.selected_time
        )
        new_tables = self._tables_for_people(self.people)

        if used_tables + new_tables > max_tables:
            self.view.show_status(
                f"No hay mesas disponibles para el "
                f"{self.selected_date.strftime('%d/%m/%Y')} a las {self.selected_time}. "
                f"Mesas ya ocupadas: {used_tables}/{max_tables}. "
                f"Tu reserva necesita {new_tables} mesa(s).",
                error=True,
            )
            return

        dishes_map = {d.id: d for d in self.available_dishes}
        selected_dishes = [
            dishes_map[d_id]
            for d_id in self.selected_dish_ids
            if d_id in dishes_map
        ]

        reservation = Reservation(
            date=self.selected_date,
            time=self.selected_time,
            people=self.people,
            dishes=selected_dishes,
            user_id=self.user_id or 1,
        )

        self.reservations.append(reservation)
        save_reservation(reservation)

        platos_txt = ", ".join(d.name for d in selected_dishes)
        self.view.show_status(
            f"Reserva confirmada para el "
            f"{self.selected_date.strftime('%d/%m/%Y')} a las {self.selected_time} "
            f"({self.people} personas, {self._tables_for_people(self.people)} mesa(s)). "
            f"Platos: {platos_txt}",
            error=False,
        )

        self.view.reset_form()
        self.selected_date = None
        self.selected_time = None
        self.selected_dish_ids.clear()
        self.people = 1
