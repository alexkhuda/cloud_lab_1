from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import users_controller
from my_project.auth.domain import Users

users_bp = Blueprint('users', __name__, url_prefix='/users')


@users_bp.get('')
def get_all_users() -> Response:
    """
    Get all users
    ---
    tags:
      - Users
    responses:
      200:
        description: List of all users
    """
    return make_response(jsonify(users_controller.find_all()), HTTPStatus.OK)


@users_bp.post('')
def create_users() -> Response:
    """
    Create new user
    ---
    tags:
      - Users
    parameters:
      - in: body
        name: user
        description: User data
        required: true
        schema:
          type: object
          properties:
            type:
              type: string
              description: User type (Owner, Tenant)
            first_name:
              type: string
              description: First name
            last_name:
              type: string
              description: Last name
            email:
              type: string
              description: Email address
            password_hash:
              type: string
              description: Password hash
            phone_number:
              type: string
              description: Phone number
            created_at:
              type: string
              format: date-time
              description: Creation timestamp
    responses:
      201:
        description: User created successfully
    """
    content = request.get_json()
    users = Users.create_from_dto(content)
    users_controller.create(users)
    return make_response(jsonify(users.put_into_dto()), HTTPStatus.CREATED)


@users_bp.get('/<int:users_id>')
def get_users(users_id: int) -> Response:
    """
    Get user by ID
    ---
    tags:
      - Users
    parameters:
      - in: path
        name: users_id
        type: integer
        required: true
        description: User ID
    responses:
      200:
        description: User data
      404:
        description: User not found
    """
    return make_response(jsonify(users_controller.find_by_id(users_id)), HTTPStatus.OK)


@users_bp.put('/<int:users_id>')
def bugfix_users(users_id: int) -> Response:
    """
    Update user by ID
    ---
    tags:
      - Users
    parameters:
      - in: path
        name: users_id
        type: integer
        required: true
        description: User ID
      - in: body
        name: user
        description: Updated user data
        required: true
        schema:
          type: object
          properties:
            type:
              type: string
              description: User type (Owner, Tenant)
            first_name:
              type: string
              description: First name
            last_name:
              type: string
              description: Last name
            email:
              type: string
              description: Email address
            password_hash:
              type: string
              description: Password hash
            phone_number:
              type: string
              description: Phone number
            created_at:
              type: string
              format: date-time
              description: Creation timestamp
    responses:
      200:
        description: User updated successfully
      404:
        description: User not found
    """
    content = request.get_json()
    users = Users.create_from_dto(content)
    users_controller.bugfix(users_id, users)
    return make_response("users updated", HTTPStatus.OK)


@users_bp.patch('/<int:users_id>')
def patch_users(users_id: int) -> Response:
    """
    Partially update user by ID
    ---
    tags:
      - Users
    parameters:
      - in: path
        name: users_id
        type: integer
        required: true
        description: User ID
      - in: body
        name: user
        description: Partial user data
        required: true
        schema:
          type: object
          properties:
            type:
              type: string
              description: User type (Owner, Tenant)
            first_name:
              type: string
              description: First name
            last_name:
              type: string
              description: Last name
            email:
              type: string
              description: Email address
            password_hash:
              type: string
              description: Password hash
            phone_number:
              type: string
              description: Phone number
            created_at:
              type: string
              format: date-time
              description: Creation timestamp
    responses:
      200:
        description: User updated successfully
      404:
        description: User not found
    """
    content = request.get_json()
    users_controller.patch(users_id, content)
    return make_response("users updated", HTTPStatus.OK)


@users_bp.delete('/<int:users_id>')
def delete_users(users_id: int) -> Response:
    """
    Delete user by ID
    ---
    tags:
      - Users
    parameters:
      - in: path
        name: users_id
        type: integer
        required: true
        description: User ID
    responses:
      200:
        description: User deleted successfully
      404:
        description: User not found
    """
    users_controller.delete(users_id)
    return make_response("users deleted", HTTPStatus.OK)


