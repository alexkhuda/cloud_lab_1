from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Promotions(db.Model, IDto):

    __tablename__ = "promotions"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    discount_percentage = db.Column(db.Float, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)


    def __repr__(self) -> str:
        return f"room_location({self.id}, {self.name}, {self.discount_percentage}, {self.start_date}, {self.end_date}, {self.created_at})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "discount_percentage": self.discount_percentage,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "created_at": self.created_at,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Promotions:
        obj = Promotions(**dto_dict)
        return obj
