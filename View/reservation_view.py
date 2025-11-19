import datetime
from typing import Dict, List

import flet as ft

from Model.reservation_model import Dish
from Controller.reservation_controller import ReservationController


class ReservationView:
    """
    Vista Flet para gestionar reservas del restaurante.
    Construye la UI y delega la lógica en el controller.
    """

    def __init__(self, page: ft.Page, controller: ReservationController):
        self.page = page
        self.controller = controller

        self.controller.attach_view(self)

        self.page.title = "Reservas restaurante"
        self.page.vertical_alignment = ft.MainAxisAlignment.START

        self.status_text = ft.Text("")

        today = datetime.date.today()
        max_date = today + datetime.timedelta(days=14)

        self.date_picker = ft.DatePicker(
            first_date=today,
            last_date=max_date,
            on_change=self._on_date_change,
            on_dismiss=self._on_date_dismiss,
        )

        pick_date_button = ft.ElevatedButton(
            "Elegir fecha",
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda e: self.page.open(self.date_picker),
        )

        self.time_dropdown = ft.Dropdown(
            label="Hora",
            width=150,
            value=None, 
            options=[
                ft.dropdown.Option(slot)
                for slot in self.controller.available_slots
            ],
            on_change=self._on_time_change,
        )

        self.people_dropdown = ft.Dropdown(
            label="Número de personas",
            width=150,
            value="1",
            options=[ft.dropdown.Option(str(i)) for i in range(1, 11)],
            on_change=self._on_people_change,
        )

        self.dish_checkboxes: Dict[int, ft.Checkbox] = {}
        dish_controls: List[ft.Control] = [
            ft.Text("Elige qué vais a comer:", weight=ft.FontWeight.BOLD)
        ]

        for dish in self.controller.available_dishes:
            cb = ft.Checkbox(
                label=f"{dish.name} - {dish.price:.2f} €",
                value=False,
            )
            cb.on_change = self._make_dish_handler(dish.id)
            self.dish_checkboxes[dish.id] = cb
            dish_controls.append(cb)

        menu_section = ft.Column(controls=dish_controls)

        confirm_button = ft.ElevatedButton(
            "Confirmar reserva",
            icon=ft.Icons.CHECK,
            on_click=self._on_confirm_click,
        )

        root = ft.Column(
            controls=[
                ft.Text("Reservas Galvintec", size=24, weight=ft.FontWeight.BOLD),
                ft.Row(
                    controls=[
                        pick_date_button,
                        self.time_dropdown,
                        self.people_dropdown,
                    ]
                ),
                ft.Divider(),
                menu_section,
                ft.Divider(),
                confirm_button,
                self.status_text,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.START,
        )

        self.page.controls.clear()
        self.page.add(root)
        self.page.update()


    def _on_date_change(self, e: ft.ControlEvent) -> None:
        self.controller.on_date_changed(e.control.value)

    def _on_date_dismiss(self, e: ft.ControlEvent) -> None:
        self.show_status("No se ha seleccionado ninguna fecha.", error=False)

    def _on_time_change(self, e: ft.ControlEvent) -> None:
        time_str = e.control.value
        self.controller.on_time_changed(time_str)

    def _on_people_change(self, e: ft.ControlEvent) -> None:
        raw = e.control.value
        try:
            people = int(raw)
        except (TypeError, ValueError):
            self.show_status("Número de personas no válido.", error=True)
            return
        self.controller.on_people_changed(people)

    def _make_dish_handler(self, dish_id: int):
        def handler(e: ft.ControlEvent):
            checked = bool(e.control.value)
            self.controller.on_dish_toggled(dish_id, checked)

        return handler

    def _on_confirm_click(self, e: ft.ControlEvent) -> None:
        self.controller.on_confirm_clicked()


    def show_status(self, message: str, error: bool = False) -> None:
        self.status_text.value = message
        self.status_text.color = ft.Colors.RED if error else ft.Colors.GREEN
        self.page.update()

    def reset_form(self) -> None:
        for cb in self.dish_checkboxes.values():
            cb.value = False
        self.time_dropdown.value = None
        self.people_dropdown.value = "1"
        self.page.update()
