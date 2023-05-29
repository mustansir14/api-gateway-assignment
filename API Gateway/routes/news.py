from typing import List

from fastapi import APIRouter
from schemas.news import ArticleSchema
from services import news_service

router = APIRouter(prefix="/news", tags=["news"])


@router.get("", response_model=List[ArticleSchema], status_code=200)
def get_news():
    return news_service.get_news()
