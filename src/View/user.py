import flet as ft

import Model.user_model as user_model
import Controller.user_controller as user_controller
from View.appbar import create_appbar

user_id = 1  # Simulando un ID de usuario obtenido después del login

def user_view(page: ft.Page):

    user_info_container = ft.Row(
        controls=[
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(
                            "Datos del Usuario",
                            size=22,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.BLACK,
                        ),
                        ft.Divider(),
                        ft.Row(
                            controls=[
                                ft.Text(
                                    "Email:",
                                    weight=ft.FontWeight.W_600,
                                    width=50,
                                    color=ft.Colors.BLACK,
                                ),
                                ft.TextField(
                                    user_model.get_user(user_id)["email"],
                                    read_only=True,
                                    expand=1,
                                    color=ft.Colors.BLACK,
                                ),
                            ],
                        ),
                        ft.Row(
                            controls=[
                                ft.Text(
                                    "Estado:",
                                    weight=ft.FontWeight.W_600,
                                    width=120,
                                    color=ft.Colors.BLACK,
                                ),
                                ft.Text("Activo", expand=1, color=ft.Colors.GREEN_700),
                            ]
                        ),
                        ft.Row(
                            controls=[
                                ft.Text(
                                    "Reservas:",
                                    weight=ft.FontWeight.W_600,
                                    width=120,
                                    color=ft.Colors.BLACK,
                                ),
                                ft.ElevatedButton(
                                    "Historial de reservas",
                                    expand=1,
                                    on_click=lambda e: user_controller.historial_reservas(
                                        e, user_id=user_id
                                    ),
                                ),
                            ]
                        ),
                    ],
                    spacing=20,
                    alignment=ft.MainAxisAlignment.START,
                    height=300,
                    expand=True,
                ),
                alignment=ft.alignment.center,
                padding=20,
                bgcolor=ft.Colors.WHITE,
                border=ft.border.all(1, ft.Colors.GREY_300),
                border_radius=12,
                shadow=ft.BoxShadow(blur_radius=8, spread_radius=1),
                width=600,
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        expand=True,
    )

    return ft.View(
        appbar=create_appbar(),
        route="/user",
        controls=[user_info_container],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll="hidden",
    )
