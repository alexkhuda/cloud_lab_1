from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Bookings(db.Model, IDto):

    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    property_id = db.Column(db.Integer, db.ForeignKey("properties.id"), nullable=False)
    properties = db.relationship("Properties", backref="bookings")
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    users = db.relationship("Users", backref="bookings")
    check_in_date = db.Column(db.DateTime, nullable=False)
    check_out_date = db.Column(db.DateTime, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)


    def __repr__(self) -> str:
        return f"room_location({self.id}, {self.property_id}, {self.user_id}, {self.check_in_date}, {self.check_out_date}, {self.total_price}, {self.date})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "property_id": self.property_id,
            "user_id": self.user_id,
            "check_in_date": self.check_in_date,
            "check_out_date": self.check_out_date,
            "total_price": self.total_price,
            "date": self.date,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Bookings:
        obj = Bookings(**dto_dict)
        return obj
