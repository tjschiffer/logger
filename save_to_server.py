import requests
import config.config as config
import json


def save_to_server(data):
    """
    Save supplied values to server.
    Return false if the save fails, or the saved values with the db id if successful.

    :param data: [
      {
        'sensor_id': (integer),
        'timestamp': (string - format '%Y-%m-%d %H:%M:%S'),
        'value': (float)
      },
      ...
    ]
    :return: bool | [
      {
        'id': (integer)
        'sensor_id': (integer),
        'timestamp': (string - format '%Y-%m-%d %H:%M:%S'),
        'value': (float)
      },
      ...
    ]
    """
    try:
        s = requests.session()
        # Login and save to session
        s.post(config.DATABASE_CONFIG['host'] + '/api/login', {
            'username': config.DATABASE_CONFIG['user'],
            'password': config.DATABASE_CONFIG['password']
        }, timeout=1)
        # Send the values
        save_values = s.put(config.DATABASE_CONFIG['host'] + '/api/insert', json=data)
        if save_values.status_code != requests.codes.ok or not save_values.text:
            return False
        response_data = json.loads(save_values.text)
        if not response_data['success'] or not response_data['insertedRows']:
            return False
        return response_data['insertedRows']
    except Exception:
        # If any error occurs (ConnectionError etc), return false
        return False
