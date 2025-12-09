from typing import List

from my_project.auth.dao import property_photos_dao
from my_project.auth.service.general_service import GeneralService


class PropertyPhotosService(GeneralService):

    _dao = property_photos_dao

    def get_photos_by_property(self, property_id: int) -> List[object]:
        return self._dao.get_photos_by_property(property_id)
