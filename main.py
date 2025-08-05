from fastapi import FastAPI
from . import article_routes

app = FastAPI()

@app.get("/")
async def root():
    return { "message": "Hello World" }

app.include_router(article_routes.router)