from nicegui import ui, app, run
from io import BytesIO
from ...modules.encoder.encoder import load


def creator(storage):
    import torch
    from osu_dreamer.model import Model
    from ...modules.generate import generate_mapset
    from rich.traceback import install

    install(show_locals=True)

    model = Model.load_from_checkpoint(
        f'models/{storage["model_name"]}',
        sample_steps=storage['sample_steps'],
    ).eval()

    if torch.cuda.is_available():
        model = model.cuda()

    audio = BytesIO(load(storage['audio_content']))
    audio.name = storage['filename']
    audio.seek(0)
    return generate_mapset(
        model,
        audio,
        storage['bpm'],
        storage['num_samples'],
        storage['detected_title'], storage['detected_artist'],
    ).name


async def on_create():
    storage = app.storage.user

    storage['is_loading'] = True
    storage['can_be_created'] = False

    try:
        mapset_path = await run.cpu_bound(creator, dict(
            model_name=storage['model_name'],
            audio_content=storage['audio_content'],
            bpm=int(storage['bpm']),
            num_samples=int(storage['num_samples']),
            sample_steps=int(storage['sample_steps']),
            detected_title=storage['detected_title'],
            detected_artist=storage['detected_artist'],
            filename=storage['filename'],
        ))
        storage['mapset_path'] = mapset_path
        storage['can_be_saved'] = True
    except Exception as e:
        ui.notify(f'Error {e}')

    storage['is_loading'] = False
    storage['can_be_created'] = True
