import requests
import config.config as config
from urllib3.connection import NewConnectionError, ConnectTimeoutError
from urllib3.exceptions import MaxRetryError


def save_to_server(data):
    try:
        s = requests.session()
        login = s.post(config.DATABASE_CONFIG['host'] + '/api/login', {
            'username': config.DATABASE_CONFIG['user'],
            'password': config.DATABASE_CONFIG['password']
        })
        print(login.text)

        save_values = s.post(config.DATABASE_CONFIG['host'] + '/api/insert', data)
        print(save_values.text)
    except (NewConnectionError, MaxRetryError, ConnectTimeoutError) as e:
        return False
    except:
        return False
