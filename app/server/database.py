from typing import List

from bson import ObjectId

import motor.motor_asyncio

from app.server.models.category import CategoryModel

MONGODB_URL = "mongodb://root:anhnd15%40zalo.me@209.97.168.123:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
db = client.crawler

category_collection = db.get_collection("category")


async def retrieve_categories() -> List[CategoryModel]:
    categories = []
    async for category in category_collection.find():
        categories.append(CategoryModel.from_db(category))
    return categories
