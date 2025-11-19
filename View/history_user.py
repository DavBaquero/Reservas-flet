import flet as ft

import Controller.user_controller as user_controller

def create_modal_dialog(reservations):
    rows = [
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(f"{r.get('fecha','')}/{r.get('hora','')}")),
                ft.DataCell(ft.Text("Realizado" if r.get("estado") == 1 else "Cancelada", color=ft.Colors.GREEN if r.get("estado") == 1 else ft.Colors.RED)), # Cambiarlo por un ENUM
                ft.DataCell(ft.Text(r.get("tipo", ""))),
                ft.DataCell(ft.TextField(r.get("obser", ""), multiline=True, expand=True)),
            ]
        )
        for r in reservations
    ]
    
    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Fecha y Hora")),
            ft.DataColumn(ft.Text("Estado")),
            ft.DataColumn(ft.Text("Tipo")),
            ft.DataColumn(ft.Text("Observaciones")),
        ],
        rows=rows,
    )
    dialog = ft.AlertDialog(
        title=ft.Text("Historial de Reservas"),
        content=ft.Container(
            width=600,
            height=400,
            content=ft.Row(
                expand=True,
                scroll=ft.ScrollMode.AUTO,  # horizontal
                controls=[
                    ft.Column(
                        height=400,
                        scroll=ft.ScrollMode.ALWAYS,  # vertical
                        controls=[data_table],
                    )
                ],
            ),
        ),
        actions=[
            ft.ElevatedButton("Guardar", on_click=lambda e: guardar_obser(e, dialog)),
            ft.ElevatedButton("Cerrar", on_click=lambda e: cerrar_dialog(e, dialog)),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    return dialog

def cerrar_dialog(e,dialog):
    e.page.close(dialog)
    e.page.update()

def guardar_obser(e, dialog):
        try:
            dt = dialog.content.content.controls[0].controls[0]
            posicion = 0
            for row in dt.rows:
                if len(row.cells) >= 4:
                    c = row.cells[3].content
                    posicion += 1
                    user_controller.actualizar_observacion(posicion, str(c.value or ""))
            e.page.close(dialog)
            e.page.update()
        except Exception as ex:
            print("No se pudo acceder a la tabla de datos.", ex)
