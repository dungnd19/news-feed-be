from typing import List

from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    retrieve_categories
)
from app.server.models.category import (
    CategoryModel
)
from app.server.responses.response import ResponseModel

router = APIRouter()


@router.get(
    "/", response_description="List all categories", response_model=List[CategoryModel]
)
async def list_categories():
    return await retrieve_categories()
