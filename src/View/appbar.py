import flet as ft
# import View.user as user_view
from View.reservation_view import ReservationView
from Model.reservation_model import Dish
from Controller.reservation_controller import ReservationController


def create_appbar():
    return ft.AppBar(
        title=ft.Text("Reservas Galvintec"),
        bgcolor="#575757",
        actions=[
            ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED, on_click=change_theme),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Home", on_click=lambda e: e.page.go("/")),
                    ft.PopupMenuItem(),
                    ft.PopupMenuItem(text="Usuario", on_click=lambda e: e.page.go("/user")),
                    ft.PopupMenuItem(),
                    ft.PopupMenuItem(text="Reservas", on_click=lambda e: e.page.go("/venues")),
                ],
            ),
        ],
    )

def change_theme(e):
    #  Controlador para cambiar entre tema claro y oscuro
    page = e.page
    
    if page.theme_mode == "light":
        page.theme_mode = "dark"
        e.control.icon = ft.Icons.NIGHTLIGHT_ROUND
    else:
        page.theme_mode = "light"
        e.control.icon = ft.Icons.WB_SUNNY_OUTLINED
    
    if page.theme_mode == "light":
        page.bgcolor = "#DBDADA"
        if page.appbar:
            page.appbar.bgcolor = "#575757"
    else:
        page.bgcolor = "#1B1B1B"
        if page.appbar:
            page.appbar.bgcolor = "#030202"
    page.update()
