from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .database import Article
from . import schemas

def get_all_articles(db: Session):
    return db.query(Article).all()

def get_article_by_id(id: int, db: Session):
    article = db.query(Article).filter(Article.id == id).first()
    if not article:
        raise HTTPException (
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Article with ID {id} not found"
        )
    return article

def create_article(article_data: schemas.ArticleCreate, db: Session):
    new_article = Article(
        articleHead = article_data.articleHead,
        articleBody = article_data.articleBody,
        tags = article_data.tags
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article

def update_article(id: int, article_data: schemas.ArticleCreate, db: Session):
    article = db.query(Article).filter(Article.id == id).first()
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Article with ID {id} not found"
        )

    article.articleHead = article_data.articleHead
    article.articleBody = article_data.articleBody
    article.tags = article_data.tags

    db.commit()
    db.refresh(article)
    return article

def delete_article(id: int, db: Session):
    article = db.query(Article).filter(Article.id == id).first()
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Article with ID {id} not found"
        )

    db.delete(article)
    db.commit()
    return { "message": f"Article with ID {id} deleted successfully" }