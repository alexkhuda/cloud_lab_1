from typing import List

from my_project.auth.service import property_photos_service
from my_project.auth.controller.general_controller import GeneralController


class PropertyPhotosController(GeneralController):

    _service = property_photos_service

    def get_photos_by_property(self, property_id: int) -> List[object]:
        return self._service.get_photos_by_property(property_id)
