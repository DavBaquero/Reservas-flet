import flet as ft
import Model.login_model as login_model
from View.appbar import create_appbar

def home_view(page: ft.Page):
    # Vista que retorna un ft.View y no toca page directamente
    return ft.View(
        route="/",
        scroll="auto",
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.START,
        appbar= create_appbar(),
        controls=[
            ft.Container(
                alignment=ft.alignment.center,
                padding=30,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=25,
                    controls=[
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Icon(ft.Icons.CALENDAR_MONTH, size=60),
                                ft.Text(
                                    "Galvintec",
                                    size=55,
                                    weight=ft.FontWeight.BOLD,
                                ),
                            ],
                        ),
                        ft.Text(
                            "¡Bienvenido a Reservas Galvintec!",
                            size=40,
                            weight=ft.FontWeight.BOLD,
                            text_align=ft.TextAlign.CENTER,
                        ),
                        ft.Text(
                            "Tu plataforma confiable para gestionar tus citas y servicios de manera rápida y eficiente. ¡Empieza a reservar ahora!",
                            size=18,
                            text_align=ft.TextAlign.CENTER,
                            width=600,
                        ),
                        ft.FilledButton(
                            content=ft.Text(
                                "Comenzar reserva", size=18, weight=ft.FontWeight.BOLD
                            ),
                            on_click=lambda e: page.go("/venues")
                        ),
                        ft.Text("Tu reserva en un par de clics.", size=14),
                    ],
                ),
            )
        ],
    )
