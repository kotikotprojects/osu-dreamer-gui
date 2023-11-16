from nicegui import ui

from . import gui

from rich.traceback import install


def main():
    install(show_locals=True)
    ui.run(
        title='osu!dreamer',
        native=True,
        dark=True,
        reload=False,
        storage_secret='...',
        window_size=(800, 670),
    )
