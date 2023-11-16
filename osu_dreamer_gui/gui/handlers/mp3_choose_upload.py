from nicegui import ui, events, app
import mutagen

from ...modules.encoder.encoder import dump


async def on_upload(e: events.UploadEventArguments):
    storage = app.storage.user

    storage['bpm'] = None
    storage['detected_title'] = None
    storage['detected_artist'] = None

    tags = mutagen.File(e.content, easy=True)

    if 'bpm' in tags:
        storage['bpm'] = int(float(tags['bpm'][0]))

    if 'title' in tags:
        storage['detected_title'] = tags['title'][0]

    if 'artist' in tags:
        storage['detected_artist'] = tags['artist'][0]

    storage['filename'] = e.name
    storage['audio_content'] = dump(e.content.read())

    storage['can_be_created'] = True
    storage['can_be_saved'] = False
