import flet as ft

from Model.user_model import change_theme as bd_theme

user_id = 1 #Falseamos el id

def create_appbar(page: ft.Page, show_back_button: bool = False):
    if not hasattr(page, '_theme_button'):
        initial_icon = ft.Icons.NIGHTLIGHT_ROUND if page.theme_mode == ft.ThemeMode.LIGHT else ft.Icons.WB_SUNNY_OUTLINED
        
        page._theme_button = ft.IconButton(
            initial_icon, 
            on_click=lambda e: change_theme(e, page._theme_button),
        )

    appbar = ft.AppBar(
        title=ft.Text("Reservas Galvintec"),
        actions=[
            page._theme_button,
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Home", on_click=lambda e: e.page.go("/")),
                    ft.PopupMenuItem(),
                    ft.PopupMenuItem(text="Usuario", on_click=lambda e: e.page.go("/user")),
                ],
            ),
        ],
    )
    
    if show_back_button:
        appbar.leading = ft.IconButton(
            icon=ft.Icons.ARROW_BACK,
            # Eliminar icon_color codificado. Usará ON_PRIMARY del tema.
            on_click=lambda e: e.page.go("/")
        )
    
    return appbar

def change_theme(e, theme_button):
    page = e.page
    
    if page.theme_mode == ft.ThemeMode.LIGHT:
        page.theme_mode = ft.ThemeMode.DARK
        theme_button.icon = ft.Icons.WB_SUNNY_OUTLINED 
        theme_change(page.theme_mode.value, user_id)
    else:
        page.theme_mode = ft.ThemeMode.LIGHT
        theme_button.icon = ft.Icons.NIGHTLIGHT_ROUND
        theme_change(page.theme_mode.value, user_id)

    if page.views:
        current_view = page.views[-1]
        current_view.appbar = create_appbar(page, show_back_button=current_view.route != "/")

    page.update()

    
def theme_change(theme, user_id):
    if theme == "dark":
        valor = 1
    else:
        valor = 0
    bd_theme(valor, user_id)