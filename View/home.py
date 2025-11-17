import flet as ft

from View.appbar import create_appbar

def home_view(page: ft.Page):
    page.title = "Home App"
    page.appbar = create_appbar()
    page.scroll = "hidden"
    page.vertical_alignment = "start"

    
    texto = ft.Text("Bienvenido a la página principal", size=30)
    page.add(texto)
    page.update()
    