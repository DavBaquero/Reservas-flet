import flet as ft


def venues_view(page: ft.Page):
    page.title = "Página de locales"
    page.horizontal_alignment = "start"
    # Ocultamos la barra de desplazamiento
    # que se puede seguir usando
    
    page.scroll = "hidden"

    # Contenido de la página de usuario
    user_text = ft.Text("Texto genérico de la página de locales", size=30)
    page.add(user_text)