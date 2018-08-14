import json

RECENT_VALUES_FILENAME = 'recent_values.json'


def save_recent_values(data):
    """
    Save the recent values to disk.

    :param data: {
      sensor_id: (float),
      ...
    }
    :return:
    """
    f = open(RECENT_VALUES_FILENAME, 'w', encoding='utf-8')
    f.write(json.dumps(data))


def except_values(values, exception_config=None):
    """
    Remove values that are not different enough from
    the last measurement stored in recent_values for each sensor_id
    (based on the config.DATA_COMPRESSION for each sensor_id)
    from the given array of values.

    :param values: [
      {
        'sensor_id': (integer),
        'timestamp': (string - format '%Y-%m-%d %H:%M:%S'),
        'value': (float)
      },
      ...
    ]
    :param exception_config: {
        sensor_id (int): compression_value (float)
        ...
      }
    :return: [
      {
        'sensor_id': (integer),
        'timestamp': (string - format '%Y-%m-%d %H:%M:%S'),
        'value': (float)
      },
      ...
    ]
    """
    recent_values = {}
    accepted_values = []
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
                        sensor_id not in exception_config or \
                        abs(recent_values[sensor_id_str] - data_value) > exception_config[sensor_id]:
                    # The value is not available or not in the config or not within compression
                    accepted_values.append(value)
                    recent_values[sensor_id_str] = data_value
        save_recent_values(recent_values)
        return accepted_values
    except FileNotFoundError:
        # If there is not compression file, save the current values and return them
        for value in values:
            recent_values[value['sensor_id']] = value['value']
        save_recent_values(recent_values)
        return values
