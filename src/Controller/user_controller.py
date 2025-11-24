import flet as ft

import View.history_user as history_user
import Model.user_model as user_model
import View.user_password as user_pass


def historial_reservas(e, user_id):
    page = e.page
    reservations = user_model.get_reservations_by_user(user_id)
    dialog = history_user.create_modal_dialog(reservations)
    page.open(dialog)
    page.update()

def actualizar_observacion(id, observacion, user_id):
    user_model.set_observation(id, observacion, user_id)

def cambiar_contrseña(e, user_id):
    page = e.page
    dialog = user_pass.create_dialog(user_id)
    page.open(dialog)
    page.update()
