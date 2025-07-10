from flask import jsonify
from datetime import datetime
from bson.objectid import ObjectId
from bson.errors import InvalidId
from app.utils.db import datasets_col, quality_logs_col

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
    try:
        _id = ObjectId(dataset_id)
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

    result = datasets_col.update_one(
        {"_id": _id, "is_deleted": False},
        {"$set": update_fields}
    )

    if result.matched_count == 0:
        return jsonify({"Error": "Dataset not found"}), 404

    updated = datasets_col.find_one({"_id": _id})
    updated["_id"] = str(updated["_id"])

    return jsonify(updated), 200

def soft_delete_dataset(dataset_id):
    try:
        _id = ObjectId(dataset_id)
    except InvalidId:
        return jsonify({"Error": "Invalid dataset ID"}), 400

    result = datasets_col.update_one(
        {"_id": _id, "is_deleted": False},
        {"$set": {
            "is_deleted": True, 
            "updated_at": datetime.now()
        }}
    )

    if result.matched_count == 0:
        return jsonify({"Error": "Dataset not found or already deleted"}), 404

    return jsonify({"message": "Dataset soft-deleted successfully"}), 200

def add_quality_log(dataset_id, data):
    try:
        _id = ObjectId(dataset_id)
    except InvalidId:
        return jsonify({"Error": "Invalid dataset ID"}), 400

    dataset = datasets_col.find_one({"_id": _id, "is_deleted": False})
    if not dataset:
        return jsonify({"Error": "Dataset not found"}), 404

    status = data.get("status")
    details = data.get("details", "")

    if status not in ["PASS", "FAIL"]:
        return jsonify({"Error": "Status must be either 'PASS' or 'FAIL'"}), 400

    log = {
        "dataset_id": _id,
        "status": status,
        "details": details,
        "timestamp": datetime.now()
    }

    result = quality_logs_col.insert_one(log)
    log["_id"] = str(result.inserted_id)
    log["dataset_id"] = str(log["dataset_id"])
    log["timestamp"] = log["timestamp"].isoformat()

    return jsonify(log), 201

def get_quality_logs(dataset_id):
    try:
        _id = ObjectId(dataset_id)
    except InvalidId:
        return jsonify({"Error": "Invalid dataset ID"}), 400

    dataset = datasets_col.find_one({"_id": _id, "is_deleted": False})
    if not dataset:
        return jsonify({"Error": "Dataset not found"}), 404

    logs = list(quality_logs_col.find({"dataset_id": _id}))
    for log in logs:
        log["_id"] = str(log["_id"])
        log["dataset_id"] = str(log["dataset_id"])
        log["timestamp"] = log["timestamp"].isoformat()

    return jsonify(logs), 200
