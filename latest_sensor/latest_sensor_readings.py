import pymongo
from pymongo import MongoClient
import redis,json

# MongoDB connection parameters
host = "localhost"
port = 27017
MONGO_DB = "testdata"
username = "admin"
password = "adminpassword"


# Redis connection parameters
REDIS_HOST = "localhost"
REDIS_PORT = 6379

# Connect to MongoDB
connection_uri = f"mongodb://{username}:{password}@{host}:{port}"

# Access the database and collection
client = MongoClient(connection_uri)
db = client.admin  # Connect to the admin database
collection = db.mahesh_sensor_data
try:
    db.command('ismaster')  # A simple command to test the connection
    print("Connected to MongoDB successfully!")
except pymongo.errors.ConnectionFailure as e:
    print("MongoDB connection failed:", e)
# Connect to Redis
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

# Check the connection
try:
    response = redis_client.ping()
    if response:
        print("Connected to Redis!")
    else:
        print("Failed to connect to Redis.")
except ConnectionError as e:
    print("Error: Unable to connect to Redis -", e)

# Retrieve the latest ten sensor readings from MongoDB
latest_readings = list(collection.find().sort([('_id', -1)]).limit(10))
# latest_readings = list(collection.find({"sensor_id": {"$gte": 1, "$lte": 5}}))
print(latest_readings)
# Store the readings in Redis
for reading in latest_readings:
    json_reading = json.dumps(reading, default=str)  # Convert dict to JSON string
    redis_client.lpush("latest_readings", json_reading)
    print(json_reading)
# print(json_reading)
# Close connections
client.close()
redis_client.close()
