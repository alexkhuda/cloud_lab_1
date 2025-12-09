from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import bookings_controller
from my_project.auth.domain import Bookings

bookings_bp = Blueprint('bookings', __name__, url_prefix='/bookings')


@bookings_bp.get('')
def get_all_bookings() -> Response:
    """
    Get all bookings
    ---
    tags:
      - Bookings
    responses:
      200:
        description: List of all bookings
    """
    return make_response(jsonify(bookings_controller.find_all()), HTTPStatus.OK)


@bookings_bp.post('')
def create_bookings() -> Response:
    """
    Create new booking
    ---
    tags:
      - Bookings
    parameters:
      - in: body
        name: booking
        description: Booking data
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
            check_in_date:
              type: string
              format: date
              description: Check-in date
            check_out_date:
              type: string
              format: date
              description: Check-out date
            total_price:
              type: number
              format: float
              description: Total booking price
            date:
              type: string
              format: date-time
              description: Booking date
    responses:
      201:
        description: Booking created successfully
    """
    content = request.get_json()
    bookings = Bookings.create_from_dto(content)
    bookings_controller.create(bookings)
    return make_response(jsonify(bookings.put_into_dto()), HTTPStatus.CREATED)


@bookings_bp.get('/<int:bookings_id>')
def get_bookings(bookings_id: int) -> Response:
    """
    Get booking by ID
    ---
    tags:
      - Bookings
    parameters:
      - in: path
        name: bookings_id
        type: integer
        required: true
        description: Booking ID
    responses:
      200:
        description: Booking data
      404:
        description: Booking not found
    """
    return make_response(jsonify(bookings_controller.find_by_id(bookings_id)), HTTPStatus.OK)


@bookings_bp.put('/<int:bookings_id>')
def bugfix_bookings(bookings_id: int) -> Response:
    """
    Update booking by ID
    ---
    tags:
      - Bookings
    parameters:
      - in: path
        name: bookings_id
        type: integer
        required: true
        description: Booking ID
      - in: body
        name: booking
        description: Updated booking data
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
            check_in_date:
              type: string
              format: date
              description: Check-in date
            check_out_date:
              type: string
              format: date
              description: Check-out date
            total_price:
              type: number
              format: float
              description: Total booking price
            date:
              type: string
              format: date-time
              description: Booking date
    responses:
      200:
        description: Booking updated successfully
      404:
        description: Booking not found
    """
    content = request.get_json()
    bookings = Bookings.create_from_dto(content)
    bookings_controller.bugfix(bookings_id, bookings)
    return make_response("bookings updated", HTTPStatus.OK)


@bookings_bp.patch('/<int:bookings_id>')
def patch_bookings(bookings_id: int) -> Response:
    """
    Partially update booking by ID
    ---
    tags:
      - Bookings
    parameters:
      - in: path
        name: bookings_id
        type: integer
        required: true
        description: Booking ID
      - in: body
        name: booking
        description: Partial booking data
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
            check_in_date:
              type: string
              format: date
              description: Check-in date
            check_out_date:
              type: string
              format: date
              description: Check-out date
            total_price:
              type: number
              format: float
              description: Total booking price
            date:
              type: string
              format: date-time
              description: Booking date
    responses:
      200:
        description: Booking updated successfully
      404:
        description: Booking not found
    """
    content = request.get_json()
    bookings_controller.patch(bookings_id, content)
    return make_response("bookings updated", HTTPStatus.OK)


@bookings_bp.delete('/<int:bookings_id>')
def delete_bookings(bookings_id: int) -> Response:
    """
    Delete booking by ID
    ---
    tags:
      - Bookings
    parameters:
      - in: path
        name: bookings_id
        type: integer
        required: true
        description: Booking ID
    responses:
      200:
        description: Booking deleted successfully
      404:
        description: Booking not found
    """
    bookings_controller.delete(bookings_id)
    return make_response("bookings deleted", HTTPStatus.OK)


