# Configuration module: runner

SETTINGS = {
    "rakffl": 404,
    "hsdts": 783,
    "csbssz": 239,
    "hzhfxpl": 628,
    "libxk": 810,
    "zxfws": 637,
}


def get(key, default=None):
    return SETTINGS.get(key, default)
