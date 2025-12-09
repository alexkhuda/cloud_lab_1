from typing import List

from my_project.auth.service import reviews_service
from my_project.auth.controller.general_controller import GeneralController


class ReviewsController(GeneralController):

    _service = reviews_service

    def get_property_by_user(self, user_id: int) -> List[object]:
        return self._service.get_property_by_user(user_id)

    def get_user_by_property(self, property_id: int) -> List[object]:
        return self._service.get_user_by_property(property_id)
