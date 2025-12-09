from typing import List

from my_project.auth.dao import payments_dao
from my_project.auth.service.general_service import GeneralService


class PaymentsService(GeneralService):

    _dao = payments_dao

    def get_payments_by_transaction(self, transaction_id: int) -> List[object]:
        return self._dao.get_payments_by_transaction(transaction_id)
