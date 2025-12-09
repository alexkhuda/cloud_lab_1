from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class PropertiesAddress(db.Model, IDto):

    __tablename__ = "properties_address"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(255), nullable=False)

    def __repr__(self) -> str:
        return f"room_location({self.id}, {self.address}, {self.city}, {self.country})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "address": self.address,
            "city": self.city,
            "country": self.country,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> PropertiesAddress:
        obj = PropertiesAddress(**dto_dict)
        return obj
