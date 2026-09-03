from dotenv import load_dotenv
import os
load_dotenv()

uri = os.getenv("MONGO_URI")
db_name = os.getenv("DB_NAME")

print("MONGO_URI value:", uri)
print("DB_NAME value:", db_name)