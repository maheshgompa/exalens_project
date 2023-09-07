import json
import random
import os
import time
# Create a directory to store the JSON data files if it doesn't exist
data_dir = "C:\\Users\\Mahesh\\mqtt_network\\sensor_data1"
os.makedirs(data_dir, exist_ok=True)

# Generate 100 records for temperature sensor
temperature_data = []
for i in range(1,101):
    record = {
        "sensor_id": i,
        "timestamp": time.strftime('%Y-%m-%dT%H:%M:%S'),  # You can use actual timestamps here
        "value": round(random.uniform(20.0, 30.0), 2)  # Random temperature value between 20.0 and 30.0
    }
    temperature_data.append(record)

# Generate 100 records for humidity sensor
humidity_data = []
for i in range(1,101):
    record = {
        "sensor_id": i,
        "timestamp": time.strftime('%Y-%m-%dT%H:%M:%S'),  # You can use actual timestamps here
        "value": round(random.uniform(40.0, 60.0), 2)  # Random humidity value between 40.0 and 60.0
    }
    humidity_data.append(record)

# Save the data to JSON files
with open(os.path.join(data_dir, "temperature_data.json"), "w") as temperature_file:
    json.dump(temperature_data, temperature_file, indent=4)

with open(os.path.join(data_dir, "humidity_data.json"), "w") as humidity_file:
    json.dump(humidity_data, humidity_file, indent=4)

print("JSON data files generated successfully.")
