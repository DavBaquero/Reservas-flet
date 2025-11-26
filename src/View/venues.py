import flet as ft
import Model.conexion as conexion
import mysql.connector
from Model.reservation_model import Dish
from View.appbar import create_appbar


def get_venues_data():
    locales_data = []
    try:
        conn = conexion.connection()
        cursor = conn.cursor(dictionary=True)
        query = (
            "SELECT id_local, nombre, descripcion, tipo_local, horario, url_imagen "
            "FROM locales WHERE activo = TRUE"
        )
        cursor.execute(query)
        locales_data = cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error BD: {err}")
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
    finally:
        if "conn" in locals() and conn.is_connected():
            cursor.close()
            conn.close()
    return locales_data


def venues_view(page: ft.Page):
    all_locales = get_venues_data()
    venues_display = ft.ResponsiveRow(
        controls=[],
        run_spacing=20,
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    def create_local_card(local):
        def handle_click(e):
            page.go(f"/reservar/{local['id_local']}")

        return ft.Card(
            elevation=4,
            content=ft.Container(
                expand=True,
                content=ft.Column(
                    controls=[
                        ft.Image(
                            src="img/default.png",
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
                        ft.ListTile(
                            title=ft.Text(local["nombre"], weight=ft.FontWeight.BOLD),
                            subtitle=ft.Text(
                                local["descripcion"],
                                max_lines=1,
                                overflow=ft.TextOverflow.ELLIPSIS,
                            ),
                        ),
                        ft.Container(
                            content=ft.Row(
                                [ft.Text(f"Horario: {local['horario']}", size=12)]
                            ),
                            alignment=ft.alignment.center,
                            height=200, 
                        ),
                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.ElevatedButton(
                                        text="Ir a Reservar",
                                        on_click=handle_click,
                                        style=ft.ButtonStyle(
                                            padding=ft.padding.symmetric(
                                                horizontal=20
                                            ),
                                        ),
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.END,
                            ),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
            ),
        )

    def update_venues_display(e):
        filter_text = filter_textbox.value.lower()

        filtered_locales = [
            local
            for local in all_locales
            if filter_text in local["nombre"].lower()
        ]

        venues_display.controls = [
            ft.Container(
                content=create_local_card(local),
                col={"sm": 12, "md": 6, "lg": 4},
            )
            for local in filtered_locales
        ]
        venues_display.update()

    filter_textbox = ft.TextField(
        label="Filtrar por nombre",
        prefix_icon=ft.Icons.SEARCH,
        on_change=update_venues_display,
        expand=True,
    )

    venues_display.controls = [
        ft.Container(
            content=create_local_card(local),
            col={"sm": 12, "md": 6, "lg": 4},
        )
        for local in all_locales
    ]

    return ft.View(
        route="/venues",
        scroll="auto",
        appbar=create_appbar(page, show_back_button=True),
        controls=[
            ft.Text("Listado de locales disponibles", size=30, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.Container(
                content=filter_textbox,
                alignment=ft.alignment.center,
                padding=ft.padding.only(bottom=20),
            ),
            venues_display,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )