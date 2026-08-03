from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch values
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

# Connect MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
todo_collection = db["todos"]