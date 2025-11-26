import flet as ft

import Model.user_model as user_model
import Controller.user_controller as user_controller
from View.appbar import create_appbar

user_id = 1  

def user_view(page: ft.Page):
    # Obtenemos el usuario y sacamos su correo
    user_data = user_model.get_user(user_id)
    user_email = user_data.get("email", "N/A")

    # Añadimos los contenidos de la vista
    user_info_container = ft.Container(
        col={"xs": 12, "sm": 10, "md": 8, "lg": 6, "xl": 4},
        content=ft.Column(
            controls=[
                ft.Text("Datos del Usuario", size=22, weight=ft.FontWeight.BOLD),
                ft.Divider(),
                # Definimos la primera parte de los datos de usuario
                ft.Row(
                    controls=[
                        ft.Text(
                            "Email:",
                            weight=ft.FontWeight.W_600,
                            width=120,
                            color=ft.Colors.ON_SURFACE,
                        ),
                        ft.TextField(
                            user_email,
                            read_only=True,
                            expand=1,
                        ),
                    ],
                ),
                # Definimos la segunda parte de los datos de usuario
                ft.Row(
                    controls=[
                        ft.Text(
                            "Estado:",
                            weight=ft.FontWeight.W_600,
                            width=120,
                            color=ft.Colors.ON_SURFACE,
                        ),
                        ft.Text("Activo", expand=1, color=ft.Colors.TERTIARY),
                    ],
                ),
                # Definimos la tercera parte de los datos de usuario
                ft.Row(
                    controls=[
                        ft.Text(
                            "Reservas:",
                            weight=ft.FontWeight.W_600,
                            width=120,
                            color=ft.Colors.ON_SURFACE,
                        ),
                        ft.ElevatedButton(
                            "Historial de reservas",
                            expand=1,
                            on_click=lambda e: user_controller.historial_reservas(e, user_id=user_id),
                        ),
                    ],
                ),

                ft.Divider(),
                # Definimos la última parte de los datos de usuario
                ft.Row(
                    controls=[
                        ft.ElevatedButton("Cambiar contraseña", expand=0, on_click=lambda e: user_controller.cambiar_contraseña(e,user_id=user_id))
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                
                ft.Row(
                    controls=[
                        ft.ElevatedButton("Cerrar sesión", expand=0, on_click=lambda e: user_controller.log_out(e, user_id))
                    ],
                    alignment=ft.MainAxisAlignment.END
                )
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.START,
            scroll=ft.ScrollMode.AUTO,
        ),
        alignment=ft.alignment.center,
        padding=20,
        bgcolor=ft.Colors.SURFACE, 
        border=ft.border.all(1, ft.Colors.with_opacity(0.3, ft.Colors.ON_SURFACE)),
        border_radius=12,
        shadow=ft.BoxShadow(blur_radius=8, spread_radius=1),
        width=500
    )
    
    # Devolvemos la vista, con el appbar y la ruta asignada
    return ft.View(
        appbar=create_appbar(page, show_back_button=True),
        route="/user",
        controls=[ft.Container(
            content=user_info_container,
            expand=True, 
            alignment=ft.alignment.center
        )],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll="hidden",
    )