import flet as ft

import View.home as home_view
import View.register as register_view
import Model.login_model as login_model
import hashlib

# Controlador para manejar la lógica de inicio de sesión
def login_button_clicked(e, login_field, password_field):
    page = e.page

    # Obtener los valores de los campos de entrada
    username_value = login_field.value
    password_value = password_field.value

    # Encriptar la contraseña
    hashed_password = hash_password(password_value)
    login_field.error_text = None
    password_field.error_text = None
    
    # Validar el nombre de usuario
    if not username_value:
        # Si el campo de nombre de usuario está vacío, mostrar un mensaje de error
        login_field.error_text = "Por favor, ingresa un nombre de usuario"
        page.update()
        return
    elif len(username_value) < 4:
        # Validar la longitud del nombre de usuario
        login_field.error_text = "El nombre de usuario debe tener al menos 4 caracteres"
        page.update()
        return
    elif not login_model.validate_user_exists(username_value):
        # Validar si el usuario existe
        login_field.error_text = "El usuario no existe"
        page.update()
        return

    # Validar la contraseña
    if not password_value:
        # Si el campo de contraseña está vacío, mostrar un mensaje de error
        password_field.error_text = "Por favor, ingresa una contraseña"
        login_field.error_text = None
        page.update()
        return
    elif len(password_value) < 6:
        # Validar la longitud de la contraseña
        password_field.error_text = "La contraseña debe tener al menos 6 caracteres"
        page.update()
        return
    elif not login_model.validate_login(username_value, hashed_password):
        # Validar si la contraseña es correcta
        password_field.error_text = "Contraseña incorrecta"
        login_field.error_text = None
        page.update()
        return
    
    # Si todas las validaciones pasan, iniciar sesión
    if login_model.validate_login(username_value, hashed_password):
        login_field.error_text = None
        password_field.error_text = None
        page.controls.clear()
        home_view.home_view(page)
        page.update()

# Controlador para manejar la lógica de registro
def register_button_clicked(e):
    page = e.page
    page.controls.clear()
    register_view.register_view(page)
    page.update()

# Función para encriptar la contraseña utilizando SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()