from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import schemas, article_controller, database

router = APIRouter(prefix="/articles", tags=["Articles"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.ArticleResponse])
def getArticle(db: Session = Depends(get_db)):
    return article_controller.get_all_articles(db)

@router.get("/{id}", response_model=schemas.ArticleResponse)
def getArticleById(id: int, db: Session = Depends(get_db)):
    return article_controller.get_article_by_id(id, db)

@router.post("/", response_model=schemas.ArticleResponse)
def createArticle(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    return article_controller.create_article(article, db)

@router.put("/{id}", response_model=schemas.ArticleResponse)
def updateArticle(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    return article_controller.update_article(id, article, db)

@router.delete("/{id}", response_model=schemas.ArticleResponse)
def deleteArticle(id: int, db: Session = Depends(get_db)):
    return article_controller.delete_article(id, db)