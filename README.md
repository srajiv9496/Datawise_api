# Datawise Backend Assignment

This is a Flask + MongoDB based backend API for managing datasets and their quality logs.

## 🔧 Tech Stack
- Python 3.10+
- Flask 2.x
- MongoDB (via PyMongo)
- Pydantic (for validation)
- Pytest (for testing)
- Flasgger (for Swagger docs)

## 🚀 Setup

```bash
git clone <repo_url>
cd datawise-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

## 🧪 Run Tests 

```
pytest test/
```

# 📬 Sample API Requests

## ➕ Create Dataset

```
curl -X POST http://localhost:5000/datasets \
-H "Content-Type: application/json" \
-d '{"name":"Test","owner":"rajiv","tags":["a","b"]}'
```

## 📋 Get All Datasets
```
curl http://localhost:5000/datasets
```

With optional filters:
```
curl "http://localhost:5000/datasets?owner=rajiv&tag=analytics"

```

## 🔍 Get Datasets by ID
```
curl http://localhost:5000/datasets/<dataset_id>
```

## ✏️ Update Datasets
```
curl -X PUT http://localhost:5000/datasets/<dataset_id> \
-H "Content-Type: application/json" \
-d '{
  "description": "Updated description",
  "tags": ["updated", "reporting"]
}'
```

## 🗑️ Soft Delete Dataset
```
curl -X DELETE http://localhost:5000/datasets/<dataset_id>

```

## ✅ Add Quality Log
```
curl -X POST http://localhost:5000/datasets/<dataset_id>/quality-1 \
-H "Content-Type: application/json" \
-d '{
  "status": "PASS",
  "details": "Data looks good"
}'
```
## 📥 View Quality Logs

```
curl http://localhost:5000/datasets/<dataset_id>/quality-1
```

## 📚 API Docs
```
Visit http://localhost:5000/apidocs
```
## 📂 Project Structure
```arduino
.
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   └── dataset_routes.py
│   ├── services/
│   │   └── dataset_service.py
│   └── utils/
│       └── db.py
├── test/
│   └── test_datasets.py
├── requirements.txt
├── run.py
└── README.md
```