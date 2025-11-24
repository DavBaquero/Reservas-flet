import hashlib
import flet as ft
from Model.user_model import get_password_hashed as get_password
from Model.user_model import set_password as save_pass

def get_password_hashed(user_id):
    return get_password(user_id)

def hashed_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def validation_actu(user_id,password):
    pass_bd = get_password_hashed(user_id)
    password = hashed_password(password)
    if pass_bd[0] != password:
        return False
    else:
        return True
    
def save_change(user_id, new_pass):
    new_pass = hashed_password(new_pass.value)
    save_pass(user_id, new_pass)


def validation(e, user_id,pass_actu, pass_nueva, pass_repe):
    page = e.page

    pass_actu.error_text=None
    pass_nueva.error_text=None
    pass_repe.error_text=None

    if not pass_actu.value:
        pass_actu.error_text="Ingrese su contraseña actual"
        page.update()
        return
    elif not validation_actu(user_id, pass_actu.value):
        pass_actu.error_text="La contraseña proporcionada es incorrecta"
        page.update()
        return
    else:
        pass_actu.error_text=None
        page.update()

    if not pass_nueva.value:
        pass_nueva.error_text= "Ingresa la nueva contraseña"
        page.update()
        return
    elif not pass_repe.value:
        pass_nueva.error_text=None
        pass_repe.error_text= "Ingrese la nueva contraseña otra vez"
        page.update()
        return
    elif pass_nueva.value != pass_repe.value:
        pass_actu.error_text=None
        pass_repe.error_text=None

        pass_repe.error_text="Las contraseñas no coinciden"
        page.update()
        return
    
    return True

def confirmation(e, dialog, user_id):
    pass_actu = dialog.content.content.controls[0]
    pass_nueva = dialog.content.content.controls[1]
    pass_repe = dialog.content.content.controls[2]

    if validation(e,user_id, pass_actu, pass_nueva, pass_repe):
    
        page = e.page
        conf_dia = confirmation_dialog(page, user_id=user_id, pass_actu=pass_actu, pass_nueva=pass_nueva, original_dialog=dialog)
        page.open(conf_dia)
        page.update()

def close_dialog(e,dialog):
    e.page.close(dialog)
    e.page.update()

def confirmation_dialog(page, user_id, pass_actu, pass_nueva, original_dialog):
    conf_dia = ft.AlertDialog(
        title=ft.Text("¿Estás seguro de cambiar la contraseña?"),
        actions=[
            ft.ElevatedButton("Sí", on_click=lambda e: [save_change(user_id, pass_nueva), close_dialog(e, conf_dia), close_dialog(e, original_dialog)]),
            ft.ElevatedButton("No", on_click= lambda e: close_dialog(e, conf_dia))
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )
    return conf_dia