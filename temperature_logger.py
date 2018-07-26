import datetime
import compression
import buffer

# save_to_server({
#     'sensor_id': 1,
#     'timestamp': datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
#     'value': 22.5
# })

values = [

    {
        'sensor_id': 1,
        'timestamp': datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
        'value': 22.5
    },
    {
        'sensor_id': 2,
        'timestamp': datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
        'value': 60
    }
]

print(compression.compress_values(values))
# compression.compress_values(values)
# print(buffer.read_buffer())
# buffer.write_buffer(values)