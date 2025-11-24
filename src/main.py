import flet as ft
from Controller.router import route_change, view_pop
import Model.login_model as login_model

def main(page: ft.Page):
    page.title = "Reservas Galvintec"
    page.theme_mode = "light"
    page.bgcolor = "#DBDADA"

    page.on_route_change = lambda r: route_change(page)
    page.on_view_pop = lambda v: view_pop(page)

    # Navegación inicial según sesión
    if login_model.check_active_session():
        page.go("/")
    else:
        page.go("/login")

ft.app(target=main)
