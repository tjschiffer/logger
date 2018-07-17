import requests
import datetime
import config.config as config


def isWithinCompression(current_value, new_value, compression_value):
    return True


s = requests.session()

login = s.post(config.DATABASE_CONFIG['host'] + '/api/login', {
    'username': config.DATABASE_CONFIG['user'],
    'password': config.DATABASE_CONFIG['password']
})
print(login.json())

rows = [
    {
        'sensor_id': 1,
        'timestamp': datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
        'value': 22.5
    }
]

dash = s.post(config.DATABASE_CONFIG['host'] + '/api/insert', json=rows)
print(dash.text)
