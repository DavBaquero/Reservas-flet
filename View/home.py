import flet as ft

from View.appbar import create_appbar

def home_view(page: ft.Page):
    page.title = "Home App"
    page.appbar = create_appbar()
    
    # Ocultamos la barra de desplazamiento
    # que se puede seguir usando
    
    page.scroll = "hidden"
    page.vertical_alignment = "start"

    # # Contenido de la página principal
    texto = ft.Text("Bienvenido a la página principal", size=30)
    page.add(texto)
    page.update()
    