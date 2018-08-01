from datetime import datetime as datetime
import compression
import buffer
import save_to_server

import random

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

values = [

    {
        'sensor_id': 1,
        'timestamp': datetime.utcnow().strftime(DATE_FORMAT),
        'value': round(random.uniform(17, 30), 1)
    },
    {
        'sensor_id': 2,
        'timestamp': datetime.utcnow().strftime(DATE_FORMAT),
        'value': random.randint(30, 70)
    }
]

# Compress the values to ensure they have changed since last reading
compressed_values = compression.compress_values(values)
# Get the values from the buffer
buffered_values = buffer.read_buffer()

compressed_and_buffered_values = sorted(compressed_values + buffered_values,
                                        key=lambda k: datetime.strptime(k['timestamp'], DATE_FORMAT))
if not compressed_and_buffered_values:
    exit()

inserted_rows = save_to_server.save_to_server(compressed_and_buffered_values)
if not inserted_rows:
    print('Failure!')
    # If saving to the server completely fails (ex. no internet) save all the values to the buffer
    buffer.write_buffer(compressed_and_buffered_values)
else:
    print('Success!')
    # Clear the buffer since the values are now on the server
    buffer.clear()
