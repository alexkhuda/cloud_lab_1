from typing import List, Dict, Any

import sqlalchemy

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Payments


class PaymentsDAO(GeneralDAO):
    _domain_type = Payments

    def get_payments_by_transaction(self, transaction_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_payments_by_transaction(:p1)"),
                                       {'p1': transaction_id}).mappings().all()
        return [dict(row) for row in result]
