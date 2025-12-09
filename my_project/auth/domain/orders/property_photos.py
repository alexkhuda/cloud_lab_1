from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class PropertyPhotos(db.Model, IDto):

    __tablename__ = "property_photos"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    property_id = db.Column(db.Integer, db.ForeignKey("properties.id"), nullable=False)
    properties = db.relationship("Properties", backref="property_photos")
    photo_url = db.Column(db.String(255), nullable=False)
    uploaded_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self) -> str:
        return f"room_location({self.id}, {self.property_id}, {self.photo_url}, {self.uploaded_at})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "property_id": self.property_id,
            "photo_url": self.photo_url,
            "uploaded_at": self.uploaded_at,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> PropertyPhotos:
        obj = PropertyPhotos(**dto_dict)
        return obj
