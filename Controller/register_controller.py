import flet as ft

from View.home import home_view
import Model.register_model as register_model
import hashlib

def register_button_clicked(e, username, password, password_confirm):
    page = e.page
    username_value = username.value
    password_value = password.value
    password_confirm_value = password_confirm.value

    username.error_text = None
    password.error_text = None
    password_confirm.error_text = None

    if not username_value:
        username.error_text = "Por favor, ingresa un nombre de usuario"
        page.update()
        return
    elif len(username_value) < 4:
        username.error_text = "El nombre de usuario debe tener al menos 4 caracteres"
        page.update()
        return
        
    if not password_value:
        password.error_text = "Por favor, ingresa una contraseña"
        username.error_text = None
        page.update()
        return    
    elif len(password_value) < 6:
        password.error_text = "La contraseña debe tener al menos 6 caracteres"
        page.update()
        return

    if password_value != password_confirm_value:
        password_confirm.error_text = "Las contraseñas no coinciden"
        password.error_text = None
        username.error_text = None
        page.update()
        return
    else:
        username.error_text = None
        password.error_text = None
        password_confirm.error_text = None
        password_hashed = hashed_password(password_value)
        if not register_model.create_user(username_value, password_hashed):
            username.error_text = "El usuario ya existe"
            page.update()
            return
        page.controls.clear()
        home_view(page)
        page.update()

def hashed_password(password):
    return hashlib.sha256(password.encode()).hexdigest()