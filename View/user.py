import flet as ft


def user_view(page: ft.Page):
    page.title = "User Page"

    # Ocultamos la barra de desplazamiento
    # que se puede seguir usando
    
    page.scroll = "hidden"

    # Contenido de la página de usuario
    user_text = ft.Text("Welcome to the User Page", size=30)
    page.add(user_text)