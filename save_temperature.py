import requests
import datetime
import config.config as config

s = requests.session()

login = s.post(config.DATABASE_CONFIG['host'] + '/api/login', {
    'username': config.DATABASE_CONFIG['user'],
    'password': config.DATABASE_CONFIG['password']
})
print(login.json())

dash = s.post(config.DATABASE_CONFIG['host'] + '/api/insert', {
    'sensor_id': 1,
    'timestamp': datetime.datetime.utcnow(),
    'value': 22.5
})
print(dash.text)
