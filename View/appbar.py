import flet as ft

def create_appbar():
    # Crea una barra de aplicaciones personalizada 
    return ft.AppBar(
        title=ft.Text("Reservas Galvintec"),
        bgcolor=ft.Colors.BLUE_GREY_700,
        actions=[
            ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED, on_click=change_theme), #  para cambiar el tema claro/oscuro
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Home", on_click=go_home), # Acceso a la página principal
                    ft.PopupMenuItem(text="Usuario", on_click=user_page), # Acceso a la página de usuario
                ],
            ),
        ], # Acciones de la barra de aplicaciones
    )

def change_theme(e):
    #  Controlador para cambiar entre tema claro y oscuro
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

#  Controlador para navegar a la página de usuario
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