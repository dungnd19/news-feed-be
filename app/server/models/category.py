from typing import Optional, Type, Any

from bson import ObjectId
from pydantic import BaseModel, Field

from app.server.models.object import PyObjectId


class CategoryModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: Optional[str]
    origin_id: Optional[str]
    source_id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Jane Doe",
                "email": "jdoe@example.com",
                "course": "Experiments, Science, and Fashion in Nanophotonics",
                "gpa": "3.0",
            }
        }

    @staticmethod
    def from_db(obj: Any):
        model = CategoryModel()
        model.id = PyObjectId(obj["_id"])
        model.name = str(obj["name"])
        model.origin_id = str(obj["origin_id"])
        model.source_id = PyObjectId(obj["source_id"])

        return model
