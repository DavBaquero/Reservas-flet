import flet as ft

from View.appbar import create_appbar
from View.login import login_view

def main(page: ft.Page):
    page.title = "Init App"
    page.appbar = create_appbar()
    
    sesion = False  # Simulando una sesión activa
    if not sesion:
        login_view(page)
        return


ft.app(target=main)