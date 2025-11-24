from View.home import home_view
from View.login import login_view
from View.register import register_view
from View.venues import venues_view
from View.user import user_view
from View.appbar import create_appbar

rutas_con_appbar = ["/", "/venues", "/user"]

def route_change(page):
    page.views.clear()
    
    # Añadir la vista
    if page.route == "/":
        page.views.append(home_view(page))
    elif page.route == "/login":
        page.views.append(login_view(page))
    elif page.route == "/register":
        page.views.append(register_view(page))
    elif page.route == "/venues":
        from View.venues import venues_view
        page.views.append(venues_view(page))
    elif page.route == "/user":
        from View.user import user_view
        page.views.append(user_view(page))

    page.update()

def view_pop(page):
    if len(page.views) > 1:
        page.views.pop()
        page.go(page.views[-1].route)