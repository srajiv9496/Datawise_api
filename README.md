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
cd datawise-backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```
## 🧪 Run Tests 

```
pytest test/
```

## 📬 Sample API Requests
## ➕ Create Dataset

```
curl -X POST http://localhost:5000/datasets \
-H "Content-Type: application/json" \
-d '{"name":"Test","owner":"rajiv","tags":["a","b"]}'
```
## 📥 View Quality Logs

```
curl http://localhost:5000/datasets/<dataset_id>/quality-1
```

## 📚 API Docs
```
Visit http://localhost:5000/apidocs
```