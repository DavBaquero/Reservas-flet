import flet as ft

import Model.register_model as register_model
import hashlib

# Controlador para manejar la lógica de registro
def register_button_clicked(e, username, password, password_confirm):
    page = e.page
    # Obtener los valores de los campos de entrada
    username_value = username.value
    password_value = password.value
    password_confirm_value = password_confirm.value

    # Limpiar mensajes de error
    username.error_text = None
    password.error_text = None
    password_confirm.error_text = None

    if not username_value:
        # Validar si el campo de nombre de usuario está vacío
        username.error_text = "Por favor, ingresa un nombre de usuario"
        page.update()
        return
    elif len(username_value) < 4:
        # Validar la longitud del nombre de usuario
        username.error_text = "El nombre de usuario debe tener al menos 4 caracteres"
        page.update()
        return
        
    if not password_value:
        # Validar si el campo de contraseña está vacío
        password.error_text = "Por favor, ingresa una contraseña"
        username.error_text = None
        page.update()
        return    
    elif len(password_value) < 6:
        # Validar la longitud de la contraseña
        password.error_text = "La contraseña debe tener al menos 6 caracteres"
        page.update()
        return

    if password_value != password_confirm_value:
        # Validar si las contraseñas coinciden
        password_confirm.error_text = "Las contraseñas no coinciden"
        password.error_text = None
        username.error_text = None
        page.update()
        return
    else:
        # Si todas las validaciones pasan, crear el usuario
        username.error_text = None
        password.error_text = None
        password_confirm.error_text = None

        # Encriptar la contraseña
        password_hashed = hashed_password(password_value)

        # Intentar crear el usuario en el modelo
        if not register_model.create_user(username_value, password_hashed):
            # Mostrar error si el usuario ya existe
            username.error_text = "El usuario ya existe"
            page.update()
            return
        # Si el usuario se crea correctamente, redirigir a la vista de inicio
        page.go("/")
# Función para encriptar la contraseña utilizando SHA-256
def hashed_password(password):
    return hashlib.sha256(password.encode()).hexdigest()