from my_project.auth.service import transactions_service
from my_project.auth.controller.general_controller import GeneralController


class TransactionsController(GeneralController):

    _service = transactions_service
