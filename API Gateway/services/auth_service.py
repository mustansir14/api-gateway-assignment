import os

from dotenv import load_dotenv

from schemas.user import UserSchemaIn, UserSchemaOut, UserSchemaOutToken, TokenSchema
from services.client import make_request

load_dotenv()


AUTH_API = os.getenv("AUTH_API")


def login(user: UserSchemaIn) -> UserSchemaOutToken:

    return make_request("POST", url=AUTH_API + "/login", data=dict(), success_code=200, response_schema=UserSchemaOutToken)


def signup(user: UserSchemaIn) -> UserSchemaOut:

    return make_request("POST", url=AUTH_API + "/signup", data=dict(), success_code=201, response_schema=UserSchemaOut)


def decode_token(token: TokenSchema) -> UserSchemaOut:

    return make_request("POST", url=AUTH_API + "/decode_token", data=token.dict(), success_code=200, response_schema=UserSchemaOut)
