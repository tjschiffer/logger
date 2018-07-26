import config.config as config
import json

RECENT_VALUES_FILENAME = 'recent_values.json'


def save_recent_values(data):
    f = open(RECENT_VALUES_FILENAME, 'w', encoding='utf-8')
    f.write(json.dumps(data, separators=(',', ':')))


def compress_values(values):
    recent_values = {}
    compressed_values = []
    try:
        f = open(RECENT_VALUES_FILENAME, 'r', encoding='utf-8')
        json_text = f.read()
        if json_text:
            recent_values = json.loads(json_text)
            for value in values:
                sensor_id = value['sensor_id']
                data_value = value['value']
                # Use the sensor id as a string since JSON uses strings as keys
                sensor_id_str = str(sensor_id)
                if sensor_id_str not in recent_values or \
                        abs(recent_values[sensor_id_str] - data_value) > config.DATA_COMPRESSION[sensor_id]:
                    # The value is not within compression or not available
                    compressed_values.append(value)
                    recent_values[sensor_id] = data_value
        save_recent_values(recent_values)
        return compressed_values
    except FileNotFoundError:
        for value in values:
            recent_values[value['sensor_id']] = value['value']
        save_recent_values(recent_values)
        return values
    # except:
    #     raise ValueError('Sensor id must be an int and value must be a number.')
