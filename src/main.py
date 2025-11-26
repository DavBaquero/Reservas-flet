import flet as ft


from View.appbar import create_appbar
from View.login import login_view
import Model.login_model as login_model
from config.app_theme import theme_light, theme_dark

def main(page: ft.Page):
    page.title = "Init App"
    
    page.theme = theme_light

    page.dark_theme = theme_dark

    page.theme_mode = ft.ThemeMode.LIGHT
    
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