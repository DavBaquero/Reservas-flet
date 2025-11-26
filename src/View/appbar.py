import flet as ft
# import View.user as user_view
from View.reservation_view import ReservationView
from Model.reservation_model import Dish
from Controller.reservation_controller import ReservationController
from config import  LIGHT_APPBAR_BG, DARK_APPBAR_BG, LIGHT_BG, DARK_BG


def create_appbar(page: ft.Page, show_back_button: bool = False):
    color = ft.Colors.BLACK if page.theme_mode == "light" else ft.Colors.WHITE

    if not hasattr(page, '_theme_button'):
        page._theme_button = ft.IconButton(
            ft.Icons.WB_SUNNY_OUTLINED, 
            on_click=lambda e: change_theme(e, page._theme_button),
            icon_color=color,
        )
    else:
        page._theme_button.icon_color = color
        
    appbar = ft.AppBar(
        title=ft.Text("Reservas Galvintec", color=color),
        bgcolor=LIGHT_APPBAR_BG if page.theme_mode == "light" else DARK_APPBAR_BG,
        actions=[
            page._theme_button,
            ft.PopupMenuButton(
                icon_color=color,
                items=[
                    ft.PopupMenuItem(text="Home", on_click=lambda e: e.page.go("/")),
                    ft.PopupMenuItem(),
                    ft.PopupMenuItem(text="Usuario", on_click=lambda e: e.page.go("/user")),
                ],
            ),
        ],
    )
    
    if show_back_button:
        appbar.leading = ft.IconButton(
            icon=ft.Icons.ARROW_BACK,
            icon_color=color,
            on_click=lambda e: e.page.go("/")
        )
    
    return appbar

def change_theme(e, theme_button):
    page = e.page
    
    if page.theme_mode == "light":
        page.theme_mode = "dark"
        theme_button.icon = ft.Icons.NIGHTLIGHT_ROUND
        page.bgcolor = DARK_BG
    else:
        page.theme_mode = "light"
        theme_button.icon = ft.Icons.WB_SUNNY_OUTLINED
        page.bgcolor = LIGHT_BG

    if page.views:
        current_view = page.views[-1]
        current_view.appbar = create_appbar(page)

    page.update()