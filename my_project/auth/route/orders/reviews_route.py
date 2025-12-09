from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import reviews_controller
from my_project.auth.domain import Reviews

reviews_bp = Blueprint('reviews', __name__, url_prefix='/reviews')


@reviews_bp.get('')
def get_all_reviews() -> Response:
    """
    Get all reviews
    ---
    tags:
      - Reviews
    responses:
      200:
        description: List of all reviews
    """
    return make_response(jsonify(reviews_controller.find_all()), HTTPStatus.OK)


@reviews_bp.post('')
def create_reviews() -> Response:
    """
    Create new review
    ---
    tags:
      - Reviews
    parameters:
      - in: body
        name: review
        description: Review data
        required: true
        schema:
          type: object
          properties:
            property_id:
              type: integer
              description: Property ID
            user_id:
              type: integer
              description: User ID
            rating:
              type: integer
              description: Rating (1-5)
            comment:
              type: string
              description: Review comment
            created_at:
              type: string
              format: date-time
              description: Creation timestamp
    responses:
      201:
        description: Review created successfully
    """
    content = request.get_json()
    reviews = Reviews.create_from_dto(content)
    reviews_controller.create(reviews)
    return make_response(jsonify(reviews.put_into_dto()), HTTPStatus.CREATED)


@reviews_bp.get('/<int:reviews_id>')
def get_reviews(reviews_id: int) -> Response:
    """
    Get review by ID
    ---
    tags:
      - Reviews
    parameters:
      - in: path
        name: reviews_id
        type: integer
        required: true
        description: Review ID
    responses:
      200:
        description: Review data
      404:
        description: Review not found
    """
    return make_response(jsonify(reviews_controller.find_by_id(reviews_id)), HTTPStatus.OK)


@reviews_bp.put('/<int:reviews_id>')
def bugfix_reviews(reviews_id: int) -> Response:
    """
    Update review by ID
    ---
    tags:
      - Reviews
    parameters:
      - in: path
        name: reviews_id
        type: integer
        required: true
        description: Review ID
      - in: body
        name: review
        description: Updated review data
        required: true
        schema:
          type: object
          properties:
            property_id:
              type: integer
              description: Property ID
            user_id:
              type: integer
              description: User ID
            rating:
              type: integer
              description: Rating (1-5)
            comment:
              type: string
              description: Review comment
            created_at:
              type: string
              format: date-time
              description: Creation timestamp
    responses:
      200:
        description: Review updated successfully
      404:
        description: Review not found
    """
    content = request.get_json()
    reviews = Reviews.create_from_dto(content)
    reviews_controller.bugfix(reviews_id, reviews)
    return make_response("reviews updated", HTTPStatus.OK)


@reviews_bp.patch('/<int:reviews_id>')
def patch_reviews(reviews_id: int) -> Response:
    """
    Partially update review by ID
    ---
    tags:
      - Reviews
    parameters:
      - in: path
        name: reviews_id
        type: integer
        required: true
        description: Review ID
      - in: body
        name: review
        description: Partial review data
        required: true
        schema:
          type: object
          properties:
            property_id:
              type: integer
              description: Property ID
            user_id:
              type: integer
              description: User ID
            rating:
              type: integer
              description: Rating (1-5)
            comment:
              type: string
              description: Review comment
            created_at:
              type: string
              format: date-time
              description: Creation timestamp
    responses:
      200:
        description: Review updated successfully
      404:
        description: Review not found
    """
    content = request.get_json()
    reviews_controller.patch(reviews_id, content)
    return make_response("reviews updated", HTTPStatus.OK)


@reviews_bp.delete('/<int:reviews_id>')
def delete_reviews(reviews_id: int) -> Response:
    """
    Delete review by ID
    ---
    tags:
      - Reviews
    parameters:
      - in: path
        name: reviews_id
        type: integer
        required: true
        description: Review ID
    responses:
      200:
        description: Review deleted successfully
      404:
        description: Review not found
    """
    reviews_controller.delete(reviews_id)
    return make_response("reviews deleted", HTTPStatus.OK)


@reviews_bp.get('/get-properties-after-user/<int:user_id>')
def get_property_by_user(user_id: int) -> Response:
    """
    Get properties reviewed by user ID
    ---
    tags:
      - Reviews
    parameters:
      - in: path
        name: user_id
        type: integer
        required: true
        description: User ID
    responses:
      200:
        description: List of properties reviewed by the user
      404:
        description: User not found
    """
    return make_response(jsonify(reviews_controller.get_property_by_user(user_id)),
                         HTTPStatus.OK)


@reviews_bp.get('/get-users-after-property/<int:property_id>')
def get_user_by_property(property_id: int) -> Response:
    """
    Get users who reviewed property by property ID
    ---
    tags:
      - Reviews
    parameters:
      - in: path
        name: property_id
        type: integer
        required: true
        description: Property ID
    responses:
      200:
        description: List of users who reviewed the property
      404:
        description: Property not found
    """
    return make_response(jsonify(reviews_controller.get_user_by_property(property_id)),
                         HTTPStatus.OK)
