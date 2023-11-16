from nicegui import ui
from ..handlers.mp3_choose_upload import on_upload


class MP3Choose:
    uploader: ui.upload

    def place(self):
        self.uploader = ui.upload(
            label='Upload audio',
            max_files=1,
            on_upload=on_upload,
            max_total_size=100 * 1_048_576,
            auto_upload=True,
        ).classes('w-full')


mp3choose = MP3Choose()
