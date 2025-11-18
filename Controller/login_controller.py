import flet as ft

import View.home as home_view
import View.register as register_view
import Model.login_model as login_model
import hashlib

def login_button_clicked(e, login_field, password_field):
    page = e.page
    username_value = login_field.value
    password_value = password_field.value

    hashed_password = hash_password(password_value)
    login_field.error_text = None
    password_field.error_text = None
    
    if not username_value:
        login_field.error_text = "Por favor, ingresa un nombre de usuario"
        page.update()
        return
    elif len(username_value) < 4:
        login_field.error_text = "El nombre de usuario debe tener al menos 4 caracteres"
        page.update()
        return
    elif not login_model.validate_user_exists(username_value):
        login_field.error_text = "El usuario no existe"
        page.update()
        return

 
    if not password_value:
        password_field.error_text = "Por favor, ingresa una contraseña"
        login_field.error_text = None
        page.update()
        return
    elif len(password_value) < 6:
        password_field.error_text = "La contraseña debe tener al menos 6 caracteres"
        page.update()
        return
    elif not login_model.validate_login(username_value, hashed_password):
        password_field.error_text = "Contraseña incorrecta"
        login_field.error_text = None
        page.update()
        return
    
    if login_model.validate_login(username_value, hashed_password):
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

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()