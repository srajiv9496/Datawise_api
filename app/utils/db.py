from pymongo import MongoClient
import os

mongo_uri = os.environ.get("MONGO_URI", "mongodb://localhost:27017/datawise")
client = MongoClient(mongo_uri)
db = client.get_database()
datasets_col = db.datasets
quality_logs_col = db.quality_logs
