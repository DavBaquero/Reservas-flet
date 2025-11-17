import flet as ft

from View.home import home_view

def register_button_clicked(e, username, password, password_confirm):
    page = e.page
    username_value = username.value
    password_value = password.value
    password_confirm_value = password_confirm.value

    if not username_value:
        username.error_text = "Por favor, ingresa un nombre de usuario"
        page.update()
        return
    elif not password_value:
        password.error_text = "Por favor, ingresa una contraseña"
        username.error_text = None
        page.update()
        return
    elif password_value != password_confirm_value:
        password_confirm.error_text = "Las contraseñas no coinciden"
        password.error_text = None
        username.error_text = None
        page.update()
        return
    else:
        username.error_text = None
        password.error_text = None
        password_confirm.error_text = None
        page.controls.clear()
        home_view(page)
        page.update()