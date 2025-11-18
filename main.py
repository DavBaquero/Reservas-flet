import flet as ft

from View.appbar import create_appbar
from View.login import login_view

def main(page: ft.Page):
    page.title = "Init App"
    
    # Crear la barra de navegación. Esto se va a quitar
    # después de implementar el login todos.
    page.appbar = create_appbar()
    
    sesion = False 
    if not sesion:
        # Mostrar la vista de login,
        # Al no tener sesión iniciada.
        login_view(page)
        return


ft.app(target=main)