from fastapi import FastAPI

from app.server.routes.category import router as CategoryRouter

app = FastAPI()

app.include_router(CategoryRouter, tags=["Categories"], prefix="/categories")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}