from flask import Flask
from .routes.dataset_routes import dataset_bp
from flasgger import Swagger

def create_app():
    app = Flask(__name__)
    Swagger(app)

    app.register_blueprint(dataset_bp)

    return app
