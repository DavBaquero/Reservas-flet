import flet as ft

# from View.appbar import create_appbar
import Model.login_model as login_model
import View.login as login_view
import View.venues as venues_view

def handle_vista_locales(e):
    page = e.page
    page.controls.clear()
    
    # Comprobar el estado de la sesión
    if login_model.check_active_session():
        # Si hay sesión (login falseado), ir a Locales
        venues_view.venues_view(page)
    else:
        # Si no hay sesión, volver a la vista de Login
        login_view.login_view(page)
    
    page.update()


def home_view(page: ft.Page):
    page.title = "Home App"
    
    # Voy a comentar esto porque si llama a eso cada vez que cargue la home
    # no va a poder mantener el cambio de tema dado que lo recarga
    # page.appbar = create_appbar()

    # Ocultamos la barra de desplazamiento
    # que se puede seguir usando
    page.scroll = "hidden"
    page.vertical_alignment = "start"
    page.horizontal_alignment = "start"
    # # Contenido de la página principal
    page.add(contenedor_bienvenida(page))
    page.update()

# Seccion de bienvenida
def contenedor_bienvenida(page: ft.Page):
    return ft.Container(
        width=page.width,
        height=page.height,
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
                    on_click=handle_vista_locales,
                    style=ft.ButtonStyle(
                        shape={"default": ft.RoundedRectangleBorder(radius=10)},
                        padding={"default": 20},
                    ),
                ),
                ft.Text(
                    "Tu reserva en un par de clics.",
                    size=14,
                ),
            ],
        ),
    )