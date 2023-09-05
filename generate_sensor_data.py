import random
import json
from datetime import datetime, timedelta
import time

def generate_sensor_data(sensor_id):
    return {
        "sensor_id": sensor_id,
        "value": round(random.uniform(0, 100), 2),
        "timestamp": time.strftime('%Y-%m-%dT%H:%M:%S')
    }

num_samples = 100
sensor_data = [generate_sensor_data(str(sensor_id)) for sensor_id in range(1, num_samples + 1)]

with open("sensor_data.json", "w") as f:
    json.dump(sensor_data, f, indent=2)

print(sensor_data)