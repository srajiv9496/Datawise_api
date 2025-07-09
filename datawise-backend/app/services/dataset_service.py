from flask import jsonify
from datetime import datetime
from bson.objectid import ObjectId
from bson.errors import InvalidId
from app.utils.db import datasets_col

def create_dataset(data):
    required_fields = ["name", "owner", "tags"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    dataset = {
        "name": data["name"],
        "owner": data["owner"],
        "description": data.get("description", ""),
        "tags": data.get("tags", []),
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "is_deleted": False
    }

    result = datasets_col.insert_one(dataset)
    dataset["_id"] = str(result.inserted_id)

    return jsonify(dataset), 201

def get_datasets(query_params):
    filters = {"is_deleted": False}

    owner = query_params.get("owner")
    tag = query_params.get("tag")

    if owner:
        filters["owner"] = owner

    if tag:
        filters["tags"] = {"$in": [tag]}

    datasets = list(datasets_col.find(filters))
    for dataset in datasets:
        dataset["_id"] = str(dataset["_id"])

    return jsonify(datasets), 200

def get_dataset(dataset_id):
    try: _id = ObjectId(dataset_id)
    except InvalidId:
        return jsonify({"Error": "Invalid dataset ID"}), 400
    
    dataset = datasets_col.find_one({"_id": _id, "is_deleted": False})
    if not dataset:
        return jsonify({"Error": "Dataset not found"}), 404
    
    dataset["_id"] = str(dataset["_id"])
    return jsonify(dataset), 200

def update_dataset(dataset_id, data):
    try: 
        _id = ObjectId(dataset_id)
    except InvalidId:
        return jsonify({"Error": "Invalid dataset ID"}), 400
    
    allowed_fields = {"name", "owner", "description", "tags"}
    update_fields = {k: v for k, v in data.items() if k in allowed_fields}

    if not update_fields:
        return jsonify({"Error": "No valid fields to update"}), 400
    
    update_fields["updated_at"] = datetime.now()

    result  = datasets_col.update_one(
        {"_id": _id, "is_deleted": False},
        {"$set": update_fields}
    )

    if result.matched_count == 0:
        return jsonify({"Error": "Dataset not found"}), 404
    
    updated = datasets_col.find_one({"_id": _id})
    updated["_id"] = str(updated["_id"])

    return jsonify(updated), 200