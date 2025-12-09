from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import promotions_controller
from my_project.auth.domain import Promotions

promotions_bp = Blueprint('promotions', __name__, url_prefix='/promotions')


@promotions_bp.get('')
def get_all_promotions() -> Response:
    """
    Get all promotions
    ---
    tags:
      - Promotions
    responses:
      200:
        description: List of all promotions
    """
    return make_response(jsonify(promotions_controller.find_all()), HTTPStatus.OK)


@promotions_bp.post('')
def create_promotions() -> Response:
    """
    Create new promotion
    ---
    tags:
      - Promotions
    parameters:
      - in: body
        name: promotion
        description: Promotion data
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              description: Promotion name
            discount_percentage:
              type: number
              format: float
              description: Discount percentage
            start_date:
              type: string
              format: date
              description: Promotion start date
            end_date:
              type: string
              format: date
              description: Promotion end date
            created_at:
              type: string
              format: date-time
              description: Creation timestamp
    responses:
      201:
        description: Promotion created successfully
    """
    content = request.get_json()
    promotions = Promotions.create_from_dto(content)
    promotions_controller.create(promotions)
    return make_response(jsonify(promotions.put_into_dto()), HTTPStatus.CREATED)


@promotions_bp.get('/<int:promotions_id>')
def get_promotions(promotions_id: int) -> Response:
    """
    Get promotion by ID
    ---
    tags:
      - Promotions
    parameters:
      - in: path
        name: promotions_id
        type: integer
        required: true
        description: Promotion ID
    responses:
      200:
        description: Promotion data
      404:
        description: Promotion not found
    """
    return make_response(jsonify(promotions_controller.find_by_id(promotions_id)), HTTPStatus.OK)


@promotions_bp.put('/<int:promotions_id>')
def bugfix_promotions(promotions_id: int) -> Response:
    """
    Update promotion by ID
    ---
    tags:
      - Promotions
    parameters:
      - in: path
        name: promotions_id
        type: integer
        required: true
        description: Promotion ID
      - in: body
        name: promotion
        description: Updated promotion data
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              description: Promotion name
            discount_percentage:
              type: number
              format: float
              description: Discount percentage
            start_date:
              type: string
              format: date
              description: Promotion start date
            end_date:
              type: string
              format: date
              description: Promotion end date
            created_at:
              type: string
              format: date-time
              description: Creation timestamp
    responses:
      200:
        description: Promotion updated successfully
      404:
        description: Promotion not found
    """
    content = request.get_json()
    promotions = Promotions.create_from_dto(content)
    promotions_controller.bugfix(promotions_id, promotions)
    return make_response("promotions updated", HTTPStatus.OK)


@promotions_bp.patch('/<int:promotions_id>')
def patch_promotions(promotions_id: int) -> Response:
    """
    Partially update promotion by ID
    ---
    tags:
      - Promotions
    parameters:
      - in: path
        name: promotions_id
        type: integer
        required: true
        description: Promotion ID
      - in: body
        name: promotion
        description: Partial promotion data
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              description: Promotion name
            discount_percentage:
              type: number
              format: float
              description: Discount percentage
            start_date:
              type: string
              format: date
              description: Promotion start date
            end_date:
              type: string
              format: date
              description: Promotion end date
            created_at:
              type: string
              format: date-time
              description: Creation timestamp
    responses:
      200:
        description: Promotion updated successfully
      404:
        description: Promotion not found
    """
    content = request.get_json()
    promotions_controller.patch(promotions_id, content)
    return make_response("promotions updated", HTTPStatus.OK)


@promotions_bp.delete('/<int:promotions_id>')
def delete_promotions(promotions_id: int) -> Response:
    """
    Delete promotion by ID
    ---
    tags:
      - Promotions
    parameters:
      - in: path
        name: promotions_id
        type: integer
        required: true
        description: Promotion ID
    responses:
      200:
        description: Promotion deleted successfully
      404:
        description: Promotion not found
    """
    promotions_controller.delete(promotions_id)
    return make_response("promotions deleted", HTTPStatus.OK)


