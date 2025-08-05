from pydantic import BaseModel
from datetime import datetime

class ArticleCreate(BaseModel):
    articleHead: str
    articleBody: str
    tags: str

class ArticleResponse(ArticleCreate):
    id: int
    publishedDate: datetime

    class Config:
        from_attributes = True