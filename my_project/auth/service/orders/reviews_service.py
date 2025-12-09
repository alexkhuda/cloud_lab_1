from typing import List

from my_project.auth.dao import reviews_dao
from my_project.auth.service.general_service import GeneralService


class ReviewsService(GeneralService):

    _dao = reviews_dao

    def get_property_by_user(self, user_id: int) -> List[object]:
        return self._dao.get_property_by_user(user_id)

    def get_user_by_property(self, property_id: int) -> List[object]:
        return self._dao.get_user_by_property(property_id)

