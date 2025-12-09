from typing import List, Dict, Any

import sqlalchemy

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import PropertyPhotos


class PropertyPhotosDAO(GeneralDAO):
    _domain_type = PropertyPhotos

    def get_photos_by_property(self, property_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_photos_by_property(:p1)"),
                                       {'p1': property_id}).mappings().all()
        return [dict(row) for row in result]

