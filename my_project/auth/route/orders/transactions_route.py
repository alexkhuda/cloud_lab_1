from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import transactions_controller
from my_project.auth.domain import Transactions

transactions_bp = Blueprint('transactions', __name__, url_prefix='/transactions')


@transactions_bp.get('')
def get_all_transactions() -> Response:
    """
    Get all transactions
    ---
    tags:
      - Transactions
    responses:
      200:
        description: List of all transactions
    """
    return make_response(jsonify(transactions_controller.find_all()), HTTPStatus.OK)


@transactions_bp.post('')
def create_transactions() -> Response:
    """
    Create new transaction
    ---
    tags:
      - Transactions
    parameters:
      - in: body
        name: transaction
        description: Transaction data
        required: true
        schema:
          type: object
          properties:
            booking_id:
              type: integer
              description: Booking ID
            promotion_id:
              type: integer
              description: Promotion ID
            amount:
              type: number
              format: float
              description: Transaction amount
            date:
              type: string
              format: date-time
              description: Transaction date
    responses:
      201:
        description: Transaction created successfully
    """
    content = request.get_json()
    transactions = Transactions.create_from_dto(content)
    transactions_controller.create(transactions)
    return make_response(jsonify(transactions.put_into_dto()), HTTPStatus.CREATED)


@transactions_bp.get('/<int:transactions_id>')
def get_transactions(transactions_id: int) -> Response:
    """
    Get transaction by ID
    ---
    tags:
      - Transactions
    parameters:
      - in: path
        name: transactions_id
        type: integer
        required: true
        description: Transaction ID
    responses:
      200:
        description: Transaction data
      404:
        description: Transaction not found
    """
    return make_response(jsonify(transactions_controller.find_by_id(transactions_id)), HTTPStatus.OK)


@transactions_bp.put('/<int:transactions_id>')
def bugfix_transactions(transactions_id: int) -> Response:
    """
    Update transaction by ID
    ---
    tags:
      - Transactions
    parameters:
      - in: path
        name: transactions_id
        type: integer
        required: true
        description: Transaction ID
      - in: body
        name: transaction
        description: Updated transaction data
        required: true
        schema:
          type: object
          properties:
            booking_id:
              type: integer
              description: Booking ID
            promotion_id:
              type: integer
              description: Promotion ID
            amount:
              type: number
              format: float
              description: Transaction amount
            date:
              type: string
              format: date-time
              description: Transaction date
    responses:
      200:
        description: Transaction updated successfully
      404:
        description: Transaction not found
    """
    content = request.get_json()
    transactions = Transactions.create_from_dto(content)
    transactions_controller.bugfix(transactions_id, transactions)
    return make_response("transactions updated", HTTPStatus.OK)


@transactions_bp.patch('/<int:transactions_id>')
def patch_transactions(transactions_id: int) -> Response:
    """
    Partially update transaction by ID
    ---
    tags:
      - Transactions
    parameters:
      - in: path
        name: transactions_id
        type: integer
        required: true
        description: Transaction ID
      - in: body
        name: transaction
        description: Partial transaction data
        required: true
        schema:
          type: object
          properties:
            booking_id:
              type: integer
              description: Booking ID
            promotion_id:
              type: integer
              description: Promotion ID
            amount:
              type: number
              format: float
              description: Transaction amount
            date:
              type: string
              format: date-time
              description: Transaction date
    responses:
      200:
        description: Transaction updated successfully
      404:
        description: Transaction not found
    """
    content = request.get_json()
    transactions_controller.patch(transactions_id, content)
    return make_response("transactions updated", HTTPStatus.OK)


@transactions_bp.delete('/<int:transactions_id>')
def delete_transactions(transactions_id: int) -> Response:
    """
    Delete transaction by ID
    ---
    tags:
      - Transactions
    parameters:
      - in: path
        name: transactions_id
        type: integer
        required: true
        description: Transaction ID
    responses:
      200:
        description: Transaction deleted successfully
      404:
        description: Transaction not found
    """
    transactions_controller.delete(transactions_id)
    return make_response("transactions deleted", HTTPStatus.OK)


