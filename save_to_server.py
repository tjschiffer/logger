import requests
import config.config as config
from urllib3.connection import NewConnectionError, ConnectTimeoutError
from urllib3.exceptions import MaxRetryError, ReadTimeoutError
from requests.exceptions import ReadTimeout
import json


def save_to_server(data):
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
    except (NewConnectionError, MaxRetryError, ConnectTimeoutError, ReadTimeoutError, ReadTimeout) as e:
        return False
