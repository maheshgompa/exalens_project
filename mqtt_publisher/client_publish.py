import paho.mqtt.client as mqtt
import json, time

# Define MQTT broker address and port
broker_address = "localhost"
broker_port = 1883
keepalive_interval = 60

# Publish a message to a topic
temperature_topic = "sensors_temperature"
humidity_topic = "sensors_humidity"

temperature_data = [
    {
        "sensor_id": 1,
        "timestamp": "2023-09-06T14:30:45",
        "value": 21.98
    },
    {
        "sensor_id": 2,
        "timestamp": "2023-09-06T14:30:45",
        "value": 26.15
    },
    {
        "sensor_id": 3,
        "timestamp": "2023-09-06T14:30:45",
        "value": 28.05
    },
    {
        "sensor_id": 4,
        "timestamp": "2023-09-06T14:30:45",
        "value": 29.89
    },
    {
        "sensor_id": 5,
        "timestamp": "2023-09-06T14:30:45",
        "value": 26.77
    },
    {
        "sensor_id": 6,
        "timestamp": "2023-09-06T14:30:45",
        "value": 25.73
    },
    {
        "sensor_id": 7,
        "timestamp": "2023-09-06T14:30:45",
        "value": 23.12
    },
    {
        "sensor_id": 8,
        "timestamp": "2023-09-06T14:30:45",
        "value": 21.67
    },
    {
        "sensor_id": 9,
        "timestamp": "2023-09-06T14:30:45",
        "value": 20.58
    },
    {
        "sensor_id": 10,
        "timestamp": "2023-09-06T14:30:45",
        "value": 25.48
    },
    {
        "sensor_id": 11,
        "timestamp": "2023-09-06T14:30:45",
        "value": 28.39
    },
    {
        "sensor_id": 12,
        "timestamp": "2023-09-06T14:30:45",
        "value": 27.56
    },
    {
        "sensor_id": 13,
        "timestamp": "2023-09-06T14:30:45",
        "value": 20.04
    },
    {
        "sensor_id": 14,
        "timestamp": "2023-09-06T14:30:45",
        "value": 27.03
    },
    {
        "sensor_id": 15,
        "timestamp": "2023-09-06T14:30:45",
        "value": 22.87
    },
    {
        "sensor_id": 16,
        "timestamp": "2023-09-06T14:30:45",
        "value": 23.81
    },
    {
        "sensor_id": 17,
        "timestamp": "2023-09-06T14:30:45",
        "value": 23.43
    },
    {
        "sensor_id": 18,
        "timestamp": "2023-09-06T14:30:45",
        "value": 28.06
    },
    {
        "sensor_id": 19,
        "timestamp": "2023-09-06T14:30:45",
        "value": 28.59
    },
    {
        "sensor_id": 20,
        "timestamp": "2023-09-06T14:30:45",
        "value": 23.13
    },
    {
        "sensor_id": 21,
        "timestamp": "2023-09-06T14:30:45",
        "value": 21.84
    },
    {
        "sensor_id": 22,
        "timestamp": "2023-09-06T14:30:45",
        "value": 22.12
    },
    {
        "sensor_id": 23,
        "timestamp": "2023-09-06T14:30:45",
        "value": 27.31
    },
    {
        "sensor_id": 24,
        "timestamp": "2023-09-06T14:30:45",
        "value": 30.0
    },
    {
        "sensor_id": 25,
        "timestamp": "2023-09-06T14:30:45",
        "value": 27.53
    },
    {
        "sensor_id": 26,
        "timestamp": "2023-09-06T14:30:45",
        "value": 25.8
    },
    {
        "sensor_id": 27,
        "timestamp": "2023-09-06T14:30:45",
        "value": 28.75
    },
    {
        "sensor_id": 28,
        "timestamp": "2023-09-06T14:30:45",
        "value": 24.83
    },
    {
        "sensor_id": 29,
        "timestamp": "2023-09-06T14:30:45",
        "value": 20.5
    },
    {
        "sensor_id": 30,
        "timestamp": "2023-09-06T14:30:45",
        "value": 21.07
    },
    {
        "sensor_id": 31,
        "timestamp": "2023-09-06T14:30:45",
        "value": 25.83
    },
    {
        "sensor_id": 32,
        "timestamp": "2023-09-06T14:30:45",
        "value": 26.17
    },
    {
        "sensor_id": 33,
        "timestamp": "2023-09-06T14:30:45",
        "value": 20.98
    },
    {
        "sensor_id": 34,
        "timestamp": "2023-09-06T14:30:45",
        "value": 22.35
    },
    {
        "sensor_id": 35,
        "timestamp": "2023-09-06T14:30:45",
        "value": 25.32
    },
    {
        "sensor_id": 36,
        "timestamp": "2023-09-06T14:30:45",
        "value": 24.76
    },
    {
        "sensor_id": 37,
        "timestamp": "2023-09-06T14:30:45",
        "value": 28.06
    },
    {
        "sensor_id": 38,
        "timestamp": "2023-09-06T14:30:45",
        "value": 24.57
    },
    {
        "sensor_id": 39,
        "timestamp": "2023-09-06T14:30:45",
        "value": 26.52
    },
    {
        "sensor_id": 40,
        "timestamp": "2023-09-06T14:30:45",
        "value": 28.6
    },
    {
        "sensor_id": 41,
        "timestamp": "2023-09-06T14:30:45",
        "value": 22.38
    },
    {
        "sensor_id": 42,
        "timestamp": "2023-09-06T14:30:45",
        "value": 21.1
    },
    {
        "sensor_id": 43,
        "timestamp": "2023-09-06T14:30:45",
        "value": 23.0
    },
    {
        "sensor_id": 44,
        "timestamp": "2023-09-06T14:30:45",
        "value": 20.44
    },
    {
        "sensor_id": 45,
        "timestamp": "2023-09-06T14:30:45",
        "value": 26.39
    },
    {
        "sensor_id": 46,
        "timestamp": "2023-09-06T14:30:45",
        "value": 25.19
    },
    {
        "sensor_id": 47,
        "timestamp": "2023-09-06T14:30:45",
        "value": 21.54
    },
    {
        "sensor_id": 48,
        "timestamp": "2023-09-06T14:30:45",
        "value": 25.92
    },
    {
        "sensor_id": 49,
        "timestamp": "2023-09-06T14:30:45",
        "value": 29.63
    },
    {
        "sensor_id": 50,
        "timestamp": "2023-09-06T14:30:45",
        "value": 25.82
    },
    {
        "sensor_id": 51,
        "timestamp": "2023-09-06T14:30:45",
        "value": 24.84
    },
    {
        "sensor_id": 52,
        "timestamp": "2023-09-06T14:30:45",
        "value": 29.58
    },
    {
        "sensor_id": 53,
        "timestamp": "2023-09-06T14:30:45",
        "value": 26.52
    },
    {
        "sensor_id": 54,
        "timestamp": "2023-09-06T14:30:45",
        "value": 22.23
    },
    {
        "sensor_id": 55,
        "timestamp": "2023-09-06T14:30:45",
        "value": 28.98
    },
    {
        "sensor_id": 56,
        "timestamp": "2023-09-06T14:30:45",
        "value": 25.73
    },
    {
        "sensor_id": 57,
        "timestamp": "2023-09-06T14:30:45",
        "value": 27.06
    },
    {
        "sensor_id": 58,
        "timestamp": "2023-09-06T14:30:45",
        "value": 24.59
    },
    {
        "sensor_id": 59,
        "timestamp": "2023-09-06T14:30:45",
        "value": 23.1
    },
    {
        "sensor_id": 60,
        "timestamp": "2023-09-06T14:30:45",
        "value": 28.23
    },
    {
        "sensor_id": 61,
        "timestamp": "2023-09-06T14:30:45",
        "value": 22.84
    },
    {
        "sensor_id": 62,
        "timestamp": "2023-09-06T14:30:45",
        "value": 28.23
    },
    {
        "sensor_id": 63,
        "timestamp": "2023-09-06T14:30:45",
        "value": 28.37
    },
    {
        "sensor_id": 64,
        "timestamp": "2023-09-06T14:30:45",
        "value": 23.47
    },
    {
        "sensor_id": 65,
        "timestamp": "2023-09-06T14:30:45",
        "value": 22.59
    },
    {
        "sensor_id": 66,
        "timestamp": "2023-09-06T14:30:45",
        "value": 24.11
    },
    {
        "sensor_id": 67,
        "timestamp": "2023-09-06T14:30:45",
        "value": 26.36
    },
    {
        "sensor_id": 68,
        "timestamp": "2023-09-06T14:30:45",
        "value": 26.72
    },
    {
        "sensor_id": 69,
        "timestamp": "2023-09-06T14:30:45",
        "value": 24.65
    },
    {
        "sensor_id": 70,
        "timestamp": "2023-09-06T14:30:45",
        "value": 27.46
    },
    {
        "sensor_id": 71,
        "timestamp": "2023-09-06T14:30:45",
        "value": 21.6
    },
    {
        "sensor_id": 72,
        "timestamp": "2023-09-06T14:30:45",
        "value": 20.49
    },
    {
        "sensor_id": 73,
        "timestamp": "2023-09-06T14:30:45",
        "value": 24.13
    },
    {
        "sensor_id": 74,
        "timestamp": "2023-09-06T14:30:45",
        "value": 22.68
    },
    {
        "sensor_id": 75,
        "timestamp": "2023-09-06T14:30:45",
        "value": 23.01
    },
    {
        "sensor_id": 76,
        "timestamp": "2023-09-06T14:30:45",
        "value": 21.38
    },
    {
        "sensor_id": 77,
        "timestamp": "2023-09-06T14:30:45",
        "value": 21.52
    },
    {
        "sensor_id": 78,
        "timestamp": "2023-09-06T14:30:45",
        "value": 28.2
    },
    {
        "sensor_id": 79,
        "timestamp": "2023-09-06T14:30:45",
        "value": 28.41
    },
    {
        "sensor_id": 80,
        "timestamp": "2023-09-06T14:30:45",
        "value": 26.47
    },
    {
        "sensor_id": 81,
        "timestamp": "2023-09-06T14:30:45",
        "value": 24.86
    },
    {
        "sensor_id": 82,
        "timestamp": "2023-09-06T14:30:45",
        "value": 24.62
    },
    {
        "sensor_id": 83,
        "timestamp": "2023-09-06T14:30:45",
        "value": 27.64
    },
    {
        "sensor_id": 84,
        "timestamp": "2023-09-06T14:30:45",
        "value": 29.46
    },
    {
        "sensor_id": 85,
        "timestamp": "2023-09-06T14:30:45",
        "value": 21.62
    },
    {
        "sensor_id": 86,
        "timestamp": "2023-09-06T14:30:45",
        "value": 23.15
    },
    {
        "sensor_id": 87,
        "timestamp": "2023-09-06T14:30:45",
        "value": 29.97
    },
    {
        "sensor_id": 88,
        "timestamp": "2023-09-06T14:30:45",
        "value": 24.45
    },
    {
        "sensor_id": 89,
        "timestamp": "2023-09-06T14:30:45",
        "value": 27.26
    },
    {
        "sensor_id": 90,
        "timestamp": "2023-09-06T14:30:45",
        "value": 24.59
    },
    {
        "sensor_id": 91,
        "timestamp": "2023-09-06T14:30:45",
        "value": 20.5
    },
    {
        "sensor_id": 92,
        "timestamp": "2023-09-06T14:30:45",
        "value": 20.31
    },
    {
        "sensor_id": 93,
        "timestamp": "2023-09-06T14:30:45",
        "value": 20.74
    },
    {
        "sensor_id": 94,
        "timestamp": "2023-09-06T14:30:45",
        "value": 20.48
    },
    {
        "sensor_id": 95,
        "timestamp": "2023-09-06T14:30:45",
        "value": 26.48
    },
    {
        "sensor_id": 96,
        "timestamp": "2023-09-06T14:30:45",
        "value": 28.58
    },
    {
        "sensor_id": 97,
        "timestamp": "2023-09-06T14:30:45",
        "value": 24.73
    },
    {
        "sensor_id": 98,
        "timestamp": "2023-09-06T14:30:45",
        "value": 29.86
    },
    {
        "sensor_id": 99,
        "timestamp": "2023-09-06T14:30:45",
        "value": 21.1
    },
    {
        "sensor_id": 100,
        "timestamp": "2023-09-06T14:30:45",
        "value": 22.4
    }
]
humidity_data = [
    {
        "sensor_id": 1,
        "timestamp": "2023-09-06T14:30:45",
        "value": 49.78
    },
    {
        "sensor_id": 2,
        "timestamp": "2023-09-06T14:30:45",
        "value": 54.36
    },
    {
        "sensor_id": 3,
        "timestamp": "2023-09-06T14:30:45",
        "value": 42.39
    },
    {
        "sensor_id": 4,
        "timestamp": "2023-09-06T14:30:45",
        "value": 54.59
    },
    {
        "sensor_id": 5,
        "timestamp": "2023-09-06T14:30:45",
        "value": 55.12
    },
    {
        "sensor_id": 6,
        "timestamp": "2023-09-06T14:30:45",
        "value": 52.33
    },
    {
        "sensor_id": 7,
        "timestamp": "2023-09-06T14:30:45",
        "value": 44.68
    },
    {
        "sensor_id": 8,
        "timestamp": "2023-09-06T14:30:45",
        "value": 52.16
    },
    {
        "sensor_id": 9,
        "timestamp": "2023-09-06T14:30:45",
        "value": 40.21
    },
    {
        "sensor_id": 10,
        "timestamp": "2023-09-06T14:30:45",
        "value": 47.87
    },
    {
        "sensor_id": 11,
        "timestamp": "2023-09-06T14:30:45",
        "value": 57.83
    },
    {
        "sensor_id": 12,
        "timestamp": "2023-09-06T14:30:45",
        "value": 59.51
    },
    {
        "sensor_id": 13,
        "timestamp": "2023-09-06T14:30:45",
        "value": 57.28
    },
    {
        "sensor_id": 14,
        "timestamp": "2023-09-06T14:30:45",
        "value": 53.52
    },
    {
        "sensor_id": 15,
        "timestamp": "2023-09-06T14:30:45",
        "value": 49.6
    },
    {
        "sensor_id": 16,
        "timestamp": "2023-09-06T14:30:45",
        "value": 41.28
    },
    {
        "sensor_id": 17,
        "timestamp": "2023-09-06T14:30:45",
        "value": 50.6
    },
    {
        "sensor_id": 18,
        "timestamp": "2023-09-06T14:30:45",
        "value": 54.27
    },
    {
        "sensor_id": 19,
        "timestamp": "2023-09-06T14:30:45",
        "value": 57.3
    },
    {
        "sensor_id": 20,
        "timestamp": "2023-09-06T14:30:45",
        "value": 50.58
    },
    {
        "sensor_id": 21,
        "timestamp": "2023-09-06T14:30:45",
        "value": 42.6
    },
    {
        "sensor_id": 22,
        "timestamp": "2023-09-06T14:30:45",
        "value": 51.36
    },
    {
        "sensor_id": 23,
        "timestamp": "2023-09-06T14:30:45",
        "value": 55.19
    },
    {
        "sensor_id": 24,
        "timestamp": "2023-09-06T14:30:45",
        "value": 49.32
    },
    {
        "sensor_id": 25,
        "timestamp": "2023-09-06T14:30:45",
        "value": 58.41
    },
    {
        "sensor_id": 26,
        "timestamp": "2023-09-06T14:30:45",
        "value": 47.85
    },
    {
        "sensor_id": 27,
        "timestamp": "2023-09-06T14:30:45",
        "value": 59.23
    },
    {
        "sensor_id": 28,
        "timestamp": "2023-09-06T14:30:45",
        "value": 55.7
    },
    {
        "sensor_id": 29,
        "timestamp": "2023-09-06T14:30:45",
        "value": 42.93
    },
    {
        "sensor_id": 30,
        "timestamp": "2023-09-06T14:30:45",
        "value": 41.03
    },
    {
        "sensor_id": 31,
        "timestamp": "2023-09-06T14:30:45",
        "value": 40.86
    },
    {
        "sensor_id": 32,
        "timestamp": "2023-09-06T14:30:45",
        "value": 41.02
    },
    {
        "sensor_id": 33,
        "timestamp": "2023-09-06T14:30:45",
        "value": 58.95
    },
    {
        "sensor_id": 34,
        "timestamp": "2023-09-06T14:30:45",
        "value": 43.36
    },
    {
        "sensor_id": 35,
        "timestamp": "2023-09-06T14:30:45",
        "value": 49.33
    },
    {
        "sensor_id": 36,
        "timestamp": "2023-09-06T14:30:45",
        "value": 48.47
    },
    {
        "sensor_id": 37,
        "timestamp": "2023-09-06T14:30:45",
        "value": 54.16
    },
    {
        "sensor_id": 38,
        "timestamp": "2023-09-06T14:30:45",
        "value": 57.82
    },
    {
        "sensor_id": 39,
        "timestamp": "2023-09-06T14:30:45",
        "value": 45.55
    },
    {
        "sensor_id": 40,
        "timestamp": "2023-09-06T14:30:45",
        "value": 51.15
    },
    {
        "sensor_id": 41,
        "timestamp": "2023-09-06T14:30:45",
        "value": 43.68
    },
    {
        "sensor_id": 42,
        "timestamp": "2023-09-06T14:30:45",
        "value": 44.15
    },
    {
        "sensor_id": 43,
        "timestamp": "2023-09-06T14:30:45",
        "value": 55.84
    },
    {
        "sensor_id": 44,
        "timestamp": "2023-09-06T14:30:45",
        "value": 40.52
    },
    {
        "sensor_id": 45,
        "timestamp": "2023-09-06T14:30:45",
        "value": 59.33
    },
    {
        "sensor_id": 46,
        "timestamp": "2023-09-06T14:30:45",
        "value": 47.93
    },
    {
        "sensor_id": 47,
        "timestamp": "2023-09-06T14:30:45",
        "value": 50.33
    },
    {
        "sensor_id": 48,
        "timestamp": "2023-09-06T14:30:45",
        "value": 40.17
    },
    {
        "sensor_id": 49,
        "timestamp": "2023-09-06T14:30:45",
        "value": 51.83
    },
    {
        "sensor_id": 50,
        "timestamp": "2023-09-06T14:30:45",
        "value": 43.3
    },
    {
        "sensor_id": 51,
        "timestamp": "2023-09-06T14:30:45",
        "value": 42.62
    },
    {
        "sensor_id": 52,
        "timestamp": "2023-09-06T14:30:45",
        "value": 40.26
    },
    {
        "sensor_id": 53,
        "timestamp": "2023-09-06T14:30:45",
        "value": 43.11
    },
    {
        "sensor_id": 54,
        "timestamp": "2023-09-06T14:30:45",
        "value": 50.11
    },
    {
        "sensor_id": 55,
        "timestamp": "2023-09-06T14:30:45",
        "value": 59.37
    },
    {
        "sensor_id": 56,
        "timestamp": "2023-09-06T14:30:45",
        "value": 58.08
    },
    {
        "sensor_id": 57,
        "timestamp": "2023-09-06T14:30:45",
        "value": 45.36
    },
    {
        "sensor_id": 58,
        "timestamp": "2023-09-06T14:30:45",
        "value": 50.07
    },
    {
        "sensor_id": 59,
        "timestamp": "2023-09-06T14:30:45",
        "value": 43.52
    },
    {
        "sensor_id": 60,
        "timestamp": "2023-09-06T14:30:45",
        "value": 41.92
    },
    {
        "sensor_id": 61,
        "timestamp": "2023-09-06T14:30:45",
        "value": 51.18
    },
    {
        "sensor_id": 62,
        "timestamp": "2023-09-06T14:30:45",
        "value": 58.17
    },
    {
        "sensor_id": 63,
        "timestamp": "2023-09-06T14:30:45",
        "value": 44.79
    },
    {
        "sensor_id": 64,
        "timestamp": "2023-09-06T14:30:45",
        "value": 45.77
    },
    {
        "sensor_id": 65,
        "timestamp": "2023-09-06T14:30:45",
        "value": 54.21
    },
    {
        "sensor_id": 66,
        "timestamp": "2023-09-06T14:30:45",
        "value": 54.22
    },
    {
        "sensor_id": 67,
        "timestamp": "2023-09-06T14:30:45",
        "value": 41.94
    },
    {
        "sensor_id": 68,
        "timestamp": "2023-09-06T14:30:45",
        "value": 55.66
    },
    {
        "sensor_id": 69,
        "timestamp": "2023-09-06T14:30:45",
        "value": 42.01
    },
    {
        "sensor_id": 70,
        "timestamp": "2023-09-06T14:30:45",
        "value": 44.36
    },
    {
        "sensor_id": 71,
        "timestamp": "2023-09-06T14:30:45",
        "value": 50.96
    },
    {
        "sensor_id": 72,
        "timestamp": "2023-09-06T14:30:45",
        "value": 53.39
    },
    {
        "sensor_id": 73,
        "timestamp": "2023-09-06T14:30:45",
        "value": 51.72
    },
    {
        "sensor_id": 74,
        "timestamp": "2023-09-06T14:30:45",
        "value": 59.23
    },
    {
        "sensor_id": 75,
        "timestamp": "2023-09-06T14:30:45",
        "value": 44.2
    },
    {
        "sensor_id": 76,
        "timestamp": "2023-09-06T14:30:45",
        "value": 43.45
    },
    {
        "sensor_id": 77,
        "timestamp": "2023-09-06T14:30:45",
        "value": 57.55
    },
    {
        "sensor_id": 78,
        "timestamp": "2023-09-06T14:30:45",
        "value": 42.95
    },
    {
        "sensor_id": 79,
        "timestamp": "2023-09-06T14:30:45",
        "value": 45.64
    },
    {
        "sensor_id": 80,
        "timestamp": "2023-09-06T14:30:45",
        "value": 41.75
    },
    {
        "sensor_id": 81,
        "timestamp": "2023-09-06T14:30:45",
        "value": 56.06
    },
    {
        "sensor_id": 82,
        "timestamp": "2023-09-06T14:30:45",
        "value": 47.45
    },
    {
        "sensor_id": 83,
        "timestamp": "2023-09-06T14:30:45",
        "value": 43.31
    },
    {
        "sensor_id": 84,
        "timestamp": "2023-09-06T14:30:45",
        "value": 40.24
    },
    {
        "sensor_id": 85,
        "timestamp": "2023-09-06T14:30:45",
        "value": 41.53
    },
    {
        "sensor_id": 86,
        "timestamp": "2023-09-06T14:30:45",
        "value": 58.31
    },
    {
        "sensor_id": 87,
        "timestamp": "2023-09-06T14:30:45",
        "value": 40.5
    },
    {
        "sensor_id": 88,
        "timestamp": "2023-09-06T14:30:45",
        "value": 57.93
    },
    {
        "sensor_id": 89,
        "timestamp": "2023-09-06T14:30:45",
        "value": 49.63
    },
    {
        "sensor_id": 90,
        "timestamp": "2023-09-06T14:30:45",
        "value": 45.09
    },
    {
        "sensor_id": 91,
        "timestamp": "2023-09-06T14:30:45",
        "value": 55.29
    },
    {
        "sensor_id": 92,
        "timestamp": "2023-09-06T14:30:45",
        "value": 50.38
    },
    {
        "sensor_id": 93,
        "timestamp": "2023-09-06T14:30:45",
        "value": 42.41
    },
    {
        "sensor_id": 94,
        "timestamp": "2023-09-06T14:30:45",
        "value": 45.99
    },
    {
        "sensor_id": 95,
        "timestamp": "2023-09-06T14:30:45",
        "value": 53.36
    },
    {
        "sensor_id": 96,
        "timestamp": "2023-09-06T14:30:45",
        "value": 56.7
    },
    {
        "sensor_id": 97,
        "timestamp": "2023-09-06T14:30:45",
        "value": 42.71
    },
    {
        "sensor_id": 98,
        "timestamp": "2023-09-06T14:30:45",
        "value": 50.36
    },
    {
        "sensor_id": 99,
        "timestamp": "2023-09-06T14:30:45",
        "value": 47.24
    },
    {
        "sensor_id": 100,
        "timestamp": "2023-09-06T14:30:45",
        "value": 52.1
    }
]

client = mqtt.Client()

# Connect to the broker
client.connect(broker_address, broker_port, keepalive_interval)

# Connect to the MQTT broker
# if client.is_connected():
#     print("Client is connected to the MQTT broker")
# else:
#     print("Client is not connected to the MQTT broker")

# Publish sensor data to MQTT topics
client.publish(temperature_topic, json.dumps(temperature_data))
client.publish(humidity_topic, json.dumps(humidity_data))
time.sleep(5)
print(f"Published temperature sensor data: {temperature_data}\nPublished humidity sensor data: {humidity_data}")

# Disconnect from the broker
client.disconnect()
