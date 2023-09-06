import pymongo
import json
import paho.mqtt.client as mqtt


# MQTT settings
MQTT_BROKER_HOST = "localhost"  # MQTT broker host
# MQTT_TOPIC = "test2/topic"  # MQTT topic to subscribe to
temperature_topic = "sensors/temperature"
humidity_topic = "sensors/humidity"
# Connection details
username = 'admin'
password = 'adminpassword'
host = 'localhost'
port = 27017

# Create a connection URI
connection_uri = f"mongodb://{username}:{password}@{host}:{port}"

# Connect to the database
client = pymongo.MongoClient(connection_uri)
db = client.admin  # Connect to the admin database
collection = db.sensor_data_collection
# Check if the connection is successful
try:
    db.command('ismaster')  # A simple command to test the connection
    print("Connected to MongoDB successfully!")
except pymongo.errors.ConnectionFailure as e:
    print("MongoDB connection failed:", e)
def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8")
    # Process payload and insert into MongoDB
    data_to_insert = {"topic": message.topic, "payload": payload}
    collection.insert_one(data_to_insert)
    print("Inserted:", data_to_insert)

# Create MQTT client and set callback
client = mqtt.Client()
client.on_message = on_message

# Connect to MQTT broker and subscribe to the topic
client.connect(MQTT_BROKER_HOST)
client.subscribe(temperature_topic)
client.subscribe(humidity_topic)

# client.subscribe(MQTT_TOPIC)

# Start MQTT loop to process messages
client.loop_forever()

# Query and retrieve data from MongoDB
# retrieved_data = collection.find()
#
# for document in retrieved_data:
#     print("Topic:", document["topic"])
#     print("Payload:", document["payload"])
#     print("===")

# # Load JSON data from a file
# with open("sensor_data.json", "r") as file:
#     sensor_data = json.load(file)
#
# # Insert sensor data into the collection
# inserted_result = collection.insert_many(sensor_data)
# print("Inserted IDs:", inserted_result.inserted_ids)
# print()
# print(inserted_result)
# print()
# # Retrieve all sensor data
all_sensor_data = collection.find()
for doc in all_sensor_data:
    print("Sensor Data:", doc)


