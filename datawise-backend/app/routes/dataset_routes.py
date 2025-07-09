from flask import Blueprint, request, jsonify   
from app.services import dataset_service
from app.utils.db import datasets_col

dataset_bp = Blueprint('datasets', __name__, url_prefix='/datasets')

@dataset_bp.route('', methods=['POST'])
def create_dataset():
    """
    Create a new dataset
    ---
    tags:
      - Datasets
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - name
            - owner
            - tags
          properties:
            name:
              type: string
            owner:
              type: string
            description:
              type: string
            tags:
              type: array
              items:
                type: string
    responses:
      201:
        description: Dataset created successfully
      400:
        description: Missing required fields
    """
    return dataset_service.create_dataset(request.json)


@dataset_bp.route('', methods=['GET'])
def get_datasets():
    """
    List all datasets (with optional filters)
    ---
    tags:
      - Datasets
    parameters:
      - name: owner
        in: query
        type: string
        required: false
        description: Filter by owner
      - name: tag
        in: query
        type: string
        required: false
        description: Filter by tag
    responses:
      200:
        description: List of datasets
    """
    return dataset_service.get_datasets(request.args)


@dataset_bp.route('/<id>', methods=['GET'])
def get_dataset(id):
    """
        Get dataset by ID
        ```
        tags:
        - Datasets
        parameters:
            -name: id
             in: path
             type: string
             required: true
             description: The ID of the dataset responses:
             200:
               description: Dataset found
             400:
                description: Invalid dataset ID format
             404:
               description: Dataset not found
    """
    return dataset_service.get_dataset(id)


@dataset_bp.route('/<id>', methods=['PUT'])
def update_dataset(id):
    """
    Update a datasset
    ---
    tags:
        - Datasets  
    parameters:
        - name: id
          in: path
          type: string
          required: true
          description: ID of the dataset
        - in: body
          schema:
            type: object
            properties:
                name: 
                  type: string
                owner: 
                  type: string
                description:
                  type: string
                tags:
                  type: array
                  items: 
                    type: string
    
    response:
        200:
            description: Dataset updated
        400: 
            description: Invalid ID or no valid fields
        404:
            description: Dataset not found
    """
    return dataset_service.update_dataset(id, request.json)


@dataset_bp.route('/<id>', methods=['DELETE'])
def delete_dataset(id):
    return dataset_service.soft_delete_dataset(id)


@dataset_bp.route('/<id>/quality-1', methods=['POST'])
def add_quality_log(id):
    return dataset_service.add_quality_log(id, request.json)


@dataset_bp.route('/<id>/quality-1', methods=['GET'])
def get_quality_logs(id):
    return dataset_service.get_quality_logs(id)
