from typing import List

from pydantic import BaseModel


class ArticleSchema(BaseModel):

    title: str
    url: str
