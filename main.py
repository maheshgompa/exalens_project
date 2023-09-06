import pymongo
from fastapi import FastAPI, HTTPException, Query
from pymongo import MongoClient,ASCENDING
import redis
import json
from typing import List, Dict
from datetime import datetime

app = FastAPI()

# MongoDB connection parameters
username = 'admin'
password = 'adminpassword'
host = 'localhost'
port = 27017

# Redis connection parameters
REDIS_HOST = "localhost"
REDIS_PORT = 6379

# Connect to MongoDB
connection_uri = f"mongodb://{username}:{password}@{host}:{port}"

# Connect to the database
client = pymongo.MongoClient(connection_uri)
db = client.admin
collection = db["sensor_data_reading"]

# Check if the connection is successful
try:
    db.command('ismaster')  # A simple command to test the connection
    print("Connected to MongoDB successfully!")
except pymongo.errors.ConnectionFailure as e:
    print("MongoDB connection failed:", e)

# Connect to Redis
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

# Check the connection
try:
    response = redis_client.ping()
    if response:
        print("Connected to Redis!")
    else:
        print("Failed to connect to Redis.")
except ConnectionError as e:
    print("Error: Unable to connect to Redis -", e)


# Define endpoint to fetch sensor readings by specifying a start and end range
@app.get("/sensor-readings/")
async def get_sensor_readings(start: str = Query(..., description="Start timestamp"),
                              end: str = Query(..., description="End timestamp")):
    # Query MongoDB based on the provided start and end timestamps
    if start and end:
        readings = collection.find({"timestamp": {"$gte": start, "$lte": end}})
    else:
        # If no range specified, return all readings
        readings = collection.find()

    # Convert MongoDB cursor to a list of readings
    readings_list = [reading for reading in readings]
    return {"sensor_readings": readings_list}


# Define endpoint to retrieve the last ten sensor readings for a specific sensor
@app.get("/last-ten-readings/{sensor_id}")
async def get_last_ten_readings(sensor_id: str):
    try:
        # Check if sensor_id exists in Redis
        if redis_client.exists(sensor_id):
            # Retrieve the last ten readings from Redis
            last_ten_readings = redis_client.lrange(sensor_id, 0, 9)
            return {"sensor_id": sensor_id, "last_ten_readings": last_ten_readings}

        # If not found in Redis, check MongoDB (assuming MongoDB has the sensor data)
        collection = db["sensor_data"]  # Replace with your MongoDB collection name
        sensor_data = collection.find({"sensor_id": sensor_id}).limit(10).sort([("timestamp", -1)])

        # Extract the last ten readings from MongoDB
        last_ten_readings = [{"value": data["value"], "timestamp": data["timestamp"]} for data in sensor_data]
        return {"sensor_id": sensor_id, "last_ten_readings": last_ten_readings}

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)