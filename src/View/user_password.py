import flet as ft 
from Controller.user_password_controller import confirmation, close_dialog
def create_dialog(user_id):
    dialog = ft.AlertDialog(
        title=ft.Text("Cambiar contraseña"),
        content=ft.Container(
            width=300,
            height=200,
            expand=True,
            content=ft.Column([
                ft.TextField(label="Contraseña actual", password=True, can_reveal_password=True),
                ft.TextField(label="Nueva contraseña", password=True, can_reveal_password=True),
                ft.TextField(label="Repite la nueva contraseña", password=True, can_reveal_password=True)
            ])   
        ),
        actions=[
            ft.ElevatedButton("Guardar", on_click=lambda e: confirmation(e, dialog, user_id=user_id)),
            ft.ElevatedButton("Cerrar", on_click=lambda e: close_dialog(e,dialog),)
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    return dialog

