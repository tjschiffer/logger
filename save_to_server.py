import requests
import json


def save_to_server(data, server_config):
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
    :param server_config: {
        'host': (string),
        'user': (string),
        'password': (string),
    }
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
        s.post(server_config['host'] + '/api/login', {
            'username': server_config['user'],
            'password': server_config['password']
        }, timeout=1)
        # Send the values
        save_values = s.put(server_config['host'] + '/api/insert', json=data)
        if save_values.status_code != requests.codes.ok or not save_values.text:
            return False
        response_data = json.loads(save_values.text)
        if not response_data['success'] or not response_data['insertedRows']:
            return False
        return response_data['insertedRows']
    except Exception:
        # If any error occurs (ConnectionError etc), return false
        return False
