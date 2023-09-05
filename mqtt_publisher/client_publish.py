import paho.mqtt.client as mqtt
import json
from generate_sensor_data import sensor_data
# Define MQTT broker address and port
broker_address = "localhost"
broker_port = 1883

# Publish a message to a topic
topic = "test2/topic"
# message = "Hello, MQTT!"
message = [
  {
    "sensor_id": "1",
    "value": 25.06,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "2",
    "value": 95.64,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "3",
    "value": 60.65,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "4",
    "value": 43.22,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "5",
    "value": 99.5,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "6",
    "value": 99.08,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "7",
    "value": 79.48,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "8",
    "value": 63.29,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "9",
    "value": 99.81,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "10",
    "value": 95.22,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "11",
    "value": 56.5,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "12",
    "value": 94.12,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "13",
    "value": 66.13,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "14",
    "value": 59.88,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "15",
    "value": 82.74,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "16",
    "value": 68.7,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "17",
    "value": 28.93,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "18",
    "value": 16.23,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "19",
    "value": 98.64,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "20",
    "value": 28.17,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "21",
    "value": 5.9,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "22",
    "value": 97.4,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "23",
    "value": 85.2,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "24",
    "value": 70.49,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "25",
    "value": 17.63,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "26",
    "value": 57.03,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "27",
    "value": 82.91,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "28",
    "value": 87.28,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "29",
    "value": 91.6,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "30",
    "value": 44.59,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "31",
    "value": 64.13,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "32",
    "value": 34.13,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "33",
    "value": 83.66,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "34",
    "value": 19.16,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "35",
    "value": 78.02,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "36",
    "value": 63.98,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "37",
    "value": 15.62,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "38",
    "value": 79.36,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "39",
    "value": 70.13,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "40",
    "value": 61.38,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "41",
    "value": 41.33,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "42",
    "value": 83.19,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "43",
    "value": 82.86,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "44",
    "value": 71.88,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "45",
    "value": 32.05,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "46",
    "value": 89.22,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "47",
    "value": 47.36,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "48",
    "value": 11.61,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "49",
    "value": 18.68,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "50",
    "value": 45.97,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "51",
    "value": 31.75,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "52",
    "value": 23.34,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "53",
    "value": 71.72,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "54",
    "value": 21.4,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "55",
    "value": 21.86,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "56",
    "value": 32.23,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "57",
    "value": 89.8,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "58",
    "value": 89.75,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "59",
    "value": 49.18,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "60",
    "value": 78.82,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "61",
    "value": 95.81,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "62",
    "value": 14.01,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "63",
    "value": 28.92,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "64",
    "value": 73.82,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "65",
    "value": 20.7,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "66",
    "value": 8.02,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "67",
    "value": 77.57,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "68",
    "value": 6.21,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "69",
    "value": 24.04,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "70",
    "value": 74.57,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "71",
    "value": 71.45,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "72",
    "value": 16.4,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "73",
    "value": 93.49,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "74",
    "value": 63.91,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "75",
    "value": 37.66,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "76",
    "value": 32.73,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "77",
    "value": 39.34,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "78",
    "value": 19.78,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "79",
    "value": 86.46,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "80",
    "value": 7.77,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "81",
    "value": 29.38,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "82",
    "value": 68.48,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "83",
    "value": 37.9,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "84",
    "value": 34.38,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "85",
    "value": 71.47,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "86",
    "value": 52.5,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "87",
    "value": 67.27,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "88",
    "value": 48.17,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "89",
    "value": 37.79,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "90",
    "value": 16.05,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "91",
    "value": 41.92,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "92",
    "value": 99.62,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "93",
    "value": 66.27,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "94",
    "value": 35.33,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "95",
    "value": 81.69,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "96",
    "value": 48.06,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "97",
    "value": 84.55,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "98",
    "value": 86.79,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "99",
    "value": 1.97,
    "timestamp": "2023-08-29T11:00:43.446434"
  },
  {
    "sensor_id": "100",
    "value": 73.82,
    "timestamp": "2023-08-29T11:00:43.446434"
  }
]
payload = json.dumps(message)
# Create a MQTT client instance
client = mqtt.Client()

# Connect to the broker
client.connect(broker_address, broker_port)
# if client.connect(broker_address, broker_port):
#     print("connection establish")
# else:
#     print("not establish")

client.publish(topic, payload)

# Disconnect from the broker
client.disconnect()
