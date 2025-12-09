from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import booking_requests_controller
from my_project.auth.domain import BookingRequests

booking_requests_bp = Blueprint('booking_requests', __name__, url_prefix='/booking-requests')


@booking_requests_bp.get('')
def get_all_booking_requests() -> Response:
    """
    Get all booking requests
    ---
    tags:
      - BookingRequests
    responses:
      200:
        description: List of all booking requests
    """
    return make_response(jsonify(booking_requests_controller.find_all()), HTTPStatus.OK)


@booking_requests_bp.post('')
def create_booking_requests() -> Response:
    """
    Create new booking request
    ---
    tags:
      - BookingRequests
    parameters:
      - in: body
        name: booking_request
        description: Booking request data
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
            status:
              type: string
              description: Request status (Pending, Accepted, Rejected)
            date:
              type: string
              format: date-time
              description: Request date
    responses:
      201:
        description: Booking request created successfully
    """
    content = request.get_json()
    booking_requests = BookingRequests.create_from_dto(content)
    booking_requests_controller.create(booking_requests)
    return make_response(jsonify(booking_requests.put_into_dto()), HTTPStatus.CREATED)


@booking_requests_bp.get('/<int:booking_requests_id>')
def get_booking_requests(booking_requests_id: int) -> Response:
    """
    Get booking request by ID
    ---
    tags:
      - BookingRequests
    parameters:
      - in: path
        name: booking_requests_id
        type: integer
        required: true
        description: Booking request ID
    responses:
      200:
        description: Booking request data
      404:
        description: Booking request not found
    """
    return make_response(jsonify(booking_requests_controller.find_by_id(booking_requests_id)), HTTPStatus.OK)


@booking_requests_bp.put('/<int:booking_requests_id>')
def bugfix_booking_requests(booking_requests_id: int) -> Response:
    """
    Update booking request by ID
    ---
    tags:
      - BookingRequests
    parameters:
      - in: path
        name: booking_requests_id
        type: integer
        required: true
        description: Booking request ID
      - in: body
        name: booking_request
        description: Updated booking request data
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
            status:
              type: string
              description: Request status (Pending, Accepted, Rejected)
            date:
              type: string
              format: date-time
              description: Request date
    responses:
      200:
        description: Booking request updated successfully
      404:
        description: Booking request not found
    """
    content = request.get_json()
    booking_requests = BookingRequests.create_from_dto(content)
    booking_requests_controller.bugfix(booking_requests_id, booking_requests)
    return make_response("booking_requests updated", HTTPStatus.OK)


@booking_requests_bp.patch('/<int:booking_requests_id>')
def patch_booking_requests(booking_requests_id: int) -> Response:
    """
    Partially update booking request by ID
    ---
    tags:
      - BookingRequests
    parameters:
      - in: path
        name: booking_requests_id
        type: integer
        required: true
        description: Booking request ID
      - in: body
        name: booking_request
        description: Partial booking request data
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
            status:
              type: string
              description: Request status (Pending, Accepted, Rejected)
            date:
              type: string
              format: date-time
              description: Request date
    responses:
      200:
        description: Booking request updated successfully
      404:
        description: Booking request not found
    """
    content = request.get_json()
    booking_requests_controller.patch(booking_requests_id, content)
    return make_response("booking_requests updated", HTTPStatus.OK)


@booking_requests_bp.delete('/<int:booking_requests_id>')
def delete_booking_requests(booking_requests_id: int) -> Response:
    """
    Delete booking request by ID
    ---
    tags:
      - BookingRequests
    parameters:
      - in: path
        name: booking_requests_id
        type: integer
        required: true
        description: Booking request ID
    responses:
      200:
        description: Booking request deleted successfully
      404:
        description: Booking request not found
    """
    booking_requests_controller.delete(booking_requests_id)
    return make_response("booking_requests deleted", HTTPStatus.OK)


