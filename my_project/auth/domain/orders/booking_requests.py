from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class BookingRequests(db.Model, IDto):

    __tablename__ = "booking_requests"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    property_id = db.Column(db.Integer, db.ForeignKey("properties.id"), nullable=False)
    properties = db.relationship("Properties", backref="booking_requests")
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    users = db.relationship("Users", backref="booking_requests")
    status = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __repr__(self) -> str:
        return f"room_location({self.id}, {self.property_id}, {self.user_id}, {self.status}, {self.date})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "property_id": self.property_id,
            "user_id": self.user_id,
            "status": self.status,
            "date": self.date,

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> BookingRequests:
        obj = BookingRequests(**dto_dict)
        return obj
