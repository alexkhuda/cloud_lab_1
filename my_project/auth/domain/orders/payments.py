from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Payments(db.Model, IDto):

    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    transaction_id = db.Column(db.Integer, db.ForeignKey("transactions.id"), nullable=False)
    transactions = db.relationship("Transactions", backref="payments")
    service_fee = db.Column(db.Float, nullable=False)
    owner_amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)


    def __repr__(self) -> str:
        return f"room_location({self.id}, {self.transaction_id}, {self.service_fee}, {self.owner_amount}, {self.date})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "transaction_id": self.transaction_id,
            "service_fee": self.service_fee,
            "owner_amount": self.owner_amount,
            "date": self.date,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Payments:
        obj = Payments(**dto_dict)
        return obj
