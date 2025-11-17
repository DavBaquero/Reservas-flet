import flet as ft

from Vist.appbar import create_appbar

def main(page: ft.Page):
    page.title = "Flet Counter App"
    page.scroll = "auto"
    page.appbar = create_appbar()
    
    texto = ft.Text("Para ver", size=30)

    page.add(texto)
    

ft.app(target=main)