import flet as ft

def create_appbar():
    home_button=ft.Container(
        content=ft.Text("Reservas Galvintec"),
        on_click=go_home,
        tooltip="Ir a la página de inicio", 
    )

    return ft.AppBar(
        title=home_button,
        bgcolor=ft.Colors.BLUE_GREY_700,
        actions=[
            ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED, on_click=change_theme),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Usuario", on_click=user_page),
                    ft.PopupMenuItem(),
                ],
            ),
        ],
    )

def change_theme(e):
    page = e.page
    if page.theme_mode == "light":
        page.theme_mode = "dark"
        e.control.icon = ft.Icons.NIGHTLIGHT_ROUND
    else:
        page.theme_mode = "light"
        e.control.icon = ft.Icons.WB_SUNNY_OUTLINED
    
    if page.theme_mode == "light":
        page.bgcolor = "#DBDADA"
        page.appbar.bgcolor = "#575757"
    else:
        page.bgcolor = "#1B1B1B"
        page.appbar.bgcolor = "#575757"
    page.update()

def user_page(e):
    import View.user as user_view
    page = e.page
    page.controls.clear()
    user_view.user_view(page)

def go_home(e):
    import View.home as home_view
    page = e.page
    page.controls.clear()
    home_view.home_view(page)