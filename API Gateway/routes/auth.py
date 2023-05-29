from fastapi import APIRouter

from schemas.user import UserSchemaOutToken, UserSchemaIn, UserSchemaOut
from services import auth_service

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=UserSchemaOutToken, status_code=200)
async def login(user: UserSchemaIn):

    return auth_service.login(user)


@router.post("/signup", response_model=UserSchemaOut, status_code=201)
async def signup(user: UserSchemaIn):

    return auth_service.signup(user)
