import pymongo
from pymongo import MongoClient

# MongoDB connection parameters
host = "localhost"
port = 27017
MONGO_DB = "testdata"
username = "admin"
password = "adminpassword"

# Create a MongoClient instance with authentication
connection_uri = f"mongodb://{username}:{password}@{host}:{port}"

# Access the database and collection
client = MongoClient(connection_uri)
db = client.admin  # Connect to the admin database
collection = db.sensor_data_collection

# Check if the connection is successful
try:
    db.command('ismaster')  # A simple command to test the connection
    print("Connected to MongoDB successfully!")
except pymongo.errors.ConnectionFailure as e:
    print("MongoDB connection failed:", e)
# Example query to retrieve all documents from the collection
documents = collection.find()

print(documents)
# Iterate through the retrieved documents
for document in documents:
    print(document)


# Query documents where the value of the "sensor_type" field is "temperature"
query = {"sensor_type": "temperature"}
documents = collection.find(query)


# Close the MongoDB connection
client.close()
