from typing import List

from my_project.auth.service import payments_service
from my_project.auth.controller.general_controller import GeneralController


class PaymentsController(GeneralController):

    _service = payments_service

    def get_payments_by_transaction(self, transaction_id: int) -> List[object]:
        return self._service.get_payments_by_transaction(transaction_id)
