import pymongo
from fastapi import FastAPI, HTTPException, Query
from pymongo import MongoClient
import redis
import json
from typing import List, Dict

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
db = client.admin  # Connect to the admin database
collection = db.testdata

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

@app.get("/sensor-readings")
def get_sensor_readings(start: str = Query(...), end: str = Query(...)):
    try:
        # Query MongoDB for sensor readings within the specified range
        sensor_readings = collection.find({
            "timestamp": {
                "$gte": start,
                "$lte": end
            }
        })
        return list(sensor_readings)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/last-ten-sensor-readings")
def get_last_ten_sensor_readings(sensor_id: int = Query(...)):
    try:
        # Query Redis for the last ten sensor readings for the specified sensor
        sensor_readings = redis_client.lrange(f"sensor:{sensor_id}", 0, 9)
        return sensor_readings
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
