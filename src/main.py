import flet as ft
from Controller.router import route_change, view_pop
import Model.login_model as login_model
from config.app_theme import theme_light, theme_dark

def main(page: ft.Page):
    page.title = "Reservas Galvintec"

    page.theme = theme_light
    page.dark_theme = theme_dark
    
    page.theme_mode = ft.ThemeMode.LIGHT

    page.on_route_change = lambda r: route_change(page)
    page.on_view_pop = lambda v: view_pop(page)

    # Navegación inicial según sesión
    if login_model.check_active_session():
        page.go("/")
    else:
        page.go("/login")

ft.app(target=main)
