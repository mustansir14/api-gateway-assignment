from typing import List

from services.client import make_request
from schemas.news import ArticleSchema

import os

NEWS_API = os.getenv("NEWS_API")


def get_news() -> List[ArticleSchema]:
    return make_request("GET", NEWS_API + "/news/", {}, 200, response_schema=ArticleSchema, respone_is_list=True)
