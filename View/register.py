import flet as ft

def register_view(page: ft.Page):
    page.title = "Página de registro"
    page.scroll = "disable"

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    register_text = ft.Text("Regístrate", size=25)
    username_field = ft.TextField(label="Usuario", width=300)
    password_field = ft.TextField(label="Contraseña", width=300, password=True, can_reveal_password=True)
    password_confirm_field = ft.TextField(label="Confirmar Contraseña", width=300, password=True, can_reveal_password=True)
    register_button = ft.ElevatedButton(text="Registrarse", width=150)

    page.add(
        register_text,
        username_field,
        password_field,
        password_confirm_field,
        register_button
    )
    page.update()
    