import flet as ft

import Model.user_model as user_model
import Controller.user_controller as user_controller

user_id = 1  # Simulando un ID de usuario obtenido después del login
def user_view(page: ft.Page):
    page.title = "User Page"

    # Ocultamos la barra de desplazamiento
    # que se puede seguir usando
    
    page.scroll = "hidden"

    grid = ft.ResponsiveRow(
        run_spacing=10, 
        spacing=5,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.START,
    )

    user_info_container = ft.Container(
        col={"xs": 12, "sm": 10, "md": 8, "lg": 6, "xl": 4},
        content=ft.Column(
            controls=[
                ft.Text("Datos del Usuario", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                ft.Divider(),
                ft.Row(
                    controls=[
                        ft.Text("Email:", weight=ft.FontWeight.W_600, color=ft.Colors.BLACK),
                        ft.TextField(user_model.get_user(user_id)["email"], read_only=True, expand=1, color=ft.Colors.BLACK),
                    ],
                ),
                ft.Row(
                    controls=[
                        ft.Text("Estado:", weight=ft.FontWeight.W_600, color=ft.Colors.BLACK),
                        ft.Text("Activo", expand=1, color=ft.Colors.GREEN_700),
                    ],
                ),
                ft.Row(
                    controls=[
                        ft.Text("Reservas:", weight=ft.FontWeight.W_600, color=ft.Colors.BLACK),
                        ft.ElevatedButton("Historial de reservas", expand=1, on_click=lambda e: user_controller.historial_reservas(e, user_id=user_id)),
                    ],
                ),
                ft.Divider(),
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
        bgcolor=ft.Colors.WHITE,
        border=ft.border.all(1, ft.Colors.GREY_300),
        border_radius=12,
        shadow=ft.BoxShadow(blur_radius=8, spread_radius=1),
    )
    
    grid.controls.append(user_info_container)

    page.add(grid)
