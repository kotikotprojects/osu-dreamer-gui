from nicegui import ui
from nicegui import app
import os


class ParamsBoxes:
    title: ui.input
    artist: ui.input
    bpm: ui.number
    num_samples = ui.number
    sample_steps = ui.number
    model_name = ui.input

    def place(self):
        storage = app.storage.user

        self.title = ui.input(
            label='Title',
            placeholder='Song title',
        ).bind_value(storage, 'detected_title').classes('w-full')

        self.artist = ui.input(
            label='Artist',
            placeholder='Song artist',
        ).bind_value(storage, 'detected_artist').classes('w-full')

        self.bpm = ui.number(
            label='BPM',
            placeholder='Song BPM',
            value=180,
        ).bind_value(storage, 'bpm').classes('w-full')

        self.num_samples = ui.number(
            label='Number of samples',
            placeholder='Number of samples',
            value=2,
        ).classes('w-full').bind_value(storage, 'num_samples')

        self.sample_steps = ui.number(
            label='Sample steps',
            placeholder='Sample steps',
            value=32,
        ).classes('w-full').bind_value(storage, 'sample_steps')

        self.model_name = ui.input(
            label='Model name',
            placeholder='Model name',
            value=[item for item in filter(
                lambda x: x.endswith('.ckpt'), os.listdir('models')
            )][0],
        ).classes('w-full').bind_value(storage, 'model_name')


paramsboxes = ParamsBoxes()
