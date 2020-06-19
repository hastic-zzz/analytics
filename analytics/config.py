import os
import json


PARENT_FOLDER = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
CONFIG_FILE = os.path.join(PARENT_FOLDER, 'config.json')


config_exists = os.path.isfile(CONFIG_FILE)
if config_exists:
    with open(CONFIG_FILE) as f:
        config = json.load(f)
else:
    print('Config file %s doesn`t exist, using environment variables / defaults' % CONFIG_FILE)


def get_config_field(field: str, default_val = None, allowed_values = []):
    value = None
    if field in os.environ:
        value = os.environ[field]
    elif config_exists and field in config and config[field] != '':
        value = config[field]
    elif default_val is not None:
        value = default_val

    if len(allowed_values) > 0 and value not in allowed_values:
        raise Exception('{} value must be one of: {}, got: {}'.format(field, allowed_values, value))

    if value == None:
        raise Exception('Please configure {}'.format(field))

    return value

HASTIC_SERVER_URL = get_config_field('HASTIC_SERVER_URL', 'ws://localhost:8002')
LOGGING_LEVEL = get_config_field(
    'HS_AL_LOGGING_LEVEL', 
    'INFO', 
    # TODO: make values case insensitive
    ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
)
LEARNING_TIMEOUT = get_config_field('LEARNING_TIMEOUT', 120)
