import flet as ft

import View.home as home_view
import View.register as register_view

def login_button_clicked(e, login_field, password_field):
    page = e.page
    username_value = login_field.value
    password_value = password_field.value
    if not username_value:
        login_field.error_text = "Por favor, ingresa un nombre de usuario"
        page.update()
        return
    elif not password_value:
        password_field.error_text = "Por favor, ingresa una contraseña"
        login_field.error_text = None
        page.update()
        return
    else:
        login_field.error_text = None
        password_field.error_text = None
        page.controls.clear()
        home_view.home_view(page)
        page.update()

def register_button_clicked(e):
    page = e.page
    page.controls.clear()
    register_view.register_view(page)
    page.update()