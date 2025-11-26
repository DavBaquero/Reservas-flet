import flet as ft
import Model.odoo_api as odoo_api

from View.reservation_view import ReservationView
from Controller.reservation_controller import ReservationController
from Model.reservation_model import Dish


def get_venues_data():
    locales_data = odoo_api.get_venues_from_odoo()

    if not locales_data:
        return [
            {
                "id_local": 0,
                "nombre": "No hay Locales Odoo (res.partner)",
                "descripcion": "Verifica credenciales, Etiqueta, y que las Compañías existan.",
                "horario": "N/A",
                "url_imagen": "",
                "pos_config_id": None, 
                "pos_config_name": "N/A",
            }
        ]

    return locales_data


def handle_reservation_click(e, local):
    page = e.page

    nombre_local = local["nombre"].lower()

    if "milongas" in nombre_local:
        category_name = "Milongas"
    elif "restaurante la cuchara" in nombre_local:
        category_name = "Cuchara"
        
    dishes = odoo_api.get_products_by_category_name(category_name)
    
    if not dishes:
        dishes = [
            Dish(id=1, name="Menú del día", price=12.50),
            Dish(id=2, name="Hamburguesa", price=9.90),
            Dish(id=3, name="Pizza Margarita", price=10.50),
            Dish(id=4, name="Ensalada César", price=8.00),
        ]

    controller = ReservationController(dishes=dishes)
    ReservationView(page=page, controller=controller)
    page.update()


def create_local_card(local):
    
    pos_id = local.get('pos_config_id')
    is_linked = pos_id is not None
    
    # verification_text = (
    #     f"Local: {local.get('nombre')}\n"
    #     f"TPV Encontrado: {local.get('pos_config_name', 'N/A')} (ID: {pos_id or 'N/A'})"
    # )

    return ft.Card(
        elevation=10,
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(local["nombre"], size=20, weight=ft.FontWeight.BOLD),
                    ft.Image(
                        src=local["url_imagen"],
                        width=float("inf"),
                        height=200,
                        fit=ft.ImageFit.COVER,
                        error_content=ft.Container(
                            content=ft.Text(
                                "Imagen no disponible", color=ft.Colors.ERROR
                            ),
                            alignment=ft.alignment.center,
                            height=200,
                        ),
                    ),
                    ft.Text(
                        local["descripcion"],
                        size=12,
                        max_lines=3,
                        overflow=ft.TextOverflow.ELLIPSIS,
                    ),
                    ft.Text(f"Teléfono: {local['horario']}", size=12),
                    
                    # ft.Text(
                    #     verification_text,
                    #     size=10,
                    #     color=ft.Colors.RED_600 if not is_linked else ft.Colors.GREEN_600,
                    #     weight=ft.FontWeight.BOLD,
                    # ),
                    
                    ft.Row(
                        [
                            ft.FilledButton(
                                text="Reservar",
                                icon=ft.Icons.BOOKMARK_ADD_OUTLINED,
                                on_click=lambda e: handle_reservation_click(e, local),
                                disabled=not is_linked,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ],
            ),
            padding=15,
            border_radius=12,
        ),
    )


def venues_view(page: ft.Page):
    all_locales = get_venues_data()

    def update_venues_display(e):
        filter_text = e.control.value.lower()

        filtered_locales = [
            local for local in all_locales if filter_text in local["nombre"].lower()
        ]

        new_cards = [
            ft.Container(
                content=create_local_card(local),
                col={"sm": 12, "md": 6, "lg": 4},
            )
            for local in filtered_locales
        ]

        venues_display.controls = new_cards
        page.update()

    filter_textbox = ft.TextField(
        label="Filtrar por nombre del local",
        hint_text="Escribe el nombre del local...",
        prefix_icon=ft.Icons.SEARCH,
        on_change=update_venues_display,
        expand=True,
    )

    venues_display = ft.ResponsiveRow(
        [
            ft.Container(
                content=create_local_card(local),
                col={"sm": 12, "md": 6, "lg": 4},
            )
            for local in all_locales
        ],
        run_spacing=20,
    )

    filter_layout = ft.ResponsiveRow(
        [
            ft.Container(col={"lg": 4, "md": 3}), 

            ft.Container( 
                content=filter_textbox,
                col={"sm": 12, "md": 6, "lg": 4},
            ),

            ft.Container(col={"lg": 4, "md": 3}),
        ],
        run_spacing={"sm": 0},
        alignment=ft.MainAxisAlignment.CENTER,
    )

    page.clean()

    page.add(
        ft.Text("Listado de locales disponibles", size=30, weight=ft.FontWeight.BOLD),
        ft.Divider(),
        
        ft.Container(
            content=filter_layout,
            padding=ft.padding.only(left=10, right=10, top=10, bottom=10) 
        ),
        
        ft.Container(
            content=venues_display,
            padding=ft.padding.only(top=20)
        )
    )

    page.update()