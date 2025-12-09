from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import property_photos_controller
from my_project.auth.domain import PropertyPhotos

property_photos_bp = Blueprint('property_photos', __name__, url_prefix='/property-photos')


@property_photos_bp.get('')
def get_all_property_photos() -> Response:
    """
    Get all property photos
    ---
    tags:
      - PropertyPhotos
    responses:
      200:
        description: List of all property photos
    """
    return make_response(jsonify(property_photos_controller.find_all()), HTTPStatus.OK)


@property_photos_bp.post('')
def create_property_photos() -> Response:
    """
    Create new property photo
    ---
    tags:
      - PropertyPhotos
    parameters:
      - in: body
        name: property_photo
        description: Property photo data
        required: true
        schema:
          type: object
          properties:
            property_id:
              type: integer
              description: Property ID
            photo_url:
              type: string
              description: Photo URL
            uploaded_at:
              type: string
              format: date-time
              description: Upload timestamp
    responses:
      201:
        description: Property photo created successfully
    """
    content = request.get_json()
    property_photos = PropertyPhotos.create_from_dto(content)
    property_photos_controller.create(property_photos)
    return make_response(jsonify(property_photos.put_into_dto()), HTTPStatus.CREATED)


@property_photos_bp.get('/<int:property_photos_id>')
def get_property_photos(property_photos_id: int) -> Response:
    """
    Get property photo by ID
    ---
    tags:
      - PropertyPhotos
    parameters:
      - in: path
        name: property_photos_id
        type: integer
        required: true
        description: Property photo ID
    responses:
      200:
        description: Property photo data
      404:
        description: Property photo not found
    """
    return make_response(jsonify(property_photos_controller.find_by_id(property_photos_id)), HTTPStatus.OK)


@property_photos_bp.put('/<int:property_photos_id>')
def bugfix_property_photos(property_photos_id: int) -> Response:
    """
    Update property photo by ID
    ---
    tags:
      - PropertyPhotos
    parameters:
      - in: path
        name: property_photos_id
        type: integer
        required: true
        description: Property photo ID
      - in: body
        name: property_photo
        description: Updated property photo data
        required: true
        schema:
          type: object
          properties:
            property_id:
              type: integer
              description: Property ID
            photo_url:
              type: string
              description: Photo URL
            uploaded_at:
              type: string
              format: date-time
              description: Upload timestamp
    responses:
      200:
        description: Property photo updated successfully
      404:
        description: Property photo not found
    """
    content = request.get_json()
    property_photos = PropertyPhotos.create_from_dto(content)
    property_photos_controller.bugfix(property_photos_id, property_photos)
    return make_response("property_photos updated", HTTPStatus.OK)


@property_photos_bp.patch('/<int:property_photos_id>')
def patch_property_photos(property_photos_id: int) -> Response:
    """
    Partially update property photo by ID
    ---
    tags:
      - PropertyPhotos
    parameters:
      - in: path
        name: property_photos_id
        type: integer
        required: true
        description: Property photo ID
      - in: body
        name: property_photo
        description: Partial property photo data
        required: true
        schema:
          type: object
          properties:
            property_id:
              type: integer
              description: Property ID
            photo_url:
              type: string
              description: Photo URL
            uploaded_at:
              type: string
              format: date-time
              description: Upload timestamp
    responses:
      200:
        description: Property photo updated successfully
      404:
        description: Property photo not found
    """
    content = request.get_json()
    property_photos_controller.patch(property_photos_id, content)
    return make_response("property_photos updated", HTTPStatus.OK)


@property_photos_bp.delete('/<int:property_photos_id>')
def delete_property_photos(property_photos_id: int) -> Response:
    """
    Delete property photo by ID
    ---
    tags:
      - PropertyPhotos
    parameters:
      - in: path
        name: property_photos_id
        type: integer
        required: true
        description: Property photo ID
    responses:
      200:
        description: Property photo deleted successfully
      404:
        description: Property photo not found
    """
    property_photos_controller.delete(property_photos_id)
    return make_response("property_photos deleted", HTTPStatus.OK)


@property_photos_bp.get('/get-photos-after-property/<int:property_id>')
def get_photos_by_property(property_id: int) -> Response:
    """
    Get photos by property ID
    ---
    tags:
      - PropertyPhotos
    parameters:
      - in: path
        name: property_id
        type: integer
        required: true
        description: Property ID
    responses:
      200:
        description: List of photos for the property
      404:
        description: Property not found
    """
    return make_response(jsonify(property_photos_controller.get_photos_by_property(property_id)),
                         HTTPStatus.OK)
