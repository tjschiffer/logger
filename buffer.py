import json

BUFFER_FILENAME = 'buffer.json'


def read_buffer():
    try:
        f = open(BUFFER_FILENAME, 'r', encoding='utf-8')
        json_text = f.read()
        if json_text:
            return json.loads(json_text)
    except FileNotFoundError:
        return []
    return []


def write_buffer(data):
    f = open(BUFFER_FILENAME, 'w', encoding='utf-8')
    f.write(json.dumps(data, separators=(',', ':')))
