from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Users(db.Model, IDto):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    type = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self) -> str:
        return f"room_location({self.id}, {self.type}, {self.first_name}, {self.last_name}, {self.email}, {self.password_hash}, {self.phone_number}, {self.created_at})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "type": self.type,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password_hash": self.password_hash,
            "phone_number": self.phone_number,
            "created_at": self.created_at,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Users:
        obj = Users(**dto_dict)
        return obj
