from typing import List, Dict, Any

import sqlalchemy

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Reviews


class ReviewsDAO(GeneralDAO):
    _domain_type = Reviews

    def get_property_by_user(self, user_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_properties_by_user(:p1)"),
                                       {'p1': user_id}).mappings().all()
        return [dict(row) for row in result]

    def get_user_by_property(self, property_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_users_by_property(:p1)"),
                                       {'p1': property_id}).mappings().all()
        return [dict(row) for row in result]
