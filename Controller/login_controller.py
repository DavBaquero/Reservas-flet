import flet as ft

import View.user as user_view

def login_button_clicked(e):
    page = e.page
    page.controls.clear()
    sesion = True  
    if sesion:
        user_view.user_view(page)
    page.update()