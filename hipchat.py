import json
import requests

ROOM_ID = 1

HIPCHAT_API_URL = ''
HIPCHAT_DEFAULTS = {
        'notify': True,
        'color': 'green',
        'name': 'Magic8Ball',
        'room_id': ROOM_ID,
        }

def hipchat_message(message, **data):
    data = dict(HIPCHAT_DEFAULTS, message=message, **data)
    return json_post(HIPCHAT_API_URL, data)

def json_post(url, data_dict, **kwargs):
    requests.post(url, json.dumps(data_dict), **kwargs)
