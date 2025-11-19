from __future__ import annotations
from Model.reservation_storage import load_reservations, save_reservations
from datetime import date, datetime
from typing import List, Optional, Set

from Model.reservation_model import Dish, Reservation


class ReservationController:
    """
    Controller de reservas: maneja estado y reglas de negocio.
    No sabe nada de Flet.
    """

    def __init__(self, dishes: List[Dish]):
        # La vista se inyecta luego
        self.view: Optional["ReservationView"] = None

        # Datos base
        self.available_dishes = dishes
        self.tables_total = 10
        self.seats_per_table = 4
        # Slots de horas permitidos para reservas
        self.available_slots: List[str] = [
            "12:00", "12:30", "13:00", "13:30",
            "14:00", "14:30", "15:00", "15:30",
            "21:00", "21:30", "22:00", "22:30", "23:00",
        ]

        # Estado actual del formulario
        self.selected_date: Optional[date] = None
        self.selected_time: Optional[str] = None
        self.people: int = 1
        self.selected_dish_ids: Set[int] = set()

        # "BD" en memoria
        self.reservations: List[Reservation] = load_reservations()


    def attach_view(self, view: "ReservationView") -> None:
        self.view = view


    # Eventos de la vista
    def on_date_changed(self, new_date: Optional[date]) -> None:
        if self.view is None:
            return

        if new_date is None:
            self.selected_date = None
            self.view.show_status("No se ha seleccionado fecha.", error=True)
            return

        #  Normalizar a datetime.date
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
            self.view.show_status("El número de personas debe ser mayor que 0.", error=True)
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

        # Validaciones
        if self.selected_date is None:
            self.view.show_status("Selecciona una fecha antes de confirmar.", error=True)
            return

        if self.selected_time is None:
            self.view.show_status("Selecciona una hora antes de confirmar.", error=True)
            return

        if self.people <= 0:
            self.view.show_status("El número de personas debe ser mayor que 0.", error=True)
            return

        if not self.selected_dish_ids:
            self.view.show_status("Selecciona al menos un plato.", error=True)
            return

        # No permitir dos reservas mismo día + misma hora
        max_capacity = self.tables_total * self.seats_per_table
        used = self._seats_used_in_slot(self.selected_date, self.selected_time)

        if used + self.people > max_capacity:
            self.view.show_status(
                f"No hay mesas disponibles para el "
                f"{self.selected_date.strftime('%d/%m/%Y')} a las {self.selected_time}. "
                f"Aforo máximo {max_capacity} personas por turno.",
                error=True,
            )
            return

        # Obtener objetos Dish seleccionados
        dishes_map = {d.id: d for d in self.available_dishes}
        selected_dishes = [
            dishes_map[d_id]
            for d_id in self.selected_dish_ids
            if d_id in dishes_map
        ]

        # Crear reserva
        reservation = Reservation(
            date=self.selected_date,
            time=self.selected_time,
            people=self.people,
            dishes=selected_dishes,
        )
        self.reservations.append(reservation)
        save_reservations(self.reservations)

        platos_txt = ", ".join(d.name for d in selected_dishes)
        self.view.show_status(
            f"Reserva confirmada para el "
            f"{self.selected_date.strftime('%d/%m/%Y')} a las {self.selected_time} "
            f"({self.people} personas). Platos: {platos_txt}",
            error=False,
        )

        # Reset formulario
        self.view.reset_form()
        self.selected_date = None
        self.selected_time = None
        self.selected_dish_ids.clear()
        self.people = 1


    def _seats_used_in_slot(self, date_: date, time_str: str) -> int:
        """
        Devuelve cuántas personas hay ya reservadas en un (día, hora).
        """
        return sum(
            r.people
            for r in self.reservations
            if r.date == date_ and r.time == time_str
        )
