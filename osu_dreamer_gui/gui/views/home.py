from nicegui import ui, app
from ..elements.mp3_choose import mp3choose
from ..elements.params_boxes import paramsboxes
from ..elements.create_button import createbutton


@ui.page('/')
async def homepage():
    app.storage.user['can_be_created'] = False
    app.storage.user['is_loading'] = False
    app.storage.user['can_be_saved'] = False

    mp3choose.place()
    paramsboxes.place()
    createbutton.place()
