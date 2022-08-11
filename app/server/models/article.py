from array import array
from datetime import datetime
from typing import Type, Any

from bson import ObjectId
from pydantic import BaseModel, Field

from app.server.models.object import PyObjectId


class ArticleModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    category_id: PyObjectId = Field(default_factory=PyObjectId, alias="category_id")
    checksum: str = Field(...)
    content: str = Field(...)
    created_at: datetime = Field(...)
    description: str = Field(...)
    image_url: str = Field(...)
    keywords: array = Field(...)
    origin_category_id: array = Field(...)
    origin_created_at: datetime = Field(...)
    origin_id: str = Field(...)
    origin_updated_at: datetime = Field(...)
    pred_category_id: PyObjectId = Field(default_factory=PyObjectId, alias="pred_category_id")
    source_id: PyObjectId = Field(default_factory=PyObjectId, alias="source_id")
    title: str = Field(...)
    updated_at: datetime = Field(...)
    url: str = Field(...)

    class Config:
        allow_population_by_field_name = True
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
