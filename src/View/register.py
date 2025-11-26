import flet as ft
import Controller.register_controller as register_controller

def register_view(page: ft.Page):

    register_text = ft.Text("Regístrate", size=25)
    username_field = ft.TextField(label="Usuario", width=300)
    password_field = ft.TextField(
        label="Contraseña", width=300, password=True, can_reveal_password=True
    )
    password_confirm_field = ft.TextField(
        label="Confirmar Contraseña", width=300, password=True, can_reveal_password=True
    )

    register_button = ft.ElevatedButton(
        text="Registrarse",
        width=150,
        on_click=lambda e: register_controller.register_button_clicked(
            e, username_field, password_field, password_confirm_field
        ),
    )

    return ft.View(
        route="/register",
        controls=[
            ft.Column(
                [
                    register_text,
                    username_field,
                    password_field,
                    password_confirm_field,
                    register_button,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )