from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["datawise_catalog"]

datasets_col = db["datasets"]
quality_logs_col = db["quality_logs"]
