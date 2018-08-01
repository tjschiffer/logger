import json
import os

BUFFER_FILENAME = 'buffer.json'


def read_buffer():
    if os.path.isfile(BUFFER_FILENAME):
        f = open(BUFFER_FILENAME, 'r', encoding='utf-8')
        json_text = f.read()
        if json_text:
            return json.loads(json_text)
    else:
        return []


def write_buffer(data):
    f = open(BUFFER_FILENAME, 'w', encoding='utf-8')
    f.write(json.dumps(data, indent=4, sort_keys=True))


def clear():
    if os.path.isfile(BUFFER_FILENAME):
        os.remove(BUFFER_FILENAME)
