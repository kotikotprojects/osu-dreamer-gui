import base64


def dump(obj):
    return base64.b64encode(obj).decode()


def load(obj):
    return base64.b64decode(obj.encode())
