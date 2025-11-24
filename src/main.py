import flet as ft


from View.appbar import create_appbar
from View.login import login_view
import Model.login_model as login_model

from config import LIGHT_BG,LIGHT_APPBAR_BG,DARK_APPBAR_BG

def main(page: ft.Page):
    page.title = "Init App"
    
    # Selecciona un tema y fondo base 
    page.theme_mode = "light"
    page.bgcolor = LIGHT_BG

    page.theme = ft.Theme(color_scheme_seed = LIGHT_APPBAR_BG)
    page.dark_theme = ft.Theme(color_scheme_seed = DARK_APPBAR_BG)
    
    sesion = login_model.check_active_session()
    if not sesion:
        # Mostrar la vista de login,
        # Al no tener sesión iniciada.
        login_view(page)
        return
    else:
        page.appbar = create_appbar()
        from View.home import home_view
        home_view(page)
        return

ft.app(target=main)