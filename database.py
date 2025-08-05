from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Article(Base):
    __tablename__ = 'articleList'
    id = Column(Integer, primary_key=True)
    articleHead = Column(String, nullable=False)
    articleBody = Column(String, nullable=False)
    publishedDate = Column(DateTime, default=datetime)
    tags = Column(String)

Base.metadata.create_all(bind=engine)