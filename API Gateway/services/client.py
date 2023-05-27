from typing import List

from fastapi import HTTPException
import requests
from pydantic import BaseModel


def make_request(method: str, url: str, data: dict, success_code: int, response_schema: BaseModel | None, respone_is_list: bool = False) -> BaseModel | List[BaseModel] | None:

    try:
        res = requests.request(method, url, json=data)
        if res.status_code == success_code:
            if response_schema is None:
                return None
            if respone_is_list:
                return [response_schema(**x) for x in res.json()]
            return response_schema(**res.json())
        error_message = res.json()
        if "detail" in error_message:
            error_message = error_message['detail']
        raise HTTPException(status_code=res.status_code,
                            detail=error_message)
    except requests.exceptions.ConnectionError:
        raise HTTPException(
            status_code=500, detail="Requested service is down. Please try again later.")
