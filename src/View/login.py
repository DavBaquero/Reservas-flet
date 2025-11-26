import flet as ft
import Controller.login_controller as login_controller

def login_view(page: ft.Page):

    # Definimos los campos de la página
    login_text = ft.Text("¿Tienes cuenta? Inicia sesión", size=25)
    login_field = ft.TextField(label="Usuario", width=300)
    password_field = ft.TextField(label="Contraseña", width=300, password=True, can_reveal_password=True)
    login_button = ft.ElevatedButton(
        text="Iniciar Sesión",
        width=150,
        on_click=lambda e: login_controller.login_button_clicked(
            e, login_field, password_field
        )
    )

    separator = ft.Divider(height=20)

    signup_text = ft.Text("¿No tienes cuenta? Regístrate", size=25)
    signup_button = ft.ElevatedButton(
        text="Registrarse",
        width=150,
        on_click=login_controller.register_button_clicked
    )

    # Devolvemos todo como un View al cual le hemos asignado su ruta
    return ft.View(
        route="/login",
        controls=[
            ft.Column(
                [
                    login_text,
                    login_field,
                    password_field,
                    login_button,
                    separator,
                    signup_text,
                    signup_button,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )