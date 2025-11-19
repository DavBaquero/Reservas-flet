import flet as ft

def create_modal_dialog(reservations):
    rows = [
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(f"{r.get('fecha','')}/{r.get('hora','')}")),
                ft.DataCell(ft.Text("Realizado" if r.get("estado") == 1 else "Cancelada", color=ft.Colors.GREEN if r.get("estado") == 1 else ft.Colors.RED)),
                ft.DataCell(ft.Text(r.get("tipo", ""))),
                ft.DataCell(ft.Text(r.get("observaciones", ""))),
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
            content=ft.Column(
                expand=True,
                scroll=ft.ScrollMode.AUTO,  # vertical
                controls=[
                    ft.Row(
                        controls=[data_table],
                        scroll=ft.ScrollMode.AUTO,  # horizontal
                    )
                ],
            ),
        ),
        actions=[
            ft.ElevatedButton("Cerrar", on_click=lambda e: cerrar_dialog(e, dialog)),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    return dialog

def cerrar_dialog(e,dialog):
    e.page.close(dialog)
    e.page.update()