from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Reviews(db.Model, IDto):

    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    property_id = db.Column(db.Integer, db.ForeignKey("properties.id"), nullable=False)
    properties = db.relationship("Properties", backref="reviews")
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    users = db.relationship("Users", backref="reviews")
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)


    def __repr__(self) -> str:
        return f"room_location({self.id}, {self.property_id}, {self.user_id}, {self.rating}, {self.comment}, {self.created_at})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "property_id": self.property_id,
            "user_id": self.user_id,
            "rating": self.rating,
            "comment": self.comment,
            "created_at": self.created_at
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Reviews:
        obj = Reviews(**dto_dict)
        return obj
