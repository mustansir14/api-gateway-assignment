from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

from schemas.user import TokenSchema, UserSchemaOut
from services.auth_service import decode_token

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(access_token: str = Depends(oauth2_bearer)) -> UserSchemaOut:
    """
    Fetches user details for a given token.
    To be used as a dependency by authenticated routes
    """

    return decode_token(TokenSchema(access_token=access_token))
