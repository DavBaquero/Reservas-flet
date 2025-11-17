import flet as ft

from View.appbar import create_appbar
from View.login import login_view

def main(page: ft.Page):
    page.title = "Flet Counter App"
    page.scroll = "auto"
    page.appbar = create_appbar()
    
    sesion = False  # Simulando una sesión activa
    if not sesion:
        login_view(page)
        return
        
    texto = ft.Text("Para ver", size=30)

    page.add(texto)

ft.app(target=main)