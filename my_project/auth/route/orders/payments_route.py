from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import payments_controller
from my_project.auth.domain import Payments

payments_bp = Blueprint('payments', __name__, url_prefix='/payments')


@payments_bp.get('')
def get_all_payments() -> Response:
    """
    Get all payments
    ---
    tags:
      - Payments
    responses:
      200:
        description: List of all payments
    """
    return make_response(jsonify(payments_controller.find_all()), HTTPStatus.OK)


@payments_bp.post('')
def create_payments() -> Response:
    """
    Create new payment
    ---
    tags:
      - Payments
    parameters:
      - in: body
        name: payment
        description: Payment data
        required: true
        schema:
          type: object
          properties:
            transaction_id:
              type: integer
              description: Transaction ID
            service_fee:
              type: number
              format: float
              description: Service fee amount
            owner_amount:
              type: number
              format: float
              description: Amount for property owner
            date:
              type: string
              format: date-time
              description: Payment date
    responses:
      201:
        description: Payment created successfully
    """
    content = request.get_json()
    payments = Payments.create_from_dto(content)
    payments_controller.create(payments)
    return make_response(jsonify(payments.put_into_dto()), HTTPStatus.CREATED)


@payments_bp.get('/<int:payments_id>')
def get_payments(payments_id: int) -> Response:
    """
    Get payment by ID
    ---
    tags:
      - Payments
    parameters:
      - in: path
        name: payments_id
        type: integer
        required: true
        description: Payment ID
    responses:
      200:
        description: Payment data
      404:
        description: Payment not found
    """
    return make_response(jsonify(payments_controller.find_by_id(payments_id)), HTTPStatus.OK)


@payments_bp.put('/<int:payments_id>')
def bugfix_payments(payments_id: int) -> Response:
    """
    Update payment by ID
    ---
    tags:
      - Payments
    parameters:
      - in: path
        name: payments_id
        type: integer
        required: true
        description: Payment ID
      - in: body
        name: payment
        description: Updated payment data
        required: true
        schema:
          type: object
          properties:
            transaction_id:
              type: integer
              description: Transaction ID
            service_fee:
              type: number
              format: float
              description: Service fee amount
            owner_amount:
              type: number
              format: float
              description: Amount for property owner
            date:
              type: string
              format: date-time
              description: Payment date
    responses:
      200:
        description: Payment updated successfully
      404:
        description: Payment not found
    """
    content = request.get_json()
    payments = Payments.create_from_dto(content)
    payments_controller.bugfix(payments_id, payments)
    return make_response("payments updated", HTTPStatus.OK)


@payments_bp.patch('/<int:payments_id>')
def patch_payments(payments_id: int) -> Response:
    """
    Partially update payment by ID
    ---
    tags:
      - Payments
    parameters:
      - in: path
        name: payments_id
        type: integer
        required: true
        description: Payment ID
      - in: body
        name: payment
        description: Partial payment data
        required: true
        schema:
          type: object
          properties:
            transaction_id:
              type: integer
              description: Transaction ID
            service_fee:
              type: number
              format: float
              description: Service fee amount
            owner_amount:
              type: number
              format: float
              description: Amount for property owner
            date:
              type: string
              format: date-time
              description: Payment date
    responses:
      200:
        description: Payment updated successfully
      404:
        description: Payment not found
    """
    content = request.get_json()
    payments_controller.patch(payments_id, content)
    return make_response("payments updated", HTTPStatus.OK)


@payments_bp.delete('/<int:payments_id>')
def delete_payments(payments_id: int) -> Response:
    """
    Delete payment by ID
    ---
    tags:
      - Payments
    parameters:
      - in: path
        name: payments_id
        type: integer
        required: true
        description: Payment ID
    responses:
      200:
        description: Payment deleted successfully
      404:
        description: Payment not found
    """
    payments_controller.delete(payments_id)
    return make_response("payments deleted", HTTPStatus.OK)


@payments_bp.get('/get-payments-after-transaction/<int:transaction_id>')
def get_payments_by_transaction(transaction_id: int) -> Response:
    """
    Get payments by transaction ID
    ---
    tags:
      - Payments
    parameters:
      - in: path
        name: transaction_id
        type: integer
        required: true
        description: Transaction ID
    responses:
      200:
        description: List of payments for the transaction
      404:
        description: Transaction not found
    """
    return make_response(jsonify(payments_controller.get_payments_by_transaction(transaction_id)),
                         HTTPStatus.OK)
