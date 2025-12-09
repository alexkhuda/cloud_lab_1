from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Transactions(db.Model, IDto):

    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    booking_id = db.Column(db.Integer, db.ForeignKey("bookings.id"), nullable=False)
    bookings = db.relationship("Bookings", backref="transactions")
    promotion_id = db.Column(db.Integer, db.ForeignKey("promotions.id"), nullable=False)
    promotions = db.relationship("Promotions", backref="transactions")
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)


    def __repr__(self) -> str:
        return f"room_location({self.id}, {self.booking_id},{self.promotion_id}, {self.amount}, {self.date})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "booking_id": self.booking_id,
            "promotion_id": self.promotion_id,
            "amount": self.amount,
            "date": self.date,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Transactions:
        obj = Transactions(**dto_dict)
        return obj
