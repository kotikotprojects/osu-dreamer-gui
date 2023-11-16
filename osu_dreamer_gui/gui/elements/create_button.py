from nicegui import ui, app
from ..handlers.on_create import on_create


class CreateButton:
    create_button: ui.button
    download_button: ui.button
    loading: ui.spinner

    def place(self):
        with ui.row():
            self.create_button = ui.button(
                'Create map', on_click=on_create
            ).bind_enabled_from(app.storage.user, 'can_be_created')

            self.download_button = ui.button(
                'Save map',
                on_click=lambda: ui.download(
                    src=app.storage.user.get('mapset_path')
                )
            ).bind_enabled_from(app.storage.user, 'can_be_saved')

            self.loading = ui.spinner(
                type='audio',
                size='2rem'
            ).bind_visibility_from(app.storage.user, 'is_loading')


createbutton = CreateButton()
