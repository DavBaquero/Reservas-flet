import flet as ft
import Controller.login_controller as login_controller
def login_view(page: ft.Page):
    page.controls.clear()
    page.title = "Login Page"
    page.scroll = "disable"

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    login_text = ft.Text("¿Tienes cuenta? Inicia sesión", size=25)
    login_field = ft.TextField(label="Usuario", width=300)
    password_field = ft.TextField(label="Contraseña", width=300, password=True, can_reveal_password=True)
    login_button = ft.ElevatedButton(text="Iniciar Sesión", width=150, on_click=check_login)
    separator = ft.Divider(height=20)
    signup_text = ft.Text("¿No tienes cuenta? Regístrate", size=25)
    signup_button = ft.ElevatedButton(text="Registrarse", width=150, on_click=login_controller.register_button_clicked)

    page.add(
        login_text,
        login_field,
        password_field,
        login_button,
        separator,
        signup_text,
        signup_button
    )
    page.update()

def check_login(e):
    login_field = e.page.controls[1]
    password_field = e.page.controls[2]
    if login_field.value == "" or login_field.value is None: 
        login_field.error_text = "Por favor, ingresa tu usuario"
    elif password_field.value == "" or password_field.value is None:
        login_field.error_text = None
        password_field.error_text = "Por favor, ingresa tu contraseña"
    else:
        login_controller.login_button_clicked(e)
    e.page.update()