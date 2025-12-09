from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Properties(db.Model, IDto):

    __tablename__ = "properties"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    users = db.relationship("Users", backref="properties")
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey("properties_address.id"), nullable=False)
    addresses = db.relationship("PropertiesAddress", backref="properties")
    price_per_night = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self) -> str:
        return f"room_location({self.id}, {self.user_id}, {self.title}, {self.description}, {self.address_id}, {self.price_per_night}, {self.created_at})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title,
            "description": self.description,
            "address_id": self.address_id,
            "price_per_night": self.price_per_night,
            "created_at": self.created_at,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Properties:
        obj = Properties(**dto_dict)
        return obj
