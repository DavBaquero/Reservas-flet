import flet as ft
from Controller.router import route_change, view_pop
from Model.user_model import get_theme
import Model.login_model as login_model
from config.app_theme import theme_light, theme_dark

user_id = 1 #falseado

def main(page: ft.Page):
    page.title = "Reservas Galvintec"

    # Con esto asigno las paletas de colores creadas por mi
    page.theme = theme_light
    page.dark_theme = theme_dark

    # De esta manero hago la persistencia del modo claro o el modo oscuro
    valor = get_theme(user_id)
    if valor[0] == 1:
        page.theme_mode = ft.ThemeMode.DARK
    else:
        page.theme_mode = ft.ThemeMode.LIGHT

    # Con esto manejamos la url y la muestra de los views
    page.on_route_change = lambda r: route_change(page)
    page.on_view_pop = lambda v: view_pop(page)

    # Navegación inicial según sesión
    if login_model.check_active_session():
        page.go("/")
    else:
        page.go("/login")

ft.app(target=main)
