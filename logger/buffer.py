import json
import os

BUFFER_FILENAME = 'buffer.json'


def read_buffer():
    """
    Read the buffer from disk.

    :return: [
      {
        'sensor_id': (integer),
        'timestamp': (string - format '%Y-%m-%d %H:%M:%S'),
        'value': (float)
      },
      ...
    ]
    """
    if os.path.isfile(BUFFER_FILENAME):
        f = open(BUFFER_FILENAME, 'r', encoding='utf-8')
        json_text = f.read()
        if json_text:
            return json.loads(json_text)
    else:
        return []


def write_buffer(data):
    """
    Save values to disk.

    :param data: [
      {
        'sensor_id': (integer),
        'timestamp': (string - format '%Y-%m-%d %H:%M:%S'),
        'value': (float)
      },
      ...
    ]
    :return:
    """
    f = open(BUFFER_FILENAME, 'w', encoding='utf-8')
    f.write(json.dumps(data, indent=4, sort_keys=True))


def clear():
    """
    Clear buffer.

    :return:
    """
    if os.path.isfile(BUFFER_FILENAME):
        os.remove(BUFFER_FILENAME)
