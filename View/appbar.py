import flet as ft
# import View.user as user_view
from View.reservation_view import ReservationView
from Model.reservation_model import Dish
from Controller.reservation_controller import ReservationController

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
                    ft.PopupMenuItem(),
                    ft.PopupMenuItem(text="Usuario", on_click=user_page), # Acceso a la página de usuario
                    ft.PopupMenuItem(),
                    ft.PopupMenuItem(text="Reservas", on_click=reservation_page), # Acceso a la página de reservas
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
    
def reservation_page(e):
    page = e.page
    page.controls.clear()

    # Platos "hardcodeados" igual que en main
    dishes = [
        Dish(id=1, name="Menú del día", price=12.50),
        Dish(id=2, name="Hamburguesa", price=9.90),
        Dish(id=3, name="Pizza Margarita", price=10.50),
        Dish(id=4, name="Ensalada César", price=8.00),
    ]

    controller = ReservationController(dishes=dishes)
    # Esto construye toda la vista de reservas en la página
    ReservationView(page=page, controller=controller)

    page.update()

def go_home(e):
    import View.home as home_view
    page = e.page
    page.controls.clear()
    home_view.home_view(page)
