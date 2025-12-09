from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import properties_address_controller
from my_project.auth.domain import PropertiesAddress

properties_address_bp = Blueprint('properties_address', __name__, url_prefix='/properties-address')


@properties_address_bp.get('')
def get_all_properties_address() -> Response:
    """
    Get all property addresses
    ---
    tags:
      - PropertiesAddress
    responses:
      200:
        description: List of all property addresses
    """
    return make_response(jsonify(properties_address_controller.find_all()), HTTPStatus.OK)


@properties_address_bp.post('')
def create_properties_address() -> Response:
    """
    Create new property address
    ---
    tags:
      - PropertiesAddress
    parameters:
      - in: body
        name: properties_address
        description: Property address data
        required: true
        schema:
          type: object
          properties:
            address:
              type: string
              description: Street address
            city:
              type: string
              description: City name
            country:
              type: string
              description: Country name
    responses:
      201:
        description: Property address created successfully
    """
    content = request.get_json()
    properties_address = PropertiesAddress.create_from_dto(content)
    properties_address_controller.create(properties_address)
    return make_response(jsonify(properties_address.put_into_dto()), HTTPStatus.CREATED)


@properties_address_bp.get('/<int:properties_address_id>')
def get_properties_address(properties_address_id: int) -> Response:
    """
    Get property address by ID
    ---
    tags:
      - PropertiesAddress
    parameters:
      - in: path
        name: properties_address_id
        type: integer
        required: true
        description: Property address ID
    responses:
      200:
        description: Property address data
      404:
        description: Property address not found
    """
    return make_response(jsonify(properties_address_controller.find_by_id(properties_address_id)), HTTPStatus.OK)


@properties_address_bp.put('/<int:properties_address_id>')
def bugfix_properties_address(properties_address_id: int) -> Response:
    """
    Update property address by ID
    ---
    tags:
      - PropertiesAddress
    parameters:
      - in: path
        name: properties_address_id
        type: integer
        required: true
        description: Property address ID
      - in: body
        name: properties_address
        description: Updated property address data
        required: true
        schema:
          type: object
          properties:
            address:
              type: string
              description: Street address
            city:
              type: string
              description: City name
            country:
              type: string
              description: Country name
    responses:
      200:
        description: Property address updated successfully
      404:
        description: Property address not found
    """
    content = request.get_json()
    properties_address = PropertiesAddress.create_from_dto(content)
    properties_address_controller.bugfix(properties_address_id, properties_address)
    return make_response("properties_address updated", HTTPStatus.OK)


@properties_address_bp.patch('/<int:properties_address_id>')
def patch_properties_address(properties_address_id: int) -> Response:
    """
    Partially update property address by ID
    ---
    tags:
      - PropertiesAddress
    parameters:
      - in: path
        name: properties_address_id
        type: integer
        required: true
        description: Property address ID
      - in: body
        name: properties_address
        description: Partial property address data
        required: true
        schema:
          type: object
          properties:
            address:
              type: string
              description: Street address
            city:
              type: string
              description: City name
            country:
              type: string
              description: Country name
    responses:
      200:
        description: Property address updated successfully
      404:
        description: Property address not found
    """
    content = request.get_json()
    properties_address_controller.patch(properties_address_id, content)
    return make_response("properties_address updated", HTTPStatus.OK)


@properties_address_bp.delete('/<int:properties_address_id>')
def delete_properties_address(properties_address_id: int) -> Response:
    """
    Delete property address by ID
    ---
    tags:
      - PropertiesAddress
    parameters:
      - in: path
        name: properties_address_id
        type: integer
        required: true
        description: Property address ID
    responses:
      200:
        description: Property address deleted successfully
      404:
        description: Property address not found
    """
    properties_address_controller.delete(properties_address_id)
    return make_response("properties_address deleted", HTTPStatus.OK)


