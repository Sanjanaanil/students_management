from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Test connection
uri = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')
print(f"Connecting to: {uri}")

try:
    client = MongoClient(uri)
    # Force connection to verify
    client.admin.command('ping')
    print("✅ MongoDB connected successfully!")
    
    # List databases
    print("\nAvailable databases:")
    for db_name in client.list_database_names():
        print(f"  - {db_name}")
        
except Exception as e:
    print(f"❌ Connection failed: {e}")