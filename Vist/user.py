import flet as ft


def user_view(page: ft.Page):
    page.title = "User Page"
    page.scroll = "auto"

    user_text = ft.Text("Welcome to the User Page", size=30)
    page.add(user_text)