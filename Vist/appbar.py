import flet as ft
import Vist.user as user_view

def create_appbar():
    return ft.AppBar(
        title=ft.Text("Reservas Galvintec"),
        bgcolor=ft.Colors.BLUE_GREY_700,
        actions=[
            
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Usuario", on_click=user_page),
                    ft.PopupMenuItem(),
                ],
            ),
        ],
    )


def user_page(e):
    page = e.page
    page.controls.clear()
    user_view.user_view(page)