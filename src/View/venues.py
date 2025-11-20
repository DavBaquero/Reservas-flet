import flet as ft
import Model.conexion as conexion
import mysql.connector
from View.reservation_view import ReservationView
from Model.reservation_model import Dish
from Controller.reservation_controller import ReservationController


def get_venues_data():
    locales_data = []
    # Intenta establecer conexión y ejecutar la consulta a la BD
    try:
        conn = conexion.connection()
        cursor = conn.cursor(dictionary=True)

        # Consulta SQL para obtener los locales activos
        query = "SELECT id_local, nombre, descripcion, tipo_local, horario, url_imagen FROM locales WHERE activo = TRUE"
        cursor.execute(query)

        locales_data = (
            cursor.fetchall()
        )  # Obtiene todos los resultados como una lista de diccionarios

    except mysql.connector.Error as err:
        print(f"Error al conectar o consultar la base de datos: {err}")
        # Retorna datos de prueba en caso de error de conexión
        return [
            {
                "id_local": 99,
                "nombre": "Restaurante Ficticio",
                "descripcion": "Error de conexión. Datos de prueba.",
                "tipo_local": "Restaurante",
                "horario": "N/A",
                "url_imagen": "",
            }
        ]

    finally:
        # Asegura el cierre de la conexión y el cursor
        if "conn" in locals() and conn.is_connected():
            cursor.close()
            conn.close()

    return locales_data


def venues_view(page: ft.Page):
    page.title = "Página de Locales"
    page.scroll = "auto"
    page.horizontal_alignment = "center"

    # Obtiene todos los locales de la base de datos
    all_locales = get_venues_data()

    # Esta variable se usa para mantener el estado del filtro si no hay un evento
    filter_text_value = ""

    # Función auxiliar para crear una tarjeta individual de local
    def create_local_card(local):
        imagen_src = local["url_imagen"]

        # 1. Verificar si el valor es una cadena.
        if isinstance(imagen_src, str):
            # 2. Si es una cadena, eliminamos espacios en blanco al inicio y al final (strip)
            imagen_src = imagen_src.strip()

        # 3. La condición 'if not' manejará:
        #    - El valor original si era None.
        #    - Una cadena vacía ("") después de hacer strip.
        if not imagen_src:
            imagen_src = "default.png"

        # Función que se ejecuta al hacer clic en "Ir a Reservar"
        def handle_reserve_click(
            e, local_id=local["id_local"], local_name=local["nombre"]
        ):
            page = e.page
            page.controls.clear()
            if local_id == 1:
                dishes = [
                    Dish(id=1, name="Menú del día", price=12.50),
                    Dish(id=2, name="Hamburguesa", price=9.90),
                    Dish(id=3, name="Pizza Margarita", price=10.50),
                    Dish(id=4, name="Ensalada César", price=8.00),
                ]
            else:
                dishes = [
                    Dish(id=1, name="Testeo 1", price=12.50),
                    Dish(id=2, name="Testeo 2", price=9.90),
                    Dish(id=3, name="Testeo 3", price=10.50),
                    Dish(id=4, name="Testeo 4", price=8.00),
                ]

            controller = ReservationController(dishes=dishes)

            ReservationView(page=page, controller=controller)

            page.update()

        return ft.Card(
            elevation=4,
            content=ft.Container(
                expand=True,
                content=ft.Column(
                    controls=[
                        # Contenedor de la Imagen:
                        ft.Image(
                            # Ahora mismo carga una imagen estática
                            # En el caso real se cargaría una url del campo en la base de datos
                            src=imagen_src,
                            height=200,
                            fit=ft.ImageFit.CONTAIN,
                            error_content=ft.Container(
                                content=ft.Text(
                                    "Imagen no disponible", color=ft.Colors.RED
                                ),
                                alignment=ft.alignment.center,
                                height=200,
                            ),
                        ),
                        # Título y descripción
                        ft.ListTile(
                            title=ft.Text(
                                f"{local['nombre']}", weight=ft.FontWeight.BOLD
                            ),
                            subtitle=ft.Text(
                                local['descripcion'],
                                max_lines=1,
                                overflow=ft.TextOverflow.ELLIPSIS,
                            ),
                        ),
                        # Horario
                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.Text(f"Horario: {local['horario']}", size=12),
                                ],
                            ),
                            padding=ft.padding.symmetric(horizontal=15, vertical=5),
                        ),
                        # Botón reserva que no lleva a nada ahora mismo
                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.ElevatedButton(
                                        text="Ir a Reservar",
                                        on_click=handle_reserve_click,
                                        style=ft.ButtonStyle(
                                            padding=ft.padding.symmetric(horizontal=20),
                                            bgcolor=ft.Colors.BLUE_GREY_700,
                                            color=ft.Colors.WHITE,
                                        ),
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.END,
                            ),
                            padding=ft.padding.all(10),
                        ),
                    ],
                    spacing=0,
                ),
                padding=ft.padding.all(0),
                width=400,
            ),
        )

    # Contenedor que mostrará las tarjetas
    venues_display = ft.ResponsiveRow(
        controls=[],
        run_spacing=20,
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # Función que aplica el filtro y actualiza la UI
    def update_venues_display(e: ft.ControlEvent = None):
        # Obtiene el valor del filtro, ya sea del evento o el valor inicial
        current_filter = filter_textbox.value if e else filter_text_value

        filter_text = current_filter.lower()

        # Filtra la lista de locales
        filtered_locales = [
            local for local in all_locales if filter_text in local["nombre"].lower()
        ]

        # Genera las nuevas tarjetas de locales filtrados
        new_cards = [
            ft.Container(
                content=create_local_card(local),
                col={"sm": 12, "md": 6, "lg": 4},
            )
            for local in filtered_locales
        ]

        # Actualiza lo que se muestra
        venues_display.controls = new_cards
        page.update()

    # Campo de texto para la funcionalidad de filtro
    filter_textbox = ft.TextField(
        label="Filtrar por nombre del local",
        hint_text="Escribe el nombre del local...",
        prefix_icon=ft.Icons.SEARCH,
        on_change=update_venues_display,
        width=500,
    )

    # Carga Inicial
    venues_display.controls = [
        ft.Container(
            content=create_local_card(local),
            col={"sm": 12, "md": 6, "lg": 4},
        )
        for local in all_locales
    ]

    # Construcción final de la página
    page.clean()
    page.add(
        ft.Text("Listado de locales disponibles", size=30, weight=ft.FontWeight.BOLD),
        ft.Divider(),
        # Contenedor del filtro centrado
        ft.Container(
            content=filter_textbox,
            alignment=ft.alignment.center,
            padding=ft.padding.only(bottom=20),
        ),
        # Muestra el listado de locales
        venues_display,
    )

    page.update()
