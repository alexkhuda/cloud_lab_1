from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import properties_controller
from my_project.auth.domain import Properties

properties_bp = Blueprint('properties', __name__, url_prefix='/properties')


@properties_bp.get('')
def get_all_properties() -> Response:
    """
    Get all properties
    ---
    tags:
      - Properties
    responses:
      200:
        description: List of all properties
    """
    return make_response(jsonify(properties_controller.find_all()), HTTPStatus.OK)


@properties_bp.post('')
def create_properties() -> Response:
    """
    Create new property
    ---
    tags:
      - Properties
    parameters:
      - in: body
        name: property
        description: Property data
        required: true
        schema:
          type: object
          properties:
            user_id:
              type: integer
              description: Property owner user ID
            title:
              type: string
              description: Property title
            description:
              type: string
              description: Property description
            address_id:
              type: integer
              description: Address ID
            price_per_night:
              type: number
              format: float
              description: Price per night
            created_at:
              type: string
              format: date-time
              description: Creation timestamp
    responses:
      201:
        description: Property created successfully
    """
    content = request.get_json()
    properties = Properties.create_from_dto(content)
    properties_controller.create(properties)
    return make_response(jsonify(properties.put_into_dto()), HTTPStatus.CREATED)


@properties_bp.get('/<int:properties_id>')
def get_properties(properties_id: int) -> Response:
    """
    Get property by ID
    ---
    tags:
      - Properties
    parameters:
      - in: path
        name: properties_id
        type: integer
        required: true
        description: Property ID
    responses:
      200:
        description: Property data
      404:
        description: Property not found
    """
    return make_response(jsonify(properties_controller.find_by_id(properties_id)), HTTPStatus.OK)


@properties_bp.put('/<int:properties_id>')
def bugfix_properties(properties_id: int) -> Response:
    """
    Update property by ID
    ---
    tags:
      - Properties
    parameters:
      - in: path
        name: properties_id
        type: integer
        required: true
        description: Property ID
      - in: body
        name: property
        description: Updated property data
        required: true
        schema:
          type: object
          properties:
            user_id:
              type: integer
              description: Property owner user ID
            title:
              type: string
              description: Property title
            description:
              type: string
              description: Property description
            address_id:
              type: integer
              description: Address ID
            price_per_night:
              type: number
              format: float
              description: Price per night
            created_at:
              type: string
              format: date-time
              description: Creation timestamp
    responses:
      200:
        description: Property updated successfully
      404:
        description: Property not found
    """
    content = request.get_json()
    properties = Properties.create_from_dto(content)
    properties_controller.bugfix(properties_id, properties)
    return make_response("properties updated", HTTPStatus.OK)


@properties_bp.patch('/<int:properties_id>')
def patch_properties(properties_id: int) -> Response:
    """
    Partially update property by ID
    ---
    tags:
      - Properties
    parameters:
      - in: path
        name: properties_id
        type: integer
        required: true
        description: Property ID
      - in: body
        name: property
        description: Partial property data
        required: true
        schema:
          type: object
          properties:
            user_id:
              type: integer
              description: Property owner user ID
            title:
              type: string
              description: Property title
            description:
              type: string
              description: Property description
            address_id:
              type: integer
              description: Address ID
            price_per_night:
              type: number
              format: float
              description: Price per night
            created_at:
              type: string
              format: date-time
              description: Creation timestamp
    responses:
      200:
        description: Property updated successfully
      404:
        description: Property not found
    """
    content = request.get_json()
    properties_controller.patch(properties_id, content)
    return make_response("properties updated", HTTPStatus.OK)


@properties_bp.delete('/<int:properties_id>')
def delete_properties(properties_id: int) -> Response:
    """
    Delete property by ID
    ---
    tags:
      - Properties
    parameters:
      - in: path
        name: properties_id
        type: integer
        required: true
        description: Property ID
    responses:
      200:
        description: Property deleted successfully
      404:
        description: Property not found
    """
    properties_controller.delete(properties_id)
    return make_response("properties deleted", HTTPStatus.OK)


