import flet as ft

from Model.user_model import change_theme as bd_theme

user_id = 1 #Falseamos el id

def create_appbar(page: ft.Page, show_back_button: bool = False):

    # Hacemos que sino existe el botón de cambiar tema, lo cree.
    if not hasattr(page, '_theme_button'):
        initial_icon = ft.Icons.NIGHTLIGHT_ROUND if page.theme_mode == ft.ThemeMode.LIGHT else ft.Icons.WB_SUNNY_OUTLINED
        
        page._theme_button = ft.IconButton(
            initial_icon, 
            on_click=lambda e: change_theme(e, page._theme_button),
        )

    # Definimos la appbar con sus respectivos botones.
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
    
    # Con eso hacemos que, si la variable del botón está en True,
    # añadimos el botón para ir hacia atrás
    if show_back_button:
        appbar.leading = ft.IconButton(
            icon=ft.Icons.ARROW_BACK,
            on_click=lambda e: e.page.go("/")
        )
    
    return appbar

# Esta función es la que vamos a usar para cambiar el tema
def change_theme(e, theme_button):
    page = e.page
    
    # Si está en modo claro, entonces asignamos el oscuro
    if page.theme_mode == ft.ThemeMode.LIGHT:
        page.theme_mode = ft.ThemeMode.DARK
        theme_button.icon = ft.Icons.WB_SUNNY_OUTLINED 
        # Esta función es para la persistencia en caso de reinicio de la app
        theme_change(page.theme_mode.value, user_id)
    else:
    # Sino, entonces asignamos el modo claro
        page.theme_mode = ft.ThemeMode.LIGHT
        theme_button.icon = ft.Icons.NIGHTLIGHT_ROUND
        # Esta funcion es para la presistencia en caso de reinicio de la app
        theme_change(page.theme_mode.value, user_id)

    # Este apartado, es para ver si puede ir hacia atrás en el botón
    if page.views:
        current_view = page.views[-1]
        current_view.appbar = create_appbar(page, show_back_button=current_view.route != "/")

    page.update()

# Esta función está usada simplemente para gestionar 
# el tema actual antes cambio en la base de datos
def theme_change(theme, user_id):
    if theme == "dark":
        valor = 1
    else:
        valor = 0
    bd_theme(valor, user_id)