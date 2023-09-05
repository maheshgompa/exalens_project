import json
import paho.mqtt.client as mqtt

# MQTT broker settings
broker_address = "localhost"  # Change this to your broker's IP address or hostname
port = 1883
topic = "test2/topic"  # Change this to the MQTT topic you want to subscribe to

# MQTT on_connect callback
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with code:", rc)
    client.subscribe(topic)

# MQTT on_message callback
def on_message(client, userdata, message):
    payload = message.payload.decode('utf-8')
    try:
        json_data = json.loads(payload)
        print("Received JSON data:", json_data)
    except json.JSONDecodeError as e:
        print("Received non-JSON message:", payload)

# Create an MQTT client instance
client = mqtt.Client()

# Set the callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(broker_address, port)

# Start the MQTT loop
client.loop_forever()